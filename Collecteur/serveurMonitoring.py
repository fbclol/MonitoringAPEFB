#!/usr/bin/env python
# coding: utf-8 




##################################################################
###### ------       serveur monitoring.py       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################


# pour franck  --> 9bf6d4adc10f client

import socket
import threading
import os
import datetime

today = datetime.datetime.now()
today = today.strftime("%Y-%m-%d-%H-%M")

basePathSrv="/home/tmp/tp_bash/projet/MonitoringAPEFB/Collecteur/log/"
os.system("mkdir -p /home/tmp/tp_bash/projet/MonitoringAPEFB/Collecteur/log/")

print "ip du serveur :"+socket.gethostbyname(socket.gethostname())
# si ne marche pas ouvir le port 1111
#iptables -A INPUT -p tcp -i eth0 --dport 1111 -j ACCEPT

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):
	
		localname= self.clientsocket.recv(255)
		filename="/var/run/log/collecteurMonitoring/collecteur_bash.txt"
		
		self.clientsocket.send(filename)
		r = self.clientsocket.recv(9999999)
		print("récupération du fichier "+os.path.basename(filename)+" sur "+localname)
		with open(basePathSrv+today+"_"+localname+"_"+os.path.basename(filename),'wb') as _file:
			_file.write(r)
		print("enregistrement fait : " +basePathSrv+today+"_"+localname+"_"+os.path.basename(filename))
			
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()