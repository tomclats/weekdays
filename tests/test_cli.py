"""The weekday command is the product. These tests run it."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "weekdays", *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class WeekdaysCommandTest(unittest.TestCase):
    def test_shipped_span_is_seven_weekdays(self) -> None:
        dates = (ROOT / "fixtures" / "span.txt").read_text(encoding="utf-8").split()
        self.assertEqual(dates, ["2026-10-01", "2026-10-09"])
        result = run(dates)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "7\n")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("2026-10-01", readme)
        self.assertIn("2026-10-09", readme)
        self.assertIn("\n7\n", readme)

    def test_same_dates_print_the_same_count_twice(self) -> None:
        args = ["2026-10-01", "2026-10-09"]
        first = run(args)
        second = run(args)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stdout, "7\n")

    def test_one_monday_is_one_and_a_weekend_is_zero(self) -> None:
        monday = run(["2026-10-05", "2026-10-05"])
        self.assertEqual(monday.returncode, 0, monday.stderr)
        self.assertEqual(monday.stdout, "1\n")
        weekend = run(["2026-10-03", "2026-10-04"])
        self.assertEqual(weekend.returncode, 0, weekend.stderr)
        self.assertEqual(weekend.stdout, "0\n")
        full_week = run(["2026-10-05", "2026-10-09"])
        self.assertEqual(full_week.stdout, "5\n")

    def test_reversed_dates_are_an_error(self) -> None:
        result = run(["2026-10-09", "2026-10-01"])
        self.assertEqual(result.returncode, 1)
        self.assertIn("end is before start", result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
