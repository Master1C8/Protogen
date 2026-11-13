"""Continue a finished preparation wave through translation and author review."""

import concurrent.futures
import datetime
import fcntl
import json
import os
import pathlib
import re
import subprocess
import sys
import time

if len(sys.argv) != 3:
    raise SystemExit("Usage: continue_locale_text.py <fresh-run-dir> <prior-run-dir>")
directory, prior = (pathlib.Path(arg).resolve() for arg in sys.argv[1:])
root = pathlib.Path(__file__).resolve().parents[1]
if pathlib.Path.cwd() != root or directory.parent != root / "text-assets":
    raise SystemExit("Run from the canonical checkout with a fresh text-assets run directory")
if directory.exists():
    raise SystemExit(f"Run directory already exists: {directory}")
manifest = json.loads((prior / "manifest.json").read_text())
status = directory / "status.json"
model = "gpt-6.1-terra"
effort = "high"
sessions = pathlib.Path.home() / ".codex" / "sessions"
def write(path, data):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2) + "\n")
    tmp.replace(path)

def events(path):
    if path.is_file():
        with path.open() as handle:
            for line in handle:
                try:
                    yield json.loads(line)
                except ValueError:
                    continue

def rollout(thread):
    for date in (datetime.date.today(), datetime.date.today() - datetime.timedelta(days=1)):
        yield from (sessions / date.strftime("%Y/%m/%d")).glob(f"rollout-*-{thread}.jsonl")

def context(thread):
    for file in rollout(thread):
        settings = None
        for event in events(file):
            payload = event.get("payload", {})
            if payload.get("type") == "thread_settings_applied" and payload.get("thread_id") == thread:
                settings = payload.get("thread_settings", {})
            if payload.get("type") == "task_started" and settings:
                yield {"turn_id": payload["turn_id"], "model": settings.get("model"),
                       "effort": settings.get("reasoning_effort")}
            elif event.get("type") == "turn_context":
                yield payload


import contextlib
import io
import threading
validation_lock = threading.Lock()

sys.path.insert(0, str(pathlib.Path.cwd() / "tools"))
from build_localization import edition_text, story_rows, string_keys, load_dialogue, unique_strings
base_inventory = json.loads(pathlib.Path("text-assets/inventory.json").read_text())
dlc_inventory = json.loads(pathlib.Path("text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json").read_text())
alias_keys = set(json.loads(pathlib.Path("localization/nsfw-story-aliases.json").read_text()))
expected = (set(story_rows(base_inventory)), string_keys(base_inventory),
            set(story_rows(dlc_inventory)) - set(story_rows(base_inventory)) - alias_keys,
            string_keys(dlc_inventory) - string_keys(base_inventory))
if (manifest["model"], manifest["effort"]) != (model, effort):
    raise SystemExit("Unapproved localization model or reasoning effort")
if pathlib.Path(manifest["project"]).resolve() != root:
    raise SystemExit("Prior run belongs to a different project")
codes = tuple(manifest["locales"])
if not codes or any(not re.fullmatch(r"[a-z]{2,3}(?:-[A-Za-z0-9]+)?", code) for code in codes):
    raise SystemExit("Invalid locale list")
originals = {code: json.loads((prior / code / "status.json").read_text()) for code in codes}
for code, original in originals.items():
    if (original["locale"] != code or original["state"] != "turn_completed"
            or original["exit_code"] != 0 or (original["model"], original["effort"]) != (model, effort)
            or not re.fullmatch(r"[0-9a-f-]{36}", original["thread_id"])):
        raise SystemExit(f"Invalid prior receipt for {code}")
    if not list(context(original["thread_id"])):
        raise SystemExit(f"Session telemetry missing for {code}")
