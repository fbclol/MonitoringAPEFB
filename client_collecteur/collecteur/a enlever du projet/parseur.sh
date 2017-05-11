#!/bin/bash

# app="wget"
# service=`apt-cache policy $app | grep none | wc -m`

# echo $service
# if [ $service -ne 0 ];
# then

	# apt-get install -y $app;
# else
	# echo "le service $app est déjà installé"
# fi

# app="python-bs4"
# service=`apt-cache policy $app | grep none | wc -m`

# echo $service
# if [ $service -ne 0 ];
# then

	# apt-get install -y $app;
# else
	# echo "le service $app est déjà installé"
# fi


#wget -P $PWD/ http://www.cert.ssi.gouv.fr
#cat $PWD/index.html | grep -n "<item><title>CERTFR" | grep "10:" >> parseur.json


#echo -n	'{
#  "num_altert": "'$NOMPROCESSEUR'",
#  "description":"'$HOSTNAME'",
#  "url": "''",
#  "date": "''",
#  "utilisation_cpu": "'$UTILISATIONCPU'"
#} ' > parseur.json

#./parseur.py
#$PWD/index.html*