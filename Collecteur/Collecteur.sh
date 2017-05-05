#!/bin/bash



##################################################################
###### ------       collecteur bash Collecteur.sh       ------ ###########
###### version : 0.1                                   ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

pathlog=/var/run/log/collecteurMonitoring
`mkdir -p $pathlog`
filelog=/var/run/log/collecteurMonitoring/collecteur_bash.json
`touch $filelog`

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



echo "#####################################################"
echo "######## EXTRACTION D'INFORMATION principal DU SYSTEME ########"
echo "#####################################################"
echo ""
echo ""
while true
do
	echo "nom de la machine : $HOSTNAME"
	echo "---------------------- CPU ---------------------"
	echo " nom du processeur : $NOMPROCESSEUR"
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
  "hostname":"'$HOSTNAME'",
  "ip_local": "''",
  "ip_public": "''",
  "nom_processeur": "'$NOMPROCESSEUR'",
  "architechture": "'$ARCHITECTURE'",
  "nbre_core": "'$NBREDECORE'",
  "nombre_user_connecte": "''",
  "user_connecte": "''",
  "carte_graphique": "'$GRAPHIC_CARD'",
  "disque": "'$DISQUES'",
  "ram_occuper": "'$RAMTOTAL'",
  "ram_dispo": "'$RAMDISPONIBLE'",
  "os_version": "'$OS_VERSION'",
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

