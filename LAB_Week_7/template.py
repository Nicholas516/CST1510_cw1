"""
RECORD CHECK  -  my version
===========================

Name  :  Nicholas
Lane  :  IT
Date  :  2026-11-12

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Parse one 'hostname, key=value, ...' line into a clean dict."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip()

    result = {"hostname": hostname}
    for piece in rest.split(","):
        key, value = piece.split("=")
        result[key.strip()] = float(value.strip())
    return result


def status_of(record):
    """Return OVER LIMIT, WARNING or OK based on used/total percent."""
    percent = record["used"] / record["total"] * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
raw_records = []
with open("messy_lines.txt") as f:
    for line in f:
        if line.strip():
            raw_records.append(line)


# =============================================================== PROCESS + OUTPUT
flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    if status != "OK":
        flagged += 1
    print(record, "->", status)

print(f"{len(raw_records)} records, {flagged} flagged")
