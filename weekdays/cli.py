"""Command line for weekdays."""

from __future__ import annotations

import argparse
import sys

from weekdays import __version__
from weekdays.count import DateError, inclusive_weekdays, parse_iso


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="weekdays",
        description="Count inclusive weekdays between two ISO dates.",
    )
    parser.add_argument("--version", action="version", version=f"weekdays {__version__}")
    parser.add_argument("start", help="First date, YYYY-MM-DD, included.")
    parser.add_argument("end", help="Last date, YYYY-MM-DD, included.")
    args = parser.parse_args(argv)
    try:
        count = inclusive_weekdays(parse_iso(args.start), parse_iso(args.end))
    except DateError as exc:
        print(f"weekdays: {exc}", file=sys.stderr)
        return 1
    print(count)
    return 0
