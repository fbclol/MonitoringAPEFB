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

#now = datetime.datetime.now()
#now = now.strftime("%Y-%m-%d-%H-%M")
#print now

os.system("mkdir -p /home/tmp/projet/monitoring_APEFB/Collecteur")
mon_fichier = open('/home/tmp/projet/monitoring_APEFB/Collecteur/CollecteurMixt.json', 'w')
mon_fichier.write("{\n")

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



