#!/bin/bash

#--- 	Il est recommandé d'installer la librairie sqlite pour pouvoir stocker les données depuis
#---	le parsing du site CERT-FR, utiliser la commande : sudo apt-get install sqlite


#----- Création de la base de donnée de sqlite ---
sqlite STORAGE
sqlite STORAGE "CREATE TABLE Stock(
			id INTEGER NOT NULL PRIMARY KEY,
			name_alert CHAR(50),
			hist DATE
		);"

#----- Utilisation de curl -s pour parser le site CERT-FR
site=www.cert.ssi.gouv.fr

``curl -s $site | sed -rn '' 
