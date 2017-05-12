#!/bin/bash

#*/5 * * * * root /home/monitoring/client.sh
filelog="./log/collecteur_bash.json"
filelog_py="./log/collecteur_python.json"
filelog_mixe="./log/collecteur_mixe.json"
#app="python3"
#service=`apt-cache policy $app | grep none | wc -m`

#echo $service
#if [ $service -ne 20 ];
#then
#	apt-get install -y $app;
#	apt-get install -y $app-psutil;
#else
#	echo "le service $app est déjà installé"
#fi

# Collecteur bash
./collecteur.sh
# collecteur mixe
./collecteur_mixe.py
# collecteur python
./collecteur_python.py

#client.py
#merge ici
./../stockage_collection/merge.py

echo "un fichier pour le collecteur bash vient d'être modifié : $filelog"
echo "un fichier pour le collecteur bash vient d'être modifié : $filelog_py"
echo "un fichier pour le collecteur bash vient d'être modifié : $filelog_mixe"

exit 0
