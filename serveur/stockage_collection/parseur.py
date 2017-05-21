#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import json
import urllib.request
from datetime import date

# today's date (y-m-d)
today = date.today()

# Query on the site to assign the content in a variable
with urllib.request.urlopen('http://www.cert.ssi.gouv.fr/') as response:
    html = response.read()
soup = BeautifulSoup(html, "html5lib")

valuehtml = soup.findAll('table')[5].find_all('tr')[0].contents[1].get_text().strip()
description = soup.findAll('table')[5].find_all('tr')[0].contents[3].text


# class alert
class Alert:
    def __init__(self, year, alert, num, pdf, site, description):
        self.year = year
        self.alert = alert
        self.num = num
        self.description = description
        self.pdf = pdf
        self.site = site


# method serialiseur_perso
def serialiseur_perso(obj):
    # If it's an Alert.
    if isinstance(obj, Alert):
        return {"__class__": "Alerte",
                "year": obj.year,
                "alert": obj.alert,
                "num": obj.num,
                "description": obj.description,
                "pdf": obj.pdf,
                "site": obj.site}

    # If the type of the object is unknown, an exception is thrown.
    raise TypeError(repr(obj) + " Is not serializable!")


# initialization if the file does not exist, creating the first of the list alerts
if not os.path.isfile('parseur.json'):
    liste_Alerte = []
    oAlerte = Alert(
        alert=valuehtml,
        num=valuehtml.split('-')[3],
        year=valuehtml.split('-')[1],
        pdf="http://www.cert.ssi.gouv.fr/site/" + valuehtml + ".pdf",
        site="http://www.cert.ssi.gouv.fr/site/" + valuehtml + "/index.html",
        description=description)
    liste_Alerte.append(oAlerte)
    with open('parseur.json', 'w', encoding='utf-8') as f:
        json.dump(liste_Alerte, f, indent=4, default=serialiseur_perso)
    print('mise a jour des alerte')
    print('>> parseur.json')

# récupére le JSON sérialisé
data_file = open('parseur.json')
data = json.load(data_file)

i = 0
numMax = int(max(data, key=lambda item: item['num'])['num'])
# récupére les alertes datant de 2017  et récupérer tout ce qui ne sont pas dans le JSON  avec un numéro d'alerte plus haut que celui du JSON
while ((soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().split('-')[1]) == str(today.year) and (
            int(soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().split('-')[3]) >= numMax)):
    valuehtml = soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().strip()
    description = soup.findAll('table')[5].find_all('tr')[i].contents[3].text
    if numMax != int(valuehtml.split('-')[3]):
        print(soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().split('-')[3])
        oAlerte = Alerte(alert=valuehtml,
                         num=valuehtml.split('-')[3],
                         year=valuehtml.split('-')[1],
                         pdf="http://www.cert.ssi.gouv.fr/site/" + valuehtml + ".pdf",
                         site="http://www.cert.ssi.gouv.fr/site/" + valuehtml + "/index.html",
                         description=description)
        data.insert(0, oAlerte)

    i += 1

# If there are new alerts they are saved in the file
if i > 0:
    with open('parseur.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, default=serialiseur_perso)
    print('mise a jour des alerte')
    print('>> parseur.json')

# Remove alerts overrun by time
i = 0
data_file = open('parseur.json')
data = json.load(data_file)
while i < len(data):

    if data[i]["year"] == str(today.year - 1):
        del data[i]
        with open('parseur.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, default=serialiseur_perso)
    i += 1
