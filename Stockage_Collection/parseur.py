#!/usr/bin/env python3
# coding: utf-8

import os
# os.system("apt-get install -y gcc python-dev python-pip python-bs4 python-lxml")
from bs4 import BeautifulSoup
import json
import urllib.request
from datetime import date

today = date.today()

with urllib.request.urlopen('http://www.cert.ssi.gouv.fr/') as response:
   html = response.read()
soup = BeautifulSoup(html, "html5lib")

valuehtml = soup.findAll('table')[5].find_all('td')[0].contents[1].get_text()
description = soup.findAll('table')[5].find_all('td')[2].contents[0]

class Alerte:
    def __init__(self, annee,alert,num,pdf,site):
        self.annee = annee
        self.alert = alert
        self.num = num
        self.description = description
        self.pdf = pdf
        self.site = site

def serialiseur_perso(obj):

    # Si c'est une Alerte.
    if isinstance(obj, Alerte):
        return {"__class__": "Alerte",
                "annee": obj.annee,
                "alert": obj.alert,
                "num": obj.num,
                "description": obj.description,
                "pdf": obj.pdf,
                "site": obj.site}

    # Sinon le type de l'objet est inconnu, on lance une exception.
    raise TypeError(repr(obj) + " n'est pas sérialisable !")


if os.path.isfile('parseur.json') == False:
    oAlerte = Alerte(alert=valuehtml,num=valuehtml.split('-')[3],annee=valuehtml.split('-')[1],pdf="http://www.cert.ssi.gouv.fr/site/"+valuehtml+".pdf",site="http://www.cert.ssi.gouv.fr/site/"+valuehtml+"/index.html")
    liste_Alerte = []
    liste_Alerte.append(oAlerte)
    #liste_Alerte.append(pl2)
    with open('parseur.json', 'w', encoding='utf-8') as f:
        json.dump(liste_Alerte, f, indent=4, default=serialiseur_perso)


data_file = open('parseur.json')
data = json.load(data_file)
if data[0]["num"] != valuehtml.split('-')[3]:
    oAlerte = Alerte(alert=valuehtml,num=valuehtml.split('-')[3],annee=valuehtml.split('-')[1],pdf="http://www.cert.ssi.gouv.fr/site/"+valuehtml+".pdf",site="http://www.cert.ssi.gouv.fr/site/"+valuehtml+"/index.html")
    data.insert(0,oAlerte)
    with open('parseur.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, default=serialiseur_perso)


i=0
while i < len(data):

    if data[i]["annee"] == str(today.year-1):
        del data[i]
        with open('parseur.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, default=serialiseur_perso)
    i += 1
	
	
	
print('mise a jour de alerte')
print('>> parseur.json')