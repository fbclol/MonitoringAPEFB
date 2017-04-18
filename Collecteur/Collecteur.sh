#!/bin/bash

CPU=`lscpu | sed -n 13p`
GRAPHIC_CARD=`lspci | grep VGA`
DISQUES=`df -h`
#RAM=`free -m`
RAM=`cat /proc/meminfo | sed -n 1p`
#PROCESS= ``
OS_VERSION=`cat /etc/issue`
USERS=`who`


echo "#####################################################"
echo "######## EXTRACTION D'INFORMATION DU SYSTEME ########"
echo "#####################################################"
echo ""
echo ""
while true
do
	echo "---------------------- CPU ---------------------"
	echo "$CPU"
	echo ""
	echo "---------------------- RAM ---------------------"
	echo "$RAM"
	echo ""
	echo "---------------------- CARTE GRAPHIQUE ---------------------"
	echo "$GRAPHIC_CARD"
	echo ""
	echo "---------------------- DISQUES ---------------------"
	echo "$DISQUES"
	echo ""
	echo "---------------------- OS & VERSION ----------------------"
	echo "$OS_VERSION"
	echo ""
	echo "---------------------- NBR USERS CONNECTES ----------------------"
	echo "$USERS"
	echo ""

	sleep 120
done

