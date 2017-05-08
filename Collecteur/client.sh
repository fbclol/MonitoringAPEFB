#!/bin/bash

#*/5 * * * * root /home/monitoring/client.sh
filelog="/var/run/log/collecteurMonitoring/collecteur_bash.json"
filelog_py="/var/run/log/collecteurMonitoring/CollecteurPy.json"
filelog_mixe="/var/run/log/collecteurMonitoring/collecteur_mixe.json"

app="wget"
service=`apt-cache policy $app | grep none | wc -m`
echo $service
if [ $service -ne 0 ];
then

apt-get install -y $app;
else
echo "le service $app est déjà installé"
fi

app="python"
service=`apt-cache policy $app | grep none | wc -m`
echo $service
if [ $service -ne 0 ];
then

apt-get install -y $app;
else
echo "le service $app est déjà installé"
fi


# Collecteur bash
./Collecteur.sh

# collecteur mixe
./Collecteur2.py
# collecteur python
./CollecteurFULLPY.py

#client.py


echo "un fichier pour le collecteur bash vient d'être modifié : $filelog"
echo "un fichier pour le collecteur bash vient d'être modifié : $filelog_py"
echo "un fichier pour le collecteur bash vient d'être modifié : $filelog_mixe"

exit 0