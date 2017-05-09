#!/bin/bash

#restoration
#tar -xvzf $PWD/sauvegarde.tar.gz "$PWD"

mkdir -p $PWD/archive/
# Enregistrez ce script sous le nom de backup.sh. Prennez note de son emplacement.

echo "------------------------------------------------------";
echo "- Sauvegarde des log & du parseur.json-";
echo "------------------------------------------------------";
echo "";

echo "Création de l'archive";
# On crée l'archive .tar en précisant entre guillemets les chemins absolus des dossiers à sauvegarder.
tar -cvzf $PWD/archive/backup-`date +"%Y-%m-%d"`.tar.gz "/var/run/log/collecteurMonitoring/" "$PWD/parseur.json"

echo "------------------------------------------------------";

echo "Vérification de l'existence de l'archive";
if [ -e $PWD/archive/backup-`date +"%Y-%m-%d"`.tar.gz ]
then
	echo ""
	echo "Votre archive a bien été créée.";
	echo ""
else
	echo ""
	echo "Il y a eu un problème lors de la création de l'archive.";
	echo ""
fi

echo "### Fin de la sauvegarde.  ###";

echo "supression des sauvegardes vieux de plus de 5jours"
## Supprime les sauvegardes et les répértoires  vieux  de plus de 5 jours
find $PWD/archive -name "*.gz" -mtime +5 -delete