#!/usr/bin/env python3
# coding: utf8

##################################################################
###### ---  collecteur mixe Collecteur_mixe.py    ---- ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### realized by : Franck & Pierre-E                 ###########
##################################################################

import os
import time
import datetime
import subprocess

print('#####################################################')
print("######## SYSTEM INFORMATION EXTRACTION ########")
print('#####################################################\n')

# Have the current date
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d-%H:%M:%S")

os.system("mkdir -p ./log")
mon_fichier = open('./log/collecteur_mixe.json', 'w')
mon_fichier.write("[{\n")


print('---------- Tag ----------')
args = ["hostname"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Computer name :",out[0].decode("utf-8")) 
print('\n')
mon_fichier.write('"hostname":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')	

print("Date :",now)
mon_fichier.write('"date":"' + now + '",\n')

#---------- CPU ----------
print('---------- CPU ----------')
args = ["lscpu | sed -n 12p | sed s/'Model name:'/''/g | tr -s ' ' ' '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Name processor : ",out[0].decode("utf-8")) 
print('\n')
mon_fichier.write('"name_processor":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')	

args = ["lscpu | sed -n 4p | tr -d 'CPU(s): '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Number core:",out[0].decode("utf-8") ) 
print('\n')
mon_fichier.write('"nbr_core":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

#---------- RAM ----------
print('---------- RAM ----------')

args = ["cat /proc/meminfo | sed -n 1p | tr -d 'MemTotal: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Total memory : (in kB)",out[0].decode("utf-8")[:-1]) 

mon_fichier.write('"total_memory":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["cat /proc/meminfo | sed -n 3p | tr -d 'MemAvailabe: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Memory available : (in kB)",out[0].decode("utf-8") ) 
mon_fichier.write('"memory_available":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

#---------- Disks ----------
print('---------- Disks ----------')
args = ["df -h | grep 'dev/sd' | tr '\n' ',' "]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Disks",out[0].decode("utf-8")) 

mon_fichier.write('"list_disks":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

print('---------- tasks ----------')
args = ["top -bn1 | egrep '(Tasks:|Taches:)'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Tasks :",out[0].decode("utf-8")) 

args = ["top -bn1 | egrep '(Tasks:|Taches:)' | cut -d, -f1 | tr -d 'Task: total'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"task_total":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Taches:)' | cut -d, -f2 | tr -d '(running: |en cours: )'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"task_running":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Taches:)' | cut -d, -f3 | tr -d '(sleeping: |en veille: )'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"task_sleeping":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Taches:)' | cut -d, -f4 | tr -d '(stopped: |arrêté: )'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"task_stopped":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Taches:)' | cut -d, -f5 | tr -d 'zombie '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"task_zombie":"' + str(out[0].decode("utf-8")[:-1]) + '"\n')

mon_fichier.write("\n}]")
