#!/usr/bin/env python3
# coding: utf8

##################################################################
###### ------       collecteur mixe Collecteur2.py       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

import os
import time
import datetime
import subprocess

print('#####################################################')
print("######## EXTRACTION D'INFORMATION DU SYSTEME ########")
print('#####################################################\n')

# avoir la date courante
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d-%H:%M:%S")

os.system("mkdir -p /log")
mon_fichier = open('./log/collecteur_mixe.json', 'w')
mon_fichier.write("[{\n")


print('---------- Tag ----------')
args = ["hostname"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Nom du processeur:",out[0].decode("utf-8")) 
print('\n')
mon_fichier.write('"hostname":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')	

print("Date :",now)
mon_fichier.write('"date":"' + now + '",\n')
#---------- CPU ----------
print('---------- CPU ----------')
args = ["lscpu | sed -n 12p | sed s/'Model name:'/''/g | tr -s ' ' ' '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Nom processeur:",out[0].decode("utf-8")) 
print('\n')
mon_fichier.write('"nom_processeur":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')	

args = ["lscpu | sed -n 4p | tr -d 'CPU(s): '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Nbre de core:",out[0].decode("utf-8") ) 
print('\n')
mon_fichier.write('"nbre_core":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

#---------- RAM ----------
print('---------- RAM ----------')

args = ["cat /proc/meminfo | sed -n 1p | tr -d 'MemTotal: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Memoire total : (en kB)",out[0].decode("utf-8")[:-1]) 

mon_fichier.write('"memoire_total":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["cat /proc/meminfo | sed -n 3p | tr -d 'MemAvailabe: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Memoire disponible : (en kB)",out[0].decode("utf-8") ) 
mon_fichier.write('"memoire_disponible":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

#---------- DISQUES ----------
print('---------- DISQUES ----------')
args = ["df -h | grep 'dev/sd' | tr '\n' ',' "]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Disques",out[0].decode("utf-8")) 

mon_fichier.write('"disques":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

print('---------- TACHES ----------')
args = ["top -bn1 | egrep '(Tasks:|Tâches:)'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Tache :",out[0].decode("utf-8")) 

args = ["top -bn1 | egrep '(Tasks:|Tâches:)' | cut -d, -f1 | tr -d 'Task: total'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"tache_total":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Tâches:)' | cut -d, -f2 | tr -d '(running: |en cours: )'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"tache_running":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Tâches:)' | cut -d, -f3 | tr -d '(sleeping: |en veille: )'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"tache_sleeping":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Tâches:)' | cut -d, -f4 | tr -d '(stopped: |arrêté: )'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"tache_stopped":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')

args = ["top -bn1 | egrep '(Tasks:|Tâches:)' | cut -d, -f5 | tr -d 'zombie '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
mon_fichier.write('"tache_zombie":"' + str(out[0].decode("utf-8")[:-1]) + '"\n,')


#---------- USERS CONNECTES ----------
print('---------- NBR USERS CONNECTES ----------')
args = ["top -bn1 | grep 'top -' | cut -d, -f2 | tr -s -d 'users ' ' '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("nombre user connecte",out[0].decode("utf-8") )

mon_fichier.write('"nombre_user_connecte":"' + str(out[0].decode("utf-8")[:-1]) + '"')
mon_fichier.write("\n}]")
