#!/bin/bash

# for cron
if [ ! $1 == "" ]
then
	cd $1
fi

# Collecteur bash
./collecteur.sh

# collecteur mixe
./collecteur_mixe.py

# collecteur python
./collecteur_python.py


# merge 
./../stockage_collection/merge.py


exit 0
