#!/usr/bin/python3
# coding: utf-8

import csv
import json
import sys

# open the file based on the name of the hostname
if len(sys.argv) > 1:
    data_file = open('../stockage_collection/bdd/' + sys.argv[1] + '.json')
    data = json.load(data_file)

    f = csv.writer(open('../stockage_collection/bdd/stat.dat', "w"))

    # Write CSV Header
    f.writerow(["date;nbr_users_logged;total_memory;memory_available;task_total;task_running;"
                "task_zombie;task_stopped;task_sleeping;disk_capacity_used;cpu_usage;computer_duration"])

    # one line  column delimiter ;
    for data in data:
        f.writerow([
            data["date"] + ";" +
            data["nbr_users_logged"] + ";" +
            data["total_memory"] + ";" +
            data["memory_available"] + ";" +
            data["task_total"] + ";" +
            data["task_running"] + ";" +
            data["task_zombie"] + ";" +
            data["task_stopped"] + ";" +
            data["task_sleeping"] + ";" +
            data["disk_capacity_used"] + ";" +
            data["cpu_usage"] + ";" +
            data["computer_duration"]
        ]
        )
else:
    print("Missing an argument")
