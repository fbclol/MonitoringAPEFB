#!/bin/bash



##################################################################
###### ------       collecteur bash Collecteur.sh       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################
pathlog=/var/run/log/collecteurMonitoring
`mkdir -p $pathlog`
filelog=/var/run/log/collecteurMonitoring/collecteur_bash.txt
`touch $filelog`


NOMPROCESSEUR=`lscpu | sed -n 12p`
ARCHITECTURE=`lscpu | sed -n 1p | tr -d 'Architecture: '`
NBREDECORE=`lscpu | sed -n 4p | tr -d 'CPU(s): '`
NOMPROCESSEUR=`lscpu | sed -n 1p`
GRAPHIC_CARD=`lspci | grep VGA` # sur docker sort rien...
DISQUES=`df -k | grep "dev/sd"`
#RAM=`free -m`

#RAMTOTAL=`cat /proc/meminfo | sed -n 1p`
RAMTOTAL=`cat /proc/meminfo | sed -n 1p | tr -d 'MemTotal: ' | tr -d 'kB'`
#RAMDISPONIBLE=`cat /proc/meminfo | sed -n 3p`
RAMDISPONIBLE=`cat /proc/meminfo | sed -n 3p | tr -d 'MemAvailabe: ' | tr -d 'kB'`
#PROCESS= ``
OS_VERSION=`cat /etc/issue | sed s/' \\n \\l'/''/g`
USERS=`who` # sur docker sort rien...
#who | awk -F "[ (:0)]" '{printf "%-10s%17s\n", $1, $(NF-1)}' | uniq

# trouver des lien symbolique en erreur
#find / -type l | perl -lne 'print if ! -e'

###################### EXEMPLe pour l'envoie de mail avec cron tab
# 0 0 * * * clamscan --recursive --log=/var/log/clamav/clamscan.log --quiet /DATA ; mail -s "resultat du scan des virus" email@domaine.fr < /var/log/clamav/clamscan.log
#


#en test
# Permet de voir d'un seul coup d'oeil si la machine est vraiment surchargée
#w

# Affiche avec une entête des informations (nom de login, console ... ) sur les utilisateurs connectés.
#who -H

# Permet de connaitre la date (   la date, l'heure et le décalage horaire)
#date

#  Durée de fonctionnement de l'ordinateur
#uptime

#  Charge est un indice de l'activité de l'ordinateur. Il y a trois valeurs pour 1 min , 5min et 15min
#tload

# Affiche au format humain l'espace total, occupé, libre sur tous les disques.
#df -ah
# Affiche des informations sur la mémoire (totale, libre, swap ...).
#free ou cat /proc/meminfo

# Affiche les statistiques sur la mémoire virtuelle.
#vmstat

# Affiche la liste des disques montés.
#mount
# Affiche le nom du système d'exploitation.

#unam

# Affiche le type du microprocesseur.

#arch ou uname -m

# affiche des informations sur le microprocesseur (type, fréquence, cache ...)

#cat /proc/cpuinfo


# Affiche diverses informations système (nom du SE, version, microprocesseur ...).

#uname -a


# Certaines variables système :
#echo $OSTYPE
#$BASH
#$BASH_VERSION


#  Permet d'obtenir la liste des processus qui tournent au moment où vous lancez la commande.
#ps

# Permet d'obtenir la liste des processus qui tournent pour un utilisateur donné
#ps -u UTILISATEUR


# Affiche la liste des 12 dernières connexions.
#last -n 12


#
#logname

#
#users

#
#groups
$SOMME = 0
let SOMME = RAMTOTAL / RAMDISPONIBLE * 100

echo "#####################################################"
echo "######## EXTRACTION D'INFORMATION principal DU SYSTEME ########"
echo "#####################################################"
echo ""
echo ""
while true
do
	echo "---------------------- CPU ---------------------"
	echo "$CPU"
	echo ""
	echo "---------------------- RAM ---------------------"
	echo "$RAMTOTAL kB & $RAMDISPONIBLE kB il vous reste $SOMME %"
	echo ""
	echo "---------------------- CARTE GRAPHIQUE ---------------------"
	echo "$GRAPHIC_CARD"
	echo ""
	echo "---------------------- DISQUES ---------------------"
	echo "$DISQUES"
	echo ""
	echo "---------------------- OS & VERSION ----------------------"
	echo "$OS_VERSION"
	echo ""
	echo "---------------------- NBR USERS CONNECTES ----------------------"
	echo "$USERS"
	echo ""

 echo -n	'{
  "hostname" "''"
  "ip_local" "''"
  "ip_public" "''"
  "nombre_user_connecte" "''"
  "user_connecte" "''"
  "carte_graphique" "'$GRAPHIC_CARD'"
  "disque": "'$DISQUES'"
  "ram_occuper": "'$RAMTOTAL'",
  "ram_dispo": "'$RAMDISPONIBLE'"
  "os_version": "'$OS_VERSION'"
  "nom_processeur": "'$NOMPROCESSEUR'"
} ' > $filelog
	
	
	# rep=1 
# while [ "$rep" -eq 1 ]; do 
    # printf "menu (""taper"" help pour plus d'information) :\n\n" 
   
	# echo "faire un choix :"
    # read   choix arg
    # case "$choix" in 
        # 1) 	printf "Version de linux :\n" 
			# echo `uname -a` ;; 
		# 2) 	exo2 $arg ;;		
		# 3) 	exo3 $arg ;;		
		# 4) 	exo4 $arg ;;		
		# 5) 	exo5 ;;		
		# 7) 	exo7 $arg ;;		
		# 8) 	exo8 ;;		
		# 9) 	exo9 $arg ;;		
		# 10) exo10 ;;		
		# 11) exo11 $arg ;;		
		# 12) exo12 $arg ;;
		# help)  echo "1. Version de linux" 
    # echo "2. exo2 with arg" 
    # echo "3. exo3 with arg" 
    # echo "4. exo4 with arg" 
    # echo "5. exo5" 
    # echo "7. exo7 with arg" 
    # echo "8. exo8" 
    # echo "9. exo9 with arg" 
    # echo "10. exo10" 
    # echo "11. exo11" 
    # echo "12. exo12" 
    
    # echo -e "q. To quit\n" ;;
        # q) 
            # echo "Goodbye" 
            # #pause 
            # rep=0 ;; 
        # *) 
            # echo "Input error"
			# exit 101 ;;
            # #pause ;; 
    # esac 
# done

exit 0
	
	
	
done

