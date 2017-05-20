#!/bin/bash

##################################################################
###### ----- setup dependence, setup.sh    		 ----- ###########
###### version : 1                                     ###########
###### date : 20/05/2017                               ###########
###### realized by : Franck & Pierre-E                 ###########
##################################################################


apt-get install -y wget
apt-get install -y python3
apt-get install -y python3-setuptools
apt-get install python3-pip
easy_install3 pip
pip3 install socket
pip3 install psutil


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