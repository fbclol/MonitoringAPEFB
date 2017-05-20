#!/bin/bash

##################################################################
###### ------  collecteur bash Collecteur.sh    ------ ###########
###### version : 1                                     ###########
###### date : 02/05/2017                               ###########
###### réalisé par : Franck & Pierre-E                 ###########
##################################################################

mkdir -p ./log
filelog="$PWD/log/collecteur_bash.json"

host_name=`hostname`
disk_capacity_used=`df -h | grep "dev/sd" | tr -s '' ' ' | cut -d" "   -f5 | tr -d '%'`
os_version=`cat /etc/issue | grep -o "^[^\]*"`
cpu=`top -bn1 | grep '%Cpu'`
nbr_users_logged=`top -bn1 | grep 'top -' | cut -d, -f2 | tr -s -d 'users ' ' '`
users_logged=`who | awk -F "[ (:0)]" '{printf "%-10s%17s\n", $1, $(NF-1)}' | uniq`
computer_duration=`uptime |  awk '{print $3}' | tr -d ','`
ip_local=`hostname -i`
ip_public=`wget -qO - icanhazip.com`
date=`date +"%Y-%m-%d-%X"`


echo "#####################################################"
echo "######## SYSTEM INFORMATION EXTRACTION ########"
echo "#####################################################"
echo ""
	echo "Computer name : $host_name"
	echo "ipv4 local : $ip_local"
	echo "ipv4 public : $ip_public"
	echo "---------------------- CPU ---------------------"
	echo " Utilisation du CPU : $cpu"
	echo ""
	echo "---------------------- DISQUES ---------------------"
	echo "Capacity used : $disk_capacity_used %"
	echo ""
	echo "---------------------- OS & VERSION ----------------------"
	echo "$os_version"
	echo ""
	echo "---------------------- autre info ----------------------"
	echo "List of connected users : $users_logged"
	echo "Number of users logged : $nbr_users_logged"
	echo "Server running time : $computer_duration"
	echo ""

 echo -n	'[{
  "hostname":"'$host_name'",
  "date":"'$date'",
  "ip_local": "'$ip_local'",
  "ip_public": "'$ip_public'",
  "cpu": "'$cpu'",
  "disk_capacity_used": "'$disk_capacity_used'",
  "os_version": "'$os_version'",
  "nbr_users_logged": "'$nbr_users_logged'",
  "users_logged": "'$users_logged'",
  "computer_duration": "'$computer_duration'"
}]' > $filelog
exit 0




	
