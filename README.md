# Log Analyzer

This simple Python script analyzes system log files to detect suspicious login attempts.
It searches for patterns like `Failed password` or `Invalid user` entries, often found in `/var/log/auth.log` on Linux systems.

## Features
- Detects failed or unauthorized login attempts
- Lightweight and educational for cybersecurity learners

## Usage
```bash
python3 log_analyzer.py
