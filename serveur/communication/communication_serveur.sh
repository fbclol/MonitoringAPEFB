#! /bin/bash

host="172.17.0.2"
hostname="9bf6d4adc10f"
filedir="$PWD/../stockage_collection/bdd/"
HTTP_STATUS=`curl -IL --silent 172.17.0.2:5000/monitoring | grep HTTP | cut -d' ' -f2`;    

if [[ $HTTP_STATUS == "200" ]]
then

	TEMPFILE=$PWD/$RANDOM.tmp
	curl -o $TEMPFILE 172.17.0.2:5000/monitoring  
	filename=`cat $TEMPFILE | jq -r '.[].hostname'` 
	basename=$filedir$filename'.json'
	
	if [ ! -e $basename ]; then
		cat $TEMPFILE > $basename
		
	else
		extract_next=`cat $TEMPFILE`
		extract_old=`cat $basename`
		
		echo -e "${extract_next%]},${extract_old#[}"  > $basename
		
	fi
fi

./../affichage/module_alerte_date.py



exit 0