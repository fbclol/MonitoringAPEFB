#!/bin/sh

##################################################################
###### ------       collecteur bash Collecteur.sh       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

pathlog=/var/run/log/collecteurMonitoring
`mkdir -p $pathlog`
filelog="/var/run/log/collecteurMonitoring/collecteur_bash.json"
#`touch $filelog`


HOSTNAME=`hostname`
NOMPROCESSEUR=`lscpu | sed -n 12p | sed s/'Model name:'/''/g | tr -s ' ' ' '`
ARCHITECTURE=`lscpu | sed -n 1p | tr -d 'Architecture: '`
NBREDECORE=`lscpu | sed -n 4p | tr -d 'CPU(s): '`
DISQUES=`df -h | grep "dev/sd"`
RAMTOTAL=`cat /proc/meminfo | sed -n 1p | tr -d 'MemTotal: ' | tr -d 'kB'`
RAMDISPONIBLE=`cat /proc/meminfo | sed -n 3p | tr -d 'MemAvailabe: ' | tr -d 'kB'`
OS_VERSION=`cat /etc/issue | grep -o "^[^\]*"`
PROGRAMME=`top -bn1 | grep 'Tasks:'`
UTILISATIONCPU=`top -bn1 | grep '%Cpu'`
NBREUSER=`top -bn1 | grep 'top -' | cut -d, -f2 | tr -s 'users ' ' '`
USERS=`who | awk -F "[ (:0)]" '{printf "%-10s%17s\n", $1, $(NF-1)}' | uniq` # sur docker sort rien...
DUREEORDINATEUR=`uptime |  awk '{print $3}' | tr -d ','`
IPLOCAL=`hostname -i`
IPPUBLIC=`wget -qO - icanhazip.com`

echo "#####################################################"
echo "######## EXTRACTION D'INFORMATION principal DU SYSTEME ########"
echo "#####################################################"
echo ""
	echo "nom de la machine : $HOSTNAME"
	echo "ipv4 local : $IPLOCAL"
	echo "ipv4 public : $IPPUBLIC"
	echo "---------------------- CPU ---------------------"
	echo " nom du processeur : $NOMPROCESSEUR"
	echo " nombre de core : $NBREDECORE"
	echo " architechture : $ARCHITECTURE"
	echo " Utilisation du CPU : $UTILISATIONCPU"
	echo ""
	echo "---------------------- RAM ---------------------"
	echo "Ram total : $RAMTOTAL kB"
	echo "Ram disponible : $RAMDISPONIBLE kB"
	echo ""
	echo "---------------------- DISQUES ---------------------"
	echo "$DISQUES"
	echo ""
	echo "---------------------- OS & VERSION ----------------------"
	echo "$OS_VERSION"
	echo ""
	echo "---------------------- autre info ----------------------"
	echo "Liste des utilisateurs connecté : $USERS"
	echo "nombre d'utilisateur connecté : $NBREUSER"
	echo "Durée de fonctionement du serveur : $DUREEORDINATEUR"
	echo "Tache en cours : $PROGRAMME"
	echo ""

 echo -n	'{
  "hostname":"'$HOSTNAME'",
  "ip_local": "''",
  "ip_public": "''",
  "nom_processeur": "'$NOMPROCESSEUR'",
  "architechture": "'$ARCHITECTURE'",
  "nbre_core": "'$NBREDECORE'",
  "nombre_user_connecte": "'$NBREUSER'",
  "user_connecte": "'$USERS'",
  "disque": "'$DISQUES'",
  "ram_occuper": "'$RAMTOTAL'",
  "ram_dispo": "'$RAMDISPONIBLE'",
  "os_version": "'$OS_VERSION'",
  "tache": "'$PROGRAMME'"
  "utilisation_cpu": "'$UTILISATIONCPU'"
} ' > $filelog
	
exit 0