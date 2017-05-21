#! /bin/bash

function choice_server() {
	i=0
	for line in `find ./../stockage_collection/bdd/ -type f -name "*.json"`
		do
			((i+=1))
			fullfilename=$(basename $line)
			filename=${fullfilename%.*}
			echo "$i. $filename"
			arr[$i]="$filename"
		done 
		echo "Make a choice for server loading :"
		read num_host
		echo ${arr[$num_host]}
		
		./convertJson2csv.py ${arr[$num_host]}
}

function graph_nbre_user_logged () {

	if [[ "${arr[$num_host]}" == "" ]]
	then
		choice_server
	fi
	gnuplot gnuplot/nbr_users_5day.gnu
	nbr_users_logged=`cat ./../stockage_collection/bdd/${arr[$num_host]}.json | jq -r '.[0].nbr_users_logged'`
	echo "Less than 5 min ago the server ${arr[$num_host]} has $nbr_users_logged user logged on."
}

function graph_disk_capacity_used () {

	if [[ "${arr[$num_host]}" == "" ]]
	then
		choice_server
	fi
	gnuplot gnuplot/disk_capacity_used_5day.gnu
	disk_capacity_used=`cat ./../stockage_collection/bdd/${arr[$num_host]}.json | jq -r '.[0].disk_capacity_used'`
	echo "Less than 5 min ago the server ${arr[$num_host]} has $disk_capacity_used % of the used hard disk."
}

function graph_memory_available () {

	if [[ "${arr[$num_host]}" == "" ]]
	then
		choice_server
	fi
	gnuplot gnuplot/memory_available_5day.gnu
	memory_available=`cat ./../stockage_collection/bdd/${arr[$num_host]}.json | jq -r '.[0].memory_available'`
	echo "Less than 5 min ago the server ${arr[$num_host]} has $memory_available kb available on RAM."
}


function graph_tasks () {

	if [[ "${arr[$num_host]}" == "" ]]
	then
		choice_server
	fi
	gnuplot gnuplot/tasks.gnu
	task_total=`cat ./../stockage_collection/bdd/${arr[$num_host]}.json | jq -r '.[0].task_total'`
	echo "Less than 5 min ago the server ${arr[$num_host]} has the toal of $task_total tasks."
}


rep=1 
while [ "$rep" -eq 1 ]; do 
    printf "menu :\n\n" 
    echo "1. Loading data from a server" 
    echo "2. Graphic display of the number of users" 
    echo "3. Graphic display of disk usage" 
    echo "4. Graphic display of the RAM usage"
    echo "5. Graphic display of tasks usage" 
    echo -e "q. To quit\n"
	echo "Make a choice :"
    read   choix
    case "$choix" in 
		1)  	choice_server;;				
		2) 	graph_nbre_user_logged ;;		
		3) 	graph_disk_capacity_used ;;		
		4) 	graph_memory_available ;;		
		5) 	graph_tasks ;;	
        q) 
            echo "Goodbye" 
            
            rep=0 ;; 
        *) 
            echo "Input error"
			exit 101 ;;
            
    esac 
done

exit 0
