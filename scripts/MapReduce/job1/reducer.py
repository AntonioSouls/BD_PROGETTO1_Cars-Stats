#!/usr/bin/env python3

import sys
from collections import defaultdict

models_dictionary = {}

for line in sys.stdin:
    parts = line.strip().split("\t")

    if  parts[0] not in models_dictionary:
        models_dictionary[parts[0]] = []
    models_dictionary[parts[0]].append(parts[1])

for key in models_dictionary.keys():
    make_name, model_name = key.split(',',1)
    total_cars = len(models_dictionary.get(key))
    years_list = []
    prices_list = []
    for stringa in models_dictionary.get(key):
        year, price = stringa.split(',',1)
        years_list.append(int(year))
        prices_list.append(float(price))
    min_price = min(prices_list)
    max_price = max(prices_list)
    avg_price = sum(prices_list)/len(prices_list)

    years_list = sorted(set(years_list))

    print(f"Marca: {make_name}, Modello: {model_name}, Numero Totale Macchine: {total_cars}, Prezzo Minimo: {min_price}, Prezzo Massimo: {max_price}, Prezzo Medio: {avg_price}, Lista Anni: {years_list}")