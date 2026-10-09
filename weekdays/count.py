"""Weekday arithmetic. Monday through Friday count. The ends are included."""

from __future__ import annotations

from datetime import date, timedelta


class DateError(Exception):
    """The dates cannot be counted."""


def parse_iso(text: str) -> date:
    try:
        return date.fromisoformat(text)
    except ValueError as exc:
        raise DateError(f"{text} is not a YYYY-MM-DD date") from exc


def inclusive_weekdays(start: date, end: date) -> int:
    if end < start:
        raise DateError("end is before start")
    count = 0
    day = start
    while day <= end:
        if day.weekday() < 5:
            count += 1
        day += timedelta(days=1)
    return count
