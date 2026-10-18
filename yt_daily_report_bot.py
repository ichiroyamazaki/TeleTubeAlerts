"""
YouTube daily report -> Telegram.

Sends your channel's added views and subscribers every day at 11:30 PM
Philippine time (Asia/Manila).

Setup:
    pip install requests tzdata
    python yt_daily_report_bot.py          # runs forever, reports daily at 23:30
    python yt_daily_report_bot.py --now    # send a report right now (for testing)

Settings are read from the .env file next to this script.
"""

import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = BASE_DIR / "stats_history.json"
TZ = ZoneInfo("Asia/Manila")
REPORT_HOUR, REPORT_MINUTE = 23, 30


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env(BASE_DIR / ".env")

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
MY_CHAT_ID = os.environ.get("MY_CHAT_ID", "")


# ---------- YouTube ----------
def get_channel_stats() -> dict:
    r = requests.get(
        "https://www.googleapis.com/youtube/v3/channels",
        params={"part": "snippet,statistics", "id": CHANNEL_ID, "key": YOUTUBE_API_KEY},
        timeout=30,
    )
    r.raise_for_status()
    items = r.json().get("items", [])
    if not items:
        raise RuntimeError("Channel not found. Check CHANNEL_ID.")
    item = items[0]
    stats = item["statistics"]
    return {
        "title": item["snippet"]["title"],
        "views": int(stats.get("viewCount", 0)),
        "subs": int(stats.get("subscriberCount", 0)),
        "subs_hidden": bool(stats.get("hiddenSubscriberCount", False)),
        "videos": int(stats.get("videoCount", 0)),
    }


# ---------- History ----------
def load_history() -> dict:
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


def save_history(history: dict) -> None:
    HISTORY_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")


# ---------- Telegram ----------
def send_telegram(text: str) -> None:
    r = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
        json={"chat_id": MY_CHAT_ID, "text": text},
        timeout=30,
    )
    r.raise_for_status()


# ---------- Report ----------
def signed(n: int) -> str:
    return f"+{n:,}" if n > 0 else f"{n:,}"


def build_and_send_report() -> None:
    stats = get_channel_stats()
    today = datetime.now(TZ).date().isoformat()

    history = load_history()
    previous_dates = sorted(d for d in history if d < today)
    previous = history[previous_dates[-1]] if previous_dates else None

    history[today] = {"views": stats["views"], "subs": stats["subs"]}
    save_history(history)

    lines = [
        f"📊 Daily Report - {stats['title']}",
        f"📅 {datetime.now(TZ).strftime('%A, %B %d, %Y')}",
        "",
    ]

    if previous:
        added_views = stats["views"] - previous["views"]
        added_subs = stats["subs"] - previous["subs"]
        lines.append(f"👁 Added views: {signed(added_views)}")
        if stats["subs_hidden"]:
            lines.append("👥 Subscribers: hidden by the channel")
        else:
            lines.append(f"👥 Added subscribers: {signed(added_subs)}")
        lines.append(f"(compared with {previous_dates[-1]})")
    else:
        lines.append("First run - saved today's numbers as the baseline.")
        lines.append("You'll get daily changes starting tomorrow.")

    lines += [
        "",
        "Totals",
        f"👁 Views: {stats['views']:,}",
        f"👥 Subscribers: {'hidden' if stats['subs_hidden'] else format(stats['subs'], ',')}",
        f"🎬 Videos: {stats['videos']:,}",
    ]
    send_telegram("\n".join(lines))
    print(f"[{datetime.now(TZ):%Y-%m-%d %H:%M:%S}] Report sent.")


# ---------- Scheduler ----------
def next_run_time(now: datetime) -> datetime:
    target = now.replace(hour=REPORT_HOUR, minute=REPORT_MINUTE, second=0, microsecond=0)
    if target <= now:
        target += timedelta(days=1)
    return target


def run_forever() -> None:
    print("Bot running. Daily report at 11:30 PM Philippine time.")
    while True:
        now = datetime.now(TZ)
        target = next_run_time(now)
        print(f"Next report: {target:%Y-%m-%d %H:%M %Z}")
        while datetime.now(TZ) < target:
            remaining = (target - datetime.now(TZ)).total_seconds()
            time.sleep(max(1, min(remaining, 30)))

        for attempt in range(1, 4):
            try:
                build_and_send_report()
                break
            except Exception as e:  # network / API hiccup: retry a few times
                print(f"Attempt {attempt} failed: {type(e).__name__}")
                time.sleep(60)
        time.sleep(61)  # make sure we don't fire twice in the same minute


if __name__ == "__main__":
    missing = [k for k in ("TELEGRAM_TOKEN", "YOUTUBE_API_KEY", "CHANNEL_ID", "MY_CHAT_ID") if not globals()[k]]
    if missing:
        sys.exit(f"Missing settings in .env: {', '.join(missing)}")

    if "--now" in sys.argv:
        build_and_send_report()
    else:
        run_forever()
