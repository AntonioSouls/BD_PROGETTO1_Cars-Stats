#!/usr/bin/env python3

import sys
import csv

def save_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return " "

table = csv.DictReader(sys.stdin)

for row in table:
    horsepower = save_float(row.get('horsepower'))
    engine_displacement = save_float(row.get('engine_displacement'))
    if horsepower == " " or engine_displacement == " ":
        continue

    power = (row.get('power') or " ").strip()
    make_name = (row.get('make_name') or " ").strip()
    model_name = (row.get('model_name') or " ").strip()
    price = save_float(row.get('price'))

    key = f"{horsepower}/{engine_displacement}"
    value = f"{power}/{make_name}/{model_name}/{price}"

    print(f"{key}\t{value}")
