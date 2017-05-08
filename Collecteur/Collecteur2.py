#!/usr/bin/env python
# coding: utf-8


##################################################################
###### ------       collecteur mixe Collecteur2.py       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

#import psutil
import os
import time
print('#####################################################')
print("######## EXTRACTION D'INFORMATION DU SYSTEME ########")
print('#####################################################\n')

import datetime
import subprocess
#now = datetime.datetime.now()
#now = now.strftime("%Y-%m-%d-%H-%M")
#print now

os.system("mkdir -p /var/run/log/collecteurMonitoring")
mon_fichier = open('/var/run/log/collecteurMonitoring/collecteur_mixe.json', 'w')
mon_fichier.write("{\n")




#---------- CPU ----------
print('---------- CPU ----------')
args = ["lscpu | sed -n 12p | sed s/'Model name:'/''/g | tr -s ' ' ' '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print "Nom processeur:",out[0] 
print('\n')
mon_fichier.write('"nom_processeur":"' + out[0] + '",\n')	

args = ["lscpu | sed -n 4p | tr -d 'CPU(s): '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print "Nbre de core:",out[0] 
print('\n')
mon_fichier.write('"nbre_core":"' + out[0] + '",\n')

#---------- RAM ----------
print('---------- RAM ----------')

args = ["cat /proc/meminfo | sed -n 1p | tr -d 'MemTotal: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print "Memoire total : (en kB)",out[0] 
print('\n')
mon_fichier.write('"memoire_total":"' + out[0] + '",\n')

args = ["cat /proc/meminfo | sed -n 3p | tr -d 'MemAvailabe: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print "Memoire disponible : (en kB)",out[0] 
print('\n')
mon_fichier.write('"memoire_disponible":"' + out[0] + '",\n')

#---------- DISQUES ----------
print('---------- DISQUES ----------')
args = ["df -h | grep 'dev/sd'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print "Disques",out[0] 
print('\n')
mon_fichier.write('"disques":"' + out[0] + '",\n')

#---------- OS & VERSION ----------
print('---------- OS & VERSION ----------')
args = ["cat /etc/issue | grep -o '^[^\]*'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print "Os version : ",out[0] 
print('\n')
mon_fichier.write('"os_version":"' + out[0] + '",\n')

#---------- USERS CONNECTES ----------
print('---------- NBR USERS CONNECTES ----------')
args = ["top -bn1 | grep 'top -' | cut -d, -f2 | tr -s 'users ' ' '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print "Nombre d'utilisateur(s)",out[0] 
print('\n')
mon_fichier.write('"os_version":"' + out[0] + '",\n')

