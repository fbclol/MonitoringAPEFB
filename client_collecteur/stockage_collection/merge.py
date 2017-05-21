#!/usr/bin/python3
# coding: utf-8

import json

# open 3 file
data_file1 = open('./../collecteur/log/collecteur_bash.json')
data_bash = json.load(data_file1)

data_file2 = open('./../collecteur/log/collecteur_mixe.json')
data_mixe = json.load(data_file2)

data_file3 = open('./../collecteur/log/collecteur_python.json')
data_python = json.load(data_file3)


# merge json bash with json python
i = 0
while i < len(data_bash):
    if data_bash[i]["hostname"] == data_python[i]["hostname"]:
        data_bash[i]["cpu_usage"] = data_python[i]["cpu_usage"]
        with open('./../stockage_collection/collecteur_final.json', 'w',
                  encoding='utf-8') as f:
            json.dump(data_bash, f, indent=4)
    i += 1

# merge json bash with json mixe
i = 0
while i < len(data_bash):
    if data_bash[i]["hostname"] == data_mixe[i]["hostname"]:
        data_bash[i]["task_total"] = data_mixe[i]["task_total"]
        data_bash[i]["task_running"] = data_mixe[i]["task_running"]
        data_bash[i]["task_sleeping"] = data_mixe[i]["task_sleeping"]
        data_bash[i]["task_stopped"] = data_mixe[i]["task_stopped"]
        data_bash[i]["task_zombie"] = data_mixe[i]["task_zombie"]
        data_bash[i]["name_processor"] = data_mixe[i]["name_processor"]
        data_bash[i]["nbr_core"] = data_mixe[i]["nbr_core"]
        data_bash[i]["total_memory"] = data_mixe[i]["total_memory"]
        data_bash[i]["memory_available"] = data_mixe[i]["memory_available"]
        data_bash[i]["list_disks"] = data_mixe[i]["list_disks"]
        with open('./../stockage_collection/collecteur_final.json', 'w',
                  encoding='utf-8') as f:
            json.dump(data_bash, f, indent=4)
    i += 1
