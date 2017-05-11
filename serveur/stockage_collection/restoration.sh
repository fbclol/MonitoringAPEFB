#!/bin/bash

# Enregistrez ce script sous le nom restore.sh. Prennez également note de son emplacement.

echo "------------------------------------------------------";
echo "- Restauration du système";
echo "------------------------------------------------------";
echo "";

echo "Récupération et extraction de l'archive";
# we verified that an argument has been passed to the program
if [ $# != 1 ] ; then
	echo "It is necessary to add a file name as a parameter.";
	exit 101;
fi

path_temp=$PWD
# On se place à la /(racine)
cd /
# On extrait les répertoires archivés en ne mettant PAS le / devant
tar -xvzf $path_temp/archive/backup-$1.tar.gz "${path_temp#/}/bdd/" "${path_temp#/}/parseur.json"
echo "------------------------------------------------------";
echo "";

echo "### Fin de l'extraction des fichiers.  ###";
exit 0