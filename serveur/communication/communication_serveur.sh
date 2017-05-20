#! /bin/bash

# récuperer les ip des collecteurs dans le fichier de conf
. collecteur_hosts.conf

for host in ${collecteur_hosts[@]}; do
        
	filedir="$PWD/../stockage_collection/bdd/"
	HTTP_STATUS=`curl -IL --silent -u monitoring:p7tH0n@#! $host:5000/api/monitoring | grep HTTP | cut -d' ' -f2`;    

	if [[ $HTTP_STATUS == "200" ]]
	then

		tmp_file=$PWD/$RANDOM.tmp
		curl -u monitoring:p7tH0n@#! -H "Accept: application/json" -X GET 172.17.0.2:5000/api/monitoring | jq '.response' >> $tmp_file
		filename=`cat $tmp_file | jq -r '.[].hostname'` 
		basename=$filedir$filename'.json'
	
		if [ ! -e $basename ]; then
			cat $tmp_file > $basename
		
		else
			extract_next=`cat $tmp_file`
			extract_old=`cat $basename`
		
			#echo -e "${extract_next%]},${extract_old#[}"  > $basename
			rm -f $tmp_file
		fi
	fi

	./../affichage/module_alerte_date.py $filename

done

exit 0