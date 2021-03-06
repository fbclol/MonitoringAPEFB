#!/bin/bash

##################################################################
###### ----- setup dependence, setup.sh    		 ----- ###########
###### version : 1                                     ###########
###### date : 20/05/2017                               ###########
###### realized by : Franck & Pierre-E                 ###########
##################################################################



# collecteur
sudo apt-get install -y wget python3 python3-setuptools python3-pip
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
easy_install3 pip
pip3 install socket
pip3 install psutil
pip3 install cryptography
pip3 install pyopenssl
pip3 install flask
pip3 install flask_httpauth
