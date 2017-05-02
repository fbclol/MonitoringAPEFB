#!/bin/sh

##################################################################
###### ------ INSTALL du serveur centralisateur ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

# require ficher(s) : [serveurMonitoring.py,init-d-script-monitoring]

#cp -r /etc/init/ /etc/init.save$(date +%Y%m%d)

# chemin de base du projet pour la partie Collecteur
pathProject="/home/tmp/tp_bash/projet/MonitoringAPEFB/Collecteur"
chmod +x $pathProject/serveurMonitoring.py

cd /usr/sbin/
ln -s $pathProject/serveurMonitoring ./serveurMonitoring.py

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