#!/usr/bin/env python3
# coding: utf-8

import os
import psutil
import socket
import datetime
import json

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d-%H:%M:%S")

##################################################################
###### ----- collecteur  Collecteur_python.py    ----- ###########
###### version : 1                                     ###########
###### date : 02/05/2017                               ###########
###### realized by : Franck & Pierre-E                 ###########
##################################################################

os.system("mkdir -p ./log")
mon_fichier = open('./log/collecteur_python.json', 'w')
mon_fichier.write("[{\n")

#---------------------------------------- hostname ---
hostname = socket.gethostname()
print("hostname:", hostname)
mon_fichier.write('"hostname":"' + hostname + '",\n')

#---------------------------------------- date ---
print("date:", now)
mon_fichier.write('"date":"' + now + '",\n')

#---------------------------------------- CPU Usage ---
print("CPU Usage :", psutil.cpu_percent())
mon_fichier.write('"cpu_usage":"'+str(psutil.cpu_percent())+'"\n')

mon_fichier.write("}]")
print("----------")

mon_fichier.close()
