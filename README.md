# MonitoringAPEFB
## projet CERI - Monitoring

par Pierre-Emmanuel Angoulvant et Franck Boué

#### step 0
récupérer le projet par le dépot de l'université ou sur github
[git clone MonitoringAPEFB](https://github.com/fbclol/MonitoringAPEFB)

si nécessaire pour donner les droits d'executions au script :
```bash
chmod +x ./programs.xx
```

### partie collecteur :
#### step 1 - install for dépendence
```bash
cd ./MonitoringAPEFB/client_collecteur
./setup.sh
```
le setup.sh contient toutes les librairies et paquets


#### step 2 - cron / automatisation
```bash
cd ./MonitoringAPEFB/client_collecteur/collecteur
./cron.sh
```
le `cron.sh` permet de executer :
- (toutes les 5min) Le script `client.sh` (qui inclue 3 collecteurs différents bash,mixe,python) et
Un le script `merge.py` permet de rassembler tous les données en un seul json
et enregistre dans un fichier `collecteur_final.json`

- (chaque redemarrage) Le `communication_client.py` Pour envoyer les infos du collecteur au serveur principal
`communication_client.py` -> ouvre une connection https en SSL avec un certificat qui n'est pas authentifié par un tier + par un user/mot de passe
la route de cette connection est :
`<ip_collecteur>:5000/api/monitoring` qui est envoyé en JSON en GET
Dépendance : flask

#### step 3 - Génération des clés pour le https
```bash
cd ./MonitoringAPEFB/client_collecteur/communication
./generate_key.sh
```


### partie serveur principal :
#### step 1 - install for dépendence
```bash
cd ./MonitoringAPEFB/serveur
./setup.sh
```
le `setup.sh` contient toutes les librairies et paquets

#### step 2 - cron / automatisation
```bash
cd ./MonitoringAPEFB/serveur/stockage_collection
./cron.sh
```
le `cron.sh` permet de executer :

- (toutes les 5min) Le script `communication_serveur.sh` permet de récupérer les infos de chaque fichier du collecteur ()utilisation de curl et jq).
 Aprés avoir récupéré les dernières infos d'un collecteur, le script exécute `module_alerte_date.py` se trouvant dans le dossier `affichage`
 permet de nous alerter en cas de situation de crise:
    - pas de signe de vie (+30min)
    - disque dur capacité utilisé en %
    - ram disponible en %
    - utilisation cpu en %

- (tout les jours) Le script `parseur.py` parseur web permet de récupérer les dernières infos du site [cert.ssi.gouv](http://www.cert.ssi.gouv.fr/)
Il est prévu pour récupérer l'alerte la plus récente ainsi que les autres de la liste qui n'ont pas été ajouté dans le json `parseur.json`.
Dépendance : bsp4 beautifulsoup (pour parser le html)

- (tout les jours) Le script `clean_backup_day5.sh` permet de supprimer les archives qui ont plus de 5 jours.

#### step 3 - ajouter un client collecteur
```bash
cd ./serveur/communication
```
Add line in your file `collecteur_hosts.conf`:
```bash
collecteur_hosts[n]="xxx.xxx.x.x"
```

#### step 4 - sauvegarde & restauration

```bash
cd ./serveur/stockage_collection
```

- script `sauvegarde.sh` : permet de sauvegarder à l'instant T la base de donées + le parseur dans une archive
- script `restoration.sh` : permet de restorer la base de données + le parseur


#### step 5 - affichage graphique
```bash
cd ./serveur/affichage
./interaction.sh
```

executer `interaction.sh` : permet affichage en console de graphique.
on demande de charger un serveur parmi la liste proposé pour pouvoir afficher par la suite des graphiques
d'un graph sur l'historique des infos demandés + une phrase sur la dernière info reçu.
dépendance : gnuplot (pour les graph en console)

#### step 6 - modification pour l'envoie des mails

```bash
cd ./serveur/affichage
```
Change de destinateur et d'émetteur modified line 32,33 in your file `module_alerte_date.py`:
```python
fromaddr = "franck.boue@alumni.univ-avignon.fr"
toaddr = "franck.boue@alumni.univ-avignon.fr"
```

for config send mail modified line 60 in your file `module_alerte_date.py`:
```python
server.login(fromaddr, "XXXXXXXXXX")
```
si vous voulez changer de serveur de mail :
modified line 56 in your file `module_alerte_date.py`:
```python
server = smtplib.SMTP_SSL('smtpz.univ-avignon.fr', 465)
```




#### bonus :
- Bdd sans serveur : json
- Les deux scripts pour le collecteur peuvent etre installés sur des serveurs sans avoir à toucher la partie du code :
pour cela un fichier collecteur_hosts.conf est placé sur le sereur principal --> chaque ligne du tableau correspond aux ip des collecteurs. Pour en ajouter un ip faut ajouter une ligne du tableau.
- Template mail permettant de gérer les différents cas de la situation de crise de collecteur (module_alerte_date.py)
- Envoie de mail depuis le serveur de université
- HTTPS

