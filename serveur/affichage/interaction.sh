#! /bin/bash

rep=1 
while [ "$rep" -eq 1 ]; do 
    printf "menu :\n\n" 
	echo "1. Afficher la liste des serveurs du réseau" 
    echo "2. Charger les données d'un serveur" 
    echo "3. Affichage graphique du nombre d'utilisateur" 
    echo "4. Affichage graphique de l'occupation du disque" 
    echo "5. Affichage graphique de l'utisation de la ram"
    echo "7. Affichage graphique du statut des taches" 
    echo -e "q. To quit\n"
	echo "Make a choice :"
    read   choix arg
    case "$choix" in 
        1) 	gnuplot gnuplot/nbre_user_5day.gnu ;; 
		2) 	./convertJson2csv.py ;;		
		3) 	gnuplot gnuplot/nbre_user_5day.gnu ;;		
		4) 	exo4 $arg ;;		
		5) 	exo5 ;;		
		7) 	exo7 $arg ;;	
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