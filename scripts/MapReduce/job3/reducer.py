#!/usr/bin/env python3

import sys

def save_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return float(0)


cars_dictionary = {}

for line in sys.stdin:
    parts = line.strip().split("\t")
    horsepower, engine_displacement = parts[0].split('/',1)
    horsepower = float(horsepower)
    engine_displacement = float(engine_displacement)

    if parts[0] not in cars_dictionary:
        counter = 0
        for key in cars_dictionary.keys():
            key_hp, key_ed = key.split('/',1)
            key_hp = float(key_hp)
            key_ed = float(key_ed)
            if key_hp <= (horsepower * 1.1) and key_hp >= (horsepower * 0.9) and horsepower <= (key_hp * 1.1) and horsepower >= (key_hp * 0.9) and key_ed <= (engine_displacement * 1.1) and key_ed >= (engine_displacement * 0.9) and engine_displacement <= (key_ed * 1.1) and engine_displacement >= (key_ed * 0.9):
                cars_dictionary[key].append(parts[1])
                break
            counter += 1
        if counter == len(cars_dictionary):
            cars_dictionary[parts[0]] = []
            cars_dictionary[parts[0]].append(parts[1])
    else:
        cars_dictionary[parts[0]].append(parts[1])

for key in cars_dictionary.keys():
    horsepower, engine_displacement = key.split('/',1)
    horsepower = float(horsepower)
    engine_displacement = float(engine_displacement)
    price_list = []
    power_dictionary = {}
    for stringa in cars_dictionary.get(key):
        parti = stringa.split("/")
        power = parti[0]
        make_name = parti[1]
        model_name = parti[2]
        price = parti[3]
        price = save_float(price)
        price_list.append(price)
        power_dictionary[power] = [make_name, model_name]
    avg_price = sum(price_list)/len(price_list)
    max_power = max(list(power_dictionary.keys()))
    name_max_power = power_dictionary.get(max_power)
    max_make_name = name_max_power[0]
    max_model_name = name_max_power[1]

    print(f"Gruppo HP_ED: {horsepower}_{engine_displacement}, Prezzo Medio: {avg_price:.1f}, Modello con maggiore potenza: {max_make_name},{max_model_name} => {max_power}")