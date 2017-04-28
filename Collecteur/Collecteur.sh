#!/bin/bash

CPU=`lscpu | sed -n 13p`
GRAPHIC_CARD=`lspci | grep VGA`
DISQUES=`df -h`
#RAM=`free -m`
RAM=`cat /proc/meminfo | sed -n 1p`
#PROCESS= ``
OS_VERSION=`cat /etc/issue`
USERS=`who`
#who | awk -F "[ (:0)]" '{printf "%-10s%17s\n", $1, $(NF-1)}' | uniq




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
	echo "$RAM"
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

	
	
	
	rep=1 
while [ "$rep" -eq 1 ]; do 
    printf "menu (""taper"" help pour plus d'information) :\n\n" 
   
	echo "Make a choice :"
    read   choix arg
    case "$choix" in 
        1) 	printf "Version de linux :\n" 
			echo `uname -a` ;; 
		2) 	exo2 $arg ;;		
		3) 	exo3 $arg ;;		
		4) 	exo4 $arg ;;		
		5) 	exo5 ;;		
		7) 	exo7 $arg ;;		
		8) 	exo8 ;;		
		9) 	exo9 $arg ;;		
		10) exo10 ;;		
		11) exo11 $arg ;;		
		12) exo12 $arg ;;
		help)  echo "1. Version de linux" 
    echo "2. exo2 with arg" 
    echo "3. exo3 with arg" 
    echo "4. exo4 with arg" 
    echo "5. exo5" 
    echo "7. exo7 with arg" 
    echo "8. exo8" 
    echo "9. exo9 with arg" 
    echo "10. exo10" 
    echo "11. exo11" 
    echo "12. exo12" 
    
    echo -e "q. To quit\n" ;;
        q) 
            echo "Goodbye" 
            #pause 
            rep=0 ;; 
        *) 
            echo "Input error"
			exit 101 ;;
            #pause ;; 
    esac 
done

exit 0
	
	
	
done

