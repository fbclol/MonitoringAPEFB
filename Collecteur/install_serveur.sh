#!/bin/sh

##################################################################
###### ------ INSTALL du serveur centralisateur ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

# require ficher(s) : [serveurMonitoring.py,init-d-script-monitoring]

# python doit être installé
#apt-get install python

#jq doit etre installé pour le json
#apt-get install jq

# wget pour aller parser le site web
#apt-get install wget

# pour voir la carte graphique
#apt-get install pciutils 

# chemin de base du projet pour la partie Collecteur
pathProject="/home/tmp/tp_bash/projet/MonitoringAPEFB/Collecteur"
chmod +x $pathProject/serveurMonitoring.py

cd /usr/sbin/
ln -s $pathProject/serveurMonitoring.py ./serveurMonitoring

# se rendre dans le rép pour creer un lien symbolique
cd /lib/init/
ln -s $pathProject/init-d-script-monitoring ./init-d-script-monitoring
#chmod +x init-d-script-monitoring

# se rendre dans le rép pour creer un lien symbolique
cd /etc/init.d
ln -s $pathProject/serveurMonitoring ./serveurMonitoring
#chmod +x serveurMonitoring

# rendre le programme.py service / deamon et lancer au demarrage du serveur 
update-rc.d serveurMonitoring defaults 99

echo "ne pas oublier de mettre l'ip du serveur dans le scrip python (client.py)"
echo 'ip :' `hostname -I`
echo 'le service peut ce lancer avec la commande : >> service serveurMonitoring start , il tournera en arriere plan'
echo 'on peut afficher le service en mode verbeux avec la commande : >> serveurMonitoring'
#service serveurMonitoring start