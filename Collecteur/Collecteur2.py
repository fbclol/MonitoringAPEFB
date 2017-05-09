#!/usr/bin/env python3
# coding: utf8


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
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d-%H:%M:%S")

os.system("mkdir -p /var/run/log/collecteurMonitoring")
mon_fichier = open('/var/run/log/collecteurMonitoring/collecteur_mixe.json', 'w')
mon_fichier.write("{\n")

<<<<<<< HEAD
	#---------- CPU ----------
	print('---------- CPU ----------')
	os.system("lscpu | sed -n 13p")
	print('\n')
	mon_fichier.write('"CPU":"' + hostname + '",\n')
	

	#---------- RAM ----------
	print('---------- RAM ----------')
	os.system("cat /proc/meminfo | sed -n 1p")
	print('\n')

	#---------- CARTE GRAPHIQUE ----------
	print('---------- CARTE GRAPHIQUE ----------')
	os.system("lspci | grep VGA")
	print('\n')

	#---------- DISQUES ----------
	print('---------- DISQUES ----------')
	os.system("df -h")
	print('\n')

	#---------- OS & VERSION ----------
	print('---------- OS & VERSION ----------')
	os.system("cat /etc/issue")
	print('\n')

	#---------- USERS CONNECTES ----------
	print('---------- NBR USERS CONNECTES ----------')
	os.system("who")
	print('\n')

=======
>>>>>>> a3b9cd429557898be5e6f894774c4aee1162b63b

print('---------- Tag ----------')
args = ["hostname"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Nom du processeur:",out[0].decode("utf-8")) 
print('\n')
mon_fichier.write('"hostname":"' + str(out[0].decode("utf-8") ) + '",\n')	

print("Date :",now)
mon_fichier.write('"date":"' + now + '",\n')
#---------- CPU ----------
print('---------- CPU ----------')
args = ["lscpu | sed -n 12p | sed s/'Model name:'/''/g | tr -s ' ' ' '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Nom processeur:",out[0].decode("utf-8")) 
print('\n')
mon_fichier.write('"nom_processeur":"' + str(out[0].decode("utf-8") ) + '",\n')	

args = ["lscpu | sed -n 4p | tr -d 'CPU(s): '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Nbre de core:",out[0].decode("utf-8") ) 
print('\n')
mon_fichier.write('"nbre_core":"' + str(out[0].decode("utf-8") ) + '",\n')

#---------- RAM ----------
print('---------- RAM ----------')

args = ["cat /proc/meminfo | sed -n 1p | tr -d 'MemTotal: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Memoire total : (en kB)",out[0].decode("utf-8") ) 
print('\n')
mon_fichier.write('"memoire_total":"' + str(out[0].decode("utf-8") ) + '",\n')

args = ["cat /proc/meminfo | sed -n 3p | tr -d 'MemAvailabe: ' | tr -d 'kB'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Memoire disponible : (en kB)",out[0].decode("utf-8") ) 
print('\n')
mon_fichier.write('"memoire_disponible":"' + str(out[0].decode("utf-8") ) + '",\n')

#---------- DISQUES ----------
print('---------- DISQUES ----------')
args = ["df -h | grep 'dev/sd'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Disques",out[0].decode("utf-8") ) 
print('\n')
mon_fichier.write('"disques":"' + str(out[0].decode("utf-8") ) + '",\n')

#---------- OS & VERSION ----------
print('---------- OS & VERSION ----------')
args = ["cat /etc/issue | grep -o '^[^\]*'"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Os version : ",out[0].decode("utf-8") )
print('\n')
mon_fichier.write('"os_version":"' + str(out[0].decode("utf-8") ) + '",\n')

#---------- USERS CONNECTES ----------
print('---------- NBR USERS CONNECTES ----------')
args = ["top -bn1 | grep 'top -' | cut -d, -f2 | tr -s 'users ' ' '"]
proc = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE)
out = proc.communicate()
print("Nombre d'utilisateur(s)",out[0].decode("utf-8") )
print('\n')
mon_fichier.write('"os_version":"' + str(out[0].decode("utf-8") ) + '",\n')