queue_lock = (prior / "continuation.lock").open("a")
try:
    fcntl.flock(queue_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    raise SystemExit("This preparation wave already has an active continuation")
directory.mkdir()

def coverage(path):
    files = [path / name for name in ("dialogue.tsv", "strings.json", "nsfw/dialogue.tsv", "nsfw/strings.json")]
    actual = [set() if not f.exists() else set(load_dialogue(f) if f.suffix == ".tsv" else json.loads(f.read_text(), object_pairs_hook=unique_strings)) for f in files]
    return [len(found & allowed) for found, allowed in zip(actual, expected)]

def strict(path):
    result = io.StringIO()
    with validation_lock, contextlib.redirect_stdout(result):
        edition_text(base_inventory, dlc_inventory, path, False)

def worker(locale):
    work = directory / locale
    work.mkdir()
    receipt = work / "status.json"
    path = pathlib.Path("localization") / locale
    thread = originals[locale]["thread_id"]
    previous_checkpoint = prior / locale / "STATUS.md"
    last = coverage(path)
    target = [len(s) for s in expected]
    stalled = 0
    prior_audit_total = 0
    decisions = path / "special-scenes.md"
    prior_decisions = decisions.read_bytes() if decisions.exists() else None
    for round_number in range(1, 81):
        run = work / f"turn-{round_number:03}"
        run.mkdir()
        log = run / "events.jsonl"
        marker = run / "model-verified.json"
        args = [manifest["cli"], "exec", "resume", "-m", model, "-c", 'model_reasoning_effort="high"',
                "-c", 'approval_policy="never"', "--json", "-o", str(run / "final.md"), thread, "-"]
        prompt = f"""Continue your own My Furry Protogen {locale} translation from saved work. The current owner decision explicitly supersedes the earlier instruction to wait for CrossOver: start translating now and leave runtime and visual verification for a later joint pass. Untested rendering stays unverified and does not stop text work. Read the updated localization/STATUS.md queue rule. Reuse your existing preparation checkpoint in localization/{locale}/STATUS.md or {previous_checkpoint}. Do not repeat the preparation pass. This session owns text and editorial only, with runtime, fonts, screenshots, packaging and Git integration assigned to the coordinator. No other models, delegated jobs, game launches, Git writes, or shared-file edits. Reuse pinned instructions and earlier accepted evidence without rereading unchanged files. Before source work wait up to 90 seconds for {marker} confirming your new turn is Terra high.

The coordinator resumes you automatically from saved checkpoints if the CLI ends while text work remains. This turn must complete a substantial concrete batch. Use locale-private checkpoints in localization/{locale} and scratch in {run}; keep dialogue.tsv, strings.json, nsfw/dialogue.tsv and nsfw/strings.json as canonical authored inputs. Read existing rows, keep valid translations, and add missing keys in source/scene order with their original English context and approved glossary. First finish and review target wording and source-bound decisions for all applicable special scenes before ordinary translation. Save decisions in localization/{locale}/special-scenes.md so the next turn can reuse them. Integrate saved special-scene drafts after checking their decisions. Read a bounded contextual batch at a time, author wording yourself, apply and validate it before proceeding. Prioritize working on the corpus instead of rediscovering tooling or producing narrative status. Current saved coverage, in order base dialogue, base UI, explicitly authored DLC-only dialogue, DLC UI: {last}, targets {target}. The remaining DLC story IDs are populated by the existing alias mechanism; do not author an alias key.

If text is incomplete, aim to finish at least 120 additional actual rows in this turn where source and context permit. If complete, run strict text validation and complete the full English comparison as durable batches, correcting objectively wrong rows and saving exact audited stable IDs in localization/{locale}/semantic-coverage.json, a JSON object with arrays base_story, base_ui, dlc_story, dlc_ui using the same four authored ID sets as above. Record the reproducible dependency closure and leave independent review pending when unavailable. Update STATUS.md and preserve all findings. Continue from any existing audit checkpoint. A turn ending is not the end of the assignment. A real blocker must describe the exact missing input or source evidence; otherwise save the batch and keep translating."""
        (run / "prompt.md").write_text(prompt)
        env = os.environ.copy()
        env.pop("CODEX_THREAD_ID", None)
        env.pop("CODEX_SESSION_ID", None)
        env.pop("CODEX_INTERNAL_ORIGINATOR_OVERRIDE", None)
        seen = {p.get("turn_id") for p in context(thread)}
        with (run / "prompt.md").open() as inp, log.open("w") as out, (run / "stderr.log").open("w") as err:
            proc = subprocess.Popen(args, stdin=inp, stdout=out, stderr=err, env=env)
            record = {"locale":locale, "thread_id":thread, "round":round_number, "pid":proc.pid,
                      "state":"starting", "coverage":last, "target":target}
            write(receipt, record)
            actual = None
            deadline = time.monotonic() + 75
            while time.monotonic() < deadline:
                actual = next((p for p in context(thread) if p.get("turn_id") not in seen), None)
                if actual or proc.poll() is not None:
                    break
                time.sleep(.5)
            if not actual or (actual.get("model"), actual.get("effort")) != (model, effort):
                if proc.poll() is None:
                    proc.terminate()
                record.update(state="model_verification_failed", exit_code=proc.wait())
                write(receipt, record)
                return
            verified = {"thread_id":thread,"turn_id":actual["turn_id"],"model":model,"effort":effort}
            write(marker,verified)
            record.update(state="running",**verified)
            write(receipt,record)
            exit_code = proc.wait()
        terminal = next((e for e in reversed(list(events(log))) if e["type"] in ("turn.completed","turn.failed")), {})
        current = coverage(path)
        audit_file = path / "semantic-coverage.json"
        audit = json.loads(audit_file.read_text()) if audit_file.exists() else {}
        reviewed = [len(set(audit.get(key, [])) & allowed) for key, allowed in zip(("base_story","base_ui","dlc_story","dlc_ui"),expected)]
        audit_total = sum(reviewed)
        record.update(state="turn_ended", coverage=current, semantic_coverage=reviewed, exit_code=exit_code,
                      reported_usage=terminal.get("usage"))
        if current == reviewed == target:
            try:
                strict(path)
            except (ValueError, RuntimeError, AssertionError, SystemExit) as exc:
                record["validation_error"] = str(exc)
            else:
                record["state"] = "text_complete"
        if exit_code != 0 or terminal.get("type") != "turn.completed":
            record["state"] = "worker_error"
        write(run / "status.json",record)
        write(receipt,record)
        if record["state"] in ("text_complete","worker_error"):
            return
        current_decisions = decisions.read_bytes() if decisions.exists() else None
        if current == last and audit_total == prior_audit_total and current_decisions == prior_decisions:
            stalled += 1
        else:
            stalled = 0
        last = current
        prior_audit_total = audit_total
        prior_decisions = current_decisions
        if stalled >= 3:
            record["state"] = "checkpoint_needs_reconciliation"
            write(receipt,record)
            return
    record["state"] = "checkpoint_needs_reconciliation"
    write(receipt,record)

write(status, {"pid":os.getpid(),"model":model,"effort":effort,"state":"active",
               "jobs":{code:str(directory / code / "status.json") for code in codes}})
with concurrent.futures.ThreadPoolExecutor(max_workers=len(codes)) as pool:
    runs = {code:pool.submit(worker, code) for code in codes}
    for code, run in runs.items():
        try:
            run.result()
        except Exception as exc:
            write(directory / code / "status.json", {"locale":code,"state":"launcher_error","error":str(exc)})
final = json.loads(status.read_text())
final["state"] = "sessions_ended"
write(status,final)
