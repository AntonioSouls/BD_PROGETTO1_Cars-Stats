#!/usr/bin/env python3

import sys
import csv

table = csv.DictReader(sys.stdin)

for row in table:
    make_name = row['make_name'].strip()
    model_name = row['model_name'].strip()
    year = int(row['year'])
    price = float(row['price'])

    if year > 2025 or year < 1886 or price < 2500.0:
        continue

    key = f"{make_name},{model_name}"
    value = f"{year},{price}"

    print(f"{key}\t{value}")