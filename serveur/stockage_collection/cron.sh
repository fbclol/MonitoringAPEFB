#!/bin/bash

path=$PWD

# export  crontab
crontab -l > /tmp/crontab.txt 

echo "@daily sh $path/parseur.py $PWD/ " >> /tmp/crontab.txt
echo "@daily sh $path/clean_backup_day5.sh $PWD/ " >> /tmp/crontab.txt
echo "*/5 * * * *  sh $path/../communication/communication_serveur.sh $PWD/ " >> /tmp/crontab.txt
crontab /tmp/crontab.txt 
rm /tmp/crontab.txt 
# update de la crontab
/etc/init.d/cron reload
