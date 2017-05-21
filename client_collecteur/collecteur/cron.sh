#!/bin/bash

path=$PWD


# export crontab
crontab -l > /tmp/crontab.txt 

echo "*/5 * * * * sh $path/client.sh $PWD " >> /tmp/crontab.txt
echo "@reboot sh $path/../communication/communication_client.py" >> /tmp/crontab.txt
crontab /tmp/crontab.txt 
rm /tmp/crontab.txt 
# update de la crontab
/etc/init.d/cron reload
