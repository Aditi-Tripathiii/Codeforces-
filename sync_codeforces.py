#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path.cwd().resolve()
CODEFORCES_DIR = ROOT / "Codeforces"
SEEN_FILE = ROOT / ".codeforces_seen.json"


def sanitize_name(value: str) -> str:
    value = value.strip()
    value = re.sub(r"[^A-Za-z0-9_. -]+", "_", value)
    value = re.sub(r"\s+", "_", value)
    value = value.strip("._ ")
    return value or "solution"


def load_seen() -> dict:
    if not SEEN_FILE.exists():
        return {}
    try:
        data = json.loads(SEEN_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_seen(seen: dict) -> None:
    SEEN_FILE.write_text(json.dumps(seen, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def fetch_recent_submissions(handle: str, count: int = 200) -> list:
    url = "https://codeforces.com/api/user.status"
    params = {"handle": handle, "from": 1, "count": count}
    resp = requests.get(url, params=params, timeout=20)
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("status") != "OK":
        raise RuntimeError(f"Codeforces API error: {payload}")
    return payload.get("result", [])


def fetch_submission_source(contest_id: int, submission_id: int) -> str:
    url = f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}"
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    selectors = [
        "#program-source-text",
        "pre[id='program-source-text']",
        "textarea[id='program-source-text']",
        "pre.program-source",
        "div.source",
        "textarea",
    ]
    for selector in selectors:
        el = soup.select_one(selector)
        if el is not None:
            text = el.get_text()
            if text.strip():
                return text

    match = re.search(r"source\s*:\s*'([^']+)'", soup.get_text(), re.DOTALL)
    if match:
        return match.group(1)

    raise RuntimeError(f"Could not locate source for submission {submission_id} in contest {contest_id}")


def build_target_path(problem: dict, contest_id: int) -> Path:
    CODEFORCES_DIR.mkdir(parents=True, exist_ok=True)
    name = problem.get("name") or problem.get("index") or "solution"
    index = problem.get("index", "")
    filename = f"{contest_id}_{index}_{sanitize_name(name)}.cpp"
    return CODEFORCES_DIR / filename


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=str(ROOT), check=False, capture_output=True, text=True)


def push_to_repo() -> None:
    status = git("status", "--short")
    if not status.stdout.strip():
        return

    add = git("add", "Codeforces")
    if add.returncode != 0:
        raise RuntimeError(f"git add failed: {add.stdout}\n{add.stderr}")

    commit = git("commit", "-m", "Auto-sync Codeforces solution")
    if commit.returncode != 0:
        if "nothing to commit" in (commit.stdout + commit.stderr).lower():
            return
        raise RuntimeError(f"git commit failed: {commit.stdout}\n{commit.stderr}")

    push = git("push", "origin", "HEAD")
    if push.returncode != 0:
        raise RuntimeError(f"git push failed: {push.stdout}\n{push.stderr}")


def sync_once(handle: str) -> bool:
    submissions = fetch_recent_submissions(handle, count=200)
    if not submissions:
        return False

    seen = load_seen()
    created_any = False

    for submission in submissions:
        verdict = submission.get("verdict")
        if verdict != "OK":
            continue

        contest_id = submission.get("contestId")
        submission_id = submission.get("id")
        problem = submission.get("problem")
        if not contest_id or not submission_id or not problem:
            continue

        key = f"{contest_id}-{submission_id}"
        if key in seen:
            continue

        try:
            source = fetch_submission_source(contest_id, submission_id)
        except Exception as exc:
            print(f"Skipping {key}: {exc}", file=sys.stderr)
            continue

        target = build_target_path(problem, contest_id)
        target.write_text(source, encoding="utf-8")
        seen[key] = submission_id
        created_any = True

    if created_any:
        save_seen(seen)
        push_to_repo()
        return True

    save_seen(seen)
    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Auto-sync Codeforces accepted submissions to this GitHub repo.")
    parser.add_argument("--handle", default=os.getenv("CODEFORCES_HANDLE", "aditi_101"), help="Codeforces handle to monitor.")
    parser.add_argument("--once", action="store_true", help="Run a single sync and exit.")
    parser.add_argument("--interval", type=int, default=int(os.getenv("CODEFORCES_INTERVAL", "60")), help="Polling interval in seconds.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    handle = args.handle.strip()
    if not handle:
        print("Error: a Codeforces handle is required.", file=sys.stderr)
        return 2

    try:
        if args.once:
            sync_once(handle)
            return 0

        while True:
            try:
                sync_once(handle)
            except Exception as exc:
                print(f"Sync failed: {exc}", file=sys.stderr)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
