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

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d-%H-%M")
print now

while True:

	#---------- CPU ----------
	print('---------- CPU ----------')
	os.system("lscpu | sed -n 13p")
	print('\n')

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




	time.sleep(120)		#delai de 2 min

