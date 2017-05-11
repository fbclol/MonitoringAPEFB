#! /bin/bash

TEMPFILE=$PWD/$RANDOM.tmp

filedir="$PWD/../stockage_collection/bdd/"

curl -o $TEMPFILE 172.17.0.2:5000/monitoring  

filename=`cat $TEMPFILE | jq -r '.[].hostname'` 
basename=$filedir$filename'.json'

if [ ! -e $basename ]; then
	cat $TEMPFILE > $basename
	unlink $TEMPFILE
else
	extract_next=`cat $TEMPFILE`
	extract_old=`cat $basename`
	
	echo -e "${extract_old%]},${extract_next#[}"  > $basename
	unlink $TEMPFILE
fi