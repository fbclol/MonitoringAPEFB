#!/usr/bin/env python3
# coding: utf-8

import os
#os.system("apt-get install -y gcc python3-dev python3-pip python3-psutil")
import psutil
import socket
import datetime
import json
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d-%H:%M:%S")

##################################################################
###### ------       collecteur python, Collecteur.sh       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

os.system("mkdir -p ./log")
mon_fichier = open('./log/collecteur_python.json', 'w')
mon_fichier.write("[{\n")

#print psutil.users()

#---------------------------------------- hostname ---
hostname = socket.gethostname()
print("hostname:", hostname)
mon_fichier.write('"hostname":"' + hostname + '",\n')

#---------------------------------------- hostname ---
print("date:", now)
mon_fichier.write('"date":"' + now + '",\n')

#---------------------------------------- utilization cpu ---
print("utilization cpu:", psutil.cpu_percent())
mon_fichier.write('"utilization_cpu":"'+str(psutil.cpu_percent())+'"\n')

#---------------------------------------- nbr cpu ---
#print("number cpu:", psutil.cpu_percent())
#mon_fichier.write('"number_cpu":"'+str(psutil.cpu_count())+'"\n')

#---------------------------------------- freq cpu---

#print "frequence cpu:", psutil.cpu_freq()
#mon_fichier.write('"frequence_cpu":"'+str(psutil.cpu_freq())+'"\n')

mon_fichier.write("}]")
print("----------")

mon_fichier.close()
