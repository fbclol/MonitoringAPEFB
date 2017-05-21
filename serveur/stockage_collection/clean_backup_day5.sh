#!/bin/bash

# for cron
if [ ! $1 == "" ]
then
	cd $1
fi

## Supprime les sauvegardes et les répértoires  vieux  de plus de 5 jours
find $PDW/archive -name "*.gz" -mtime +5 -delete
