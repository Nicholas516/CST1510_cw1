"""
RECORD CHECK  -  my version
===========================

Name  :  Nicholas
Lane  :  IT
Date  :  2026-05-11

Run it:   python template.py
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read the CSV file we made. Header is: hostname,used_gb,total_gb
#    Each row is a server and how full its disk is.

df = pd.read_csv("servers.csv")   # load the data into a DataFrame


# ================================================================= PROCESS
# 2. Work out how full each server is as a percentage.
#    used_gb / total_gb, times 100 so it reads like a normal percent.

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# Now tag each row with a status based on that percent.
# One lambda, one expression: 100+ is over, 90+ is a warning, else OK.
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ================================================================== OUTPUT
# 3. Show the whole table so we can eyeball percent and status.
print(df)

# Only show the rows that aren't "OK" — i.e. ones that need attention.
# Boolean filter on the status column, no loops.
not_ok = df[df["status"] != "OK"]
print("\nRows that are NOT OK:")
print(not_ok)


# ==========================================================================s