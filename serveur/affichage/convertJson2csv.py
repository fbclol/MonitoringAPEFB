#!/usr/bin/python3
# coding: utf-8

import csv
import json

# ouvrir le fichier en fonction du nom du hostname
data_file = open('../stockage_collection/bdd/9bf6d4adc10f.json')
data = json.load(data_file)


f = csv.writer(open("../stockage_collection/bdd/9bf6d4adc10f.dat", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["date"  "nombre_user_connecte"])

for data in data:
    f.writerow([data["date"]+";"+data["nombre_user_connecte"]])
