#import psutil
import os
import time

#Pour compiler le programme python, utiliser la commande 'python <nom du fichier>'

print('#####################################################')
print("######## EXTRACTION D'INFORMATION DU SYSTEME ########")
print('#####################################################\n')

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

