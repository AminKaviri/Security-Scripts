# Simple Log Detector

A minimal Python script for detecting basic suspicious patterns in log files.

## 🔍 Description
This script scans a log file (e.g., `sample.log`) and prints lines containing any of these suspicious keywords:

- `error`
- `failed`
- `unauthorized`
- `denied`

## 🧠 How It Works
1. Opens the file `sample.log` line by line
2. Checks each line for the above keywords (case-insensitive)
3. Prints the line number and the detected keyword for any match

## 🚀 Usage
```bash
python simple_log_detector.py
```
Make sure a `sample.log` file exists in the same directory.

## 📂 Example Output
```text
[Line 1] Suspicious pattern (failed) → User login failed
[Line 2] Suspicious pattern (denied) → Connection denied to database
```

---
**Author:** Amin Kaviri  
**Project:** security-scripts  
**Purpose:** Learning cybersecurity automation with Python
