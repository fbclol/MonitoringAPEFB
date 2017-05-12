#!/usr/bin/python3
# coding: utf-8

import json

data_file1 = open('./../collecteur/log/collecteur_bash.json')
data1 = json.load(data_file1)

data_file2 = open('./../collecteur/log/collecteur_mixe.json')
data2 = json.load(data_file2)

data_file3 = open('./../collecteur/log/collecteur_python.json')
data3 = json.load(data_file3)

i = 0

while i < len(data1):
    if data1[i]["hostname"] == data3[i]["hostname"]:
        data1[i]["utilization_cpu"] = data3[i]["utilization_cpu"]
        with open('./collecteur_final.json', 'w',
                  encoding='utf-8') as f:
            json.dump(data1, f, indent=4)
    i += 1

i = 0
while i < len(data1):
    if data1[i]["hostname"] == data2[i]["hostname"]:
        data1[i]["tache_total"] = data2[i]["tache_total"]
        data1[i]["tache_running"] = data2[i]["tache_running"]
        data1[i]["tache_sleeping"] = data2[i]["tache_sleeping"]
        data1[i]["tache_stopped"] = data2[i]["tache_stopped"]
        data1[i]["tache_zombie"] = data2[i]["tache_zombie"]
        with open('./collecteur_final.json', 'w',
                  encoding='utf-8') as f:
            json.dump(data1, f, indent=4)
    i += 1
