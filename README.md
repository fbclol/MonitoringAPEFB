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

un script communication_serveur.sh permet de récupérer les infos de chaque collecteur par fichier
utilisation de curl et jq

aprés avoir récupérer les derniere info d'un collecteur le script  execute module_alterte_date.py
permet de nous alerter en cas de situation de crise
- pas de signe de vie (+30min)
- disque dur
- ram disponible
- cpu

le parseur web (parseur.py) permet de récupérer les derniere info du site http://www.cert.ssi.gouv.fr/
il est prévu pour qu'il récupére aussi bien la 1er de la liste qui est sencé etre l'alerte la plus récente que les alertes dernière alerte qui n'aurait pas été ajouté dans le json (parseur.json)


l'affichage en console de lance via le script interaction.sh
on demande de charger un serveur par mit la liste proposé pour pouvoir afficher par la suite ses graphiques
un graph de l'historique des info demandé + une phrase sur la dernière info récu.







bonus :
- bdd sans serveur : json
- les deux script pour le collecteur peuvent etre installer sur des serveur sans avoir à toucher la partie du code
pour cela un fichier collecteur_hosts.conf est placer sur le sereur principal chaque line du tableau correspond au ip des collecteurs pour en ajouter un il faut ajouter une line au tableau.
- template mail permetant de gérer les différent cas de la situation de crise de collecteur (module_alerte_date.py)

