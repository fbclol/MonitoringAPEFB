#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime
import json
import smtplib
import os, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Constant python
_CODE_ALERT_MAIL_FUNCTIONING=1
_CODE_ALERT_MAIL_DISK=2
_CODE_ALERT_MAIL_RAM=3
_CODE_ALERT_MAIL_CPU=4

#There must be an argument.
#hostname to point to each of the collectors
if len(sys.argv) > 1:

    data_file = open('../stockage_collection/bdd/'+sys.argv[1]+'.json')
    data = json.load(data_file)
    datetime_object = datetime.strptime(data[0]["date"],'%Y-%m-%d-%H:%M:%S')
    duree = datetime.now() - datetime_object

    # méthode envoie_mail()
    # template email
    # param num int
    def send_mail(code):
        fromaddr = "testmailbidon126@gmail.com"
        toaddr = "boue.franck@orange.fr"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        if code == _CODE_ALERT_MAIL_FUNCTIONING:
         msg['Subject'] = "[ALERT SERVER][FUNCTIONING]- "+sys.argv[1]
         body="The server "+sys.argv[1]+" Has not given a sign of life for more than 30 min"
        elif code == _CODE_ALERT_MAIL_DISK:
         msg['Subject'] = "[ALERT SERVER][DISK]-  "+sys.argv[1]
         body="The server "+sys.argv[1]+" has no more space on the disk"
        elif code == _CODE_ALERT_MAIL_RAM:
         msg['Subject'] = "[ALERT SERVER][RAM]- "+sys.argv[1]
         body="The server "+sys.argv[1]+"  has no more RAM disponible"
        elif code == _CODE_ALERT_MAIL_CPU:
         msg['Subject'] = "[ALERT SERVER][CPU]- "+sys.argv[1]
         body="The server "+sys.argv[1]+" has no more CPU available"
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


    # Sends different mail according to the crises
    if duree.total_seconds() > 1800:
        send_mail(code= _CODE_ALERT_MAIL_FUNCTIONING)

    if int(data[0]['disk_capacity_used']) == 100:
        send_mail(code= _CODE_ALERT_MAIL_DISK)

    if int(data[0]['memory_available']) == 0:
        send_mail(code= _CODE_ALERT_MAIL_RAM)
    if int(data[0]['cpu_usage']) == 100:
        send_mail(code= _CODE_ALERT_MAIL_CPU)
else:
    print("Missing an argument")