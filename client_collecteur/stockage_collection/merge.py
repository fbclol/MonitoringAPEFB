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
        data1[i]["cpu_usage"] = data3[i]["cpu_usage"]
        with open('./collecteur_final.json', 'w',
                  encoding='utf-8') as f:
            json.dump(data1, f, indent=4)
    i += 1

i = 0
while i < len(data1):
    if data1[i]["hostname"] == data2[i]["hostname"]:
        data1[i]["task_total"] = data2[i]["task_total"]
        data1[i]["task_running"] = data2[i]["task_running"]
        data1[i]["task_sleeping"] = data2[i]["task_sleeping"]
        data1[i]["task_stopped"] = data2[i]["task_stopped"]
        data1[i]["task_zombie"] = data2[i]["task_zombie"]
        data1[i]["name_processor"] = data2[i]["name_processor"]
        data1[i]["nbr_core"] = data2[i]["nbr_core"]
        data1[i]["total_memory"] = data2[i]["total_memory"]
        data1[i]["memory_available"] = data2[i]["memory_available"]
        data1[i]["list_disks"] = data2[i]["list_disks"]
        with open('./../stockage_collection/collecteur_final.json', 'w',
                  encoding='utf-8') as f:
            json.dump(data1, f, indent=4)
    i += 1
