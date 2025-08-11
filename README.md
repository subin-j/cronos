```bash
cronos/
├── cli.py
├── cronos.py
├── test_cronos.py
├── utils.py
├── README.md
├── requirements.txt
└── venv/
```

# Cronos — Cron Expression Parser

## Overview
A simple CLI that parses a standard 5-field cron expression and expands each field into concrete values.

## Requirements
- Python 3.x
- OS X/ Linux environment

## Local Run (macOS/Linux)

Activate venv
```bash
python3 -m venv .venv && source .venv/bin/activate
```
```bash
pip install -r requirements.txt
```

### Run the app (example command)
```bash
python3 cli.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```
### Example Output

```text
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```
