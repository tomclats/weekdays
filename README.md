# weekdays

Count the weekdays from one ISO date through another. Both ends count. Saturday and Sunday do not. The dates are arguments. The tool does not look up today.

```
python3 -m weekdays 2026-10-01 2026-10-09
```

```
7
```

1 October 2026 is a Thursday and 9 October 2026 is a Friday. The nine calendar days include the weekend of the 3rd and the 4th, so seven days count. The same two dates always print the same line. Those dates also ship in `fixtures/span.txt`.

## Will not do

- Holidays, half days, or a time zone
- "Today" or the system clock
- A calendar file or an account

## Tests

```
python3 -m unittest discover -s tests -v
```

Python 3.11 or newer. The standard library is enough.

## License

MIT.
