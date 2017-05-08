#!/usr/bin/env python
# coding: utf-8


import os
os.system("apt-get install -y gcc python-dev python-pip python-psutil")
import psutil
import socket
import json


##################################################################
###### ------       collecteur python, Collecteur.sh       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################


os.system("mkdir -p /var/run/log/collecteurMonitoring")
mon_fichier = open('/var/run/log/collecteurMonitoring/CollecteurPy.json', 'w')
mon_fichier.write("{\n")

#print psutil.users()

#---------------------------------------- hostname ---
hostname = socket.gethostname()
print "hostname:", hostname
mon_fichier.write('"hostname":"' + hostname + '",\n')

#---------------------------------------- utilization cpu ---
print "utilization cpu:", psutil.cpu_percent()
mon_fichier.write('"utilization_cpu":"'+str(psutil.cpu_percent())+'",\n')

#---------------------------------------- nbr cpu ---
print "number cpu:", psutil.cpu_percent()
mon_fichier.write('"number_cpu":"'+str(psutil.cpu_count())+'"\n')

#---------------------------------------- freq cpu---

#print "frequence cpu:", psutil.cpu_freq()
#mon_fichier.write('"frequence_cpu":"'+str(psutil.cpu_freq())+'"\n')

mon_fichier.write("}")
print "----------"

mon_fichier.close()
