#!/usr/bin/env python
# coding: utf-8


##################################################################
###### ------       client client.py       ------ ###########
###### version : 0.1                                   ###########
###### date : 30/04/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################


import socket

#hostnameSRV = "172.17.0.2"
hostnameSRV ="10.120.13.189"
port = 1111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostnameSRV, port))

print("Le nom du fichier prendre sur le client:")

s.send(socket.gethostname())

nom_ficher = s.recv(2048)
print("Ouverture du fichier: ", nom_ficher, "...")
fp = open(nom_ficher, 'rb')
s.send(fp.read())
s.close()
