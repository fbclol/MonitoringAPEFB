#!/usr/bin/env python
# coding: utf-8
import psutil
import os
import socket
import json


##################################################################
###### ------       collecteur python, Collecteur.sh       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################


#path = "/home/tmp/projet"  # drwxr-xr-x
os.system("mkdir -p /home/tmp/projet/monitoring_APEFB/Collecteur")

#print(path)

mon_fichier = open('/home/tmp/projet/monitoring_APEFB/Collecteur/CollecteurPy.json', 'w')

mon_fichier.write("{\n")

#print psutil.users()


#---------------------------------------- hostname ---
hostname = socket.gethostname()
print "hostname:", hostname
mon_fichier.write('"hostname":"' + hostname + '",\n')

#---------------------------------------- utilization cpu ---
print "utilization cpu:", psutil.cpu_percent()
mon_fichier.write('"utilization cpu":"'+str(psutil.cpu_percent())+'",\n')


#---------------------------------------- nbr cpu ---
print "number cpu:", psutil.cpu_percent()
mon_fichier.write('"number cpu":"'+str(psutil.cpu_count())+'",\n')

#---------------------------------------- freq cpu---
freq ='%(number)06d' % \
        {"language": "Python", "number": psutil.cpu_freq().current}
print "frequence cpu:", freq
mon_fichier.write('"frequence cpu":"'+str(freq)+'"\n')

print psutil.users()

mon_fichier.write("}")

mon_fichier.close()
