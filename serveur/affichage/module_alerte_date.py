#!/usr/bin/env python3
# coding: utf-8
from datetime import datetime
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
maintenant = datetime.now()

data_file = open('../stockage_collection/bdd/9bf6d4adc10f.json')
data = json.load(data_file)
datetime_object = datetime.strptime(data[0]["date"],'%Y-%m-%d-%H:%M:%S')
duree = datetime.now() - datetime_object


def envoie_mail(num):
    fromaddr = "testmailbidon126@gmail.com"
    toaddr = "boue.franck@orange.fr"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "[ALTERTE SERVEUR]- 9bf6d4adc10f "
    if num ==1:
     body="Le serveur 9bf6d4adc10f n'a pas donné signe de vie depuis plus de 30min"
    elif num ==2:
     body="Le serveur 9bf6d4adc10f n'a plus de place sur le disque"
    elif num ==3:
     body="Le serveur 9bf6d4adc10f n'a plus de RAM disponible"
    else:
     body="defaut"

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "testmail")
    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()


# module date
if duree.total_seconds() > 1800:
    envoie_mail(1)

if data['disque_use'] == 100:
    envoie_mail(2)

if data['ram_dispo'] == 0:
    envoie_mail(3)