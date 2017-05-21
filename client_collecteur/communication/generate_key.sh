#!/bin/bash

country=FR
state="Some State"
town="Some Place"
email=boue.franck@orange.fr
domain=monitoring.fr
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout monitoring.com.key -out monitoring.com.crt -subj "/C=$country/ST=$state/L=$town/O=$domain/emailAddress=$email/CN=$domain"