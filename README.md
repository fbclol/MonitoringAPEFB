# MonitoringAPEFB
projet CERI


Monitoring

partie collecteur :

install for dépendence 
setup.sh

mettre le cron tab  : (toute les 5 min)
#*/5 * * * * root /home/monitoring/client.sh

client.sh (execute 3 collecteur différent bash,mixe,python)  
un fichier merge.py permet de rassembler tout les données en un seul json
qui renregistre dans un fichier collecteur_final.json

pour envoyer les infos du collecteur au serveur principal
communication_client.py qui ouvre une connection http(s) protégé par un user/mot de passe + (TLS pas encore)
la route de cette connection est : <ip_collecteur>:5000/api/monitoring qui est envoyé en JSON en GET


#######################


partie serveur principal :

install for dépendence
setup.sh

