#! /bin/bash

# récuperer les ip des collecteurs dans le fichier de conf
. collecteur_hosts.conf

for host in ${collecteur_hosts[@]}; do
        
	filedir="$PWD/../stockage_collection/bdd/"
	http_status=`curl -IL --silent -u monitoring:p7tH0n@#! https://$host:5000/api/monitoring -k | grep HTTP | cut -d' ' -f2`;    
	filename=""
	if [[ $http_status == "200" ]]
	then

		tmp_file=$PWD/$RANDOM.tmp
		curl --silent -u monitoring:p7tH0n@#! -H "Accept: application/json" -X GET https://$host:5000/api/monitoring -k | jq '.response' >> $tmp_file
		filename=`cat $tmp_file | jq -r '.[].hostname'` 
		basename=$filedir$filename'.json'
	
		if [ ! -e $basename ]; then
			cat $tmp_file > $basename
		
		else
			extract_next=`cat $tmp_file`
			extract_old=`cat $basename`
		
			echo -e "${extract_next%]},${extract_old#[}"  > $basename
			rm -f $tmp_file
		fi
	fi

	if [[ ! $filename == "" ]]
	then
		echo "The collector $host will be analyzed for the crisis system"
		./../affichage/module_alerte_date.py $filename
	else
		echo "The collector $host does not respond "
	fi
done

exit 0