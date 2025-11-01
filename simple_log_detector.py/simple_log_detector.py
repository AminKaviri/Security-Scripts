# simple_log_detector.py
# A minimal script to detect suspicious patterns in log files.

keywords = ["error", "failed", "unauthorized", "denied"]

with open("sample.log", "r", encoding="utf-8") as log:
    for line_num, line in enumerate(log, 1):
        for word in keywords:
            if word.lower() in line.lower():
                print(f"[Line {line_num}] Suspicious pattern ({word}) → {line.strip()}")