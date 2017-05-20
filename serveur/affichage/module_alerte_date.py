#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import json
import smtplib
import os, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

maintenant = datetime.now()




if len(sys.argv) > 1:

    data_file = open('../stockage_collection/bdd/'+sys.argv[1]+'.json')
    data = json.load(data_file)
    datetime_object = datetime.strptime(data[0]["date"],'%Y-%m-%d-%H:%M:%S')
    duree = datetime.now() - datetime_object

    def envoie_mail(num):
        fromaddr = "testmailbidon126@gmail.com"
        toaddr = "boue.franck@orange.fr"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        #msg['Subject'] = "[ALTERTE SERVEUR]- "+sys.argv[1]
        if num ==1:
         msg['Subject'] = "[ALTERTE SERVEUR][fonctionnement]- "+sys.argv[1]
         body="Le serveur "+sys.argv[1]+" n'a pas donné signe de vie depuis plus de 30min"
        elif num ==2:
         msg['Subject'] = "[ALTERTE SERVEUR][disque]-  "+sys.argv[1]
         body="Le serveur "+sys.argv[1]+" n'a plus de place sur le disque"
        elif num ==3:
         msg['Subject'] = "[ALTERTE SERVEUR][ram]- "+sys.argv[1]
         body="Le serveur "+sys.argv[1]+" n'a plus de RAM disponible"
        else:
         body="defaut"

        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, "testmail")

        text = msg.as_string()

        server.sendmail(fromaddr, toaddr, text)
        server.quit()


    # module date
    if duree.total_seconds() > 1800:
        envoie_mail(1)

    if int(data[0]['disque_use']) == 100:
        envoie_mail(2)

    if int(data[0]['ram_dispo']) == 0:
        envoie_mail(3)
else:
    print("manque un arguement")