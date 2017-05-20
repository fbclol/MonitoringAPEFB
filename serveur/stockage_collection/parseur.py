#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import json
import urllib.request
from datetime import date

#date du jour (y-m-d)
today = date.today()

#requete sur le site pour assigner le contenu dans une variable
with urllib.request.urlopen('http://www.cert.ssi.gouv.fr/') as response:
   html = response.read()
soup = BeautifulSoup(html, "html5lib")

valuehtml = soup.findAll('table')[5].find_all('tr')[0].contents[1].get_text().strip()
description = soup.findAll('table')[5].find_all('tr')[0].contents[3].text


# classe alerte
class Alerte:
    def __init__(self, annee,alert,num,pdf,site,description):
        self.annee = annee
        self.alert = alert
        self.num = num
        self.description = description
        self.pdf = pdf
        self.site = site

# méthode
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

# initialisation si le fichier n'existe pas (créer le premier de la liste des alertes
if os.path.isfile('parseur.json') == False:
    liste_Alerte = []
    oAlerte = Alerte(alert=valuehtml,
                     num=valuehtml.split('-')[3],
                     annee=valuehtml.split('-')[1],
                     pdf="http://www.cert.ssi.gouv.fr/site/"+valuehtml+".pdf",
                     site="http://www.cert.ssi.gouv.fr/site/"+valuehtml+"/index.html",
                     description=description)
    liste_Alerte.append(oAlerte)
    with open('parseur.json', 'w', encoding='utf-8') as f:
        json.dump(liste_Alerte, f, indent=4, default=serialiseur_perso)
    print('mise a jour des alerte')
    print('>> parseur.json')


# récupére le JSON sérialisé
data_file = open('parseur.json')
data = json.load(data_file)

i=0
numMax=int(max(data,key=lambda item:item['num'])['num'])
# récupére les alertes datant de 2017  et récupérer tout ce qui ne sont pas dans le JSON  avec un numéro d'alerte plus haut que celui du JSON
while ((soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().split('-')[1]) == str(today.year) and (int(soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().split('-')[3]) >= numMax))  :
    valuehtml=soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().strip()
    description=soup.findAll('table')[5].find_all('tr')[i].contents[3].text
    if numMax != int(valuehtml.split('-')[3]):
        print(soup.findAll('table')[5].find_all('tr')[i].contents[1].get_text().split('-')[3])
        oAlerte = Alerte(alert=valuehtml,
                         num=valuehtml.split('-')[3],
                         annee=valuehtml.split('-')[1],
                         pdf="http://www.cert.ssi.gouv.fr/site/"+valuehtml+".pdf",
                         site="http://www.cert.ssi.gouv.fr/site/"+valuehtml+"/index.html",
                         description=description)
        data.insert(0,oAlerte)

    i += 1

# si il y a des nouvelles alertes on les enregistre dans le fichier
if i > 0:
    with open('parseur.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, default=serialiseur_perso)
    print('mise a jour des alerte')
    print('>> parseur.json')


# supprime les alertes dépassé par le temps
i=0
data_file = open('parseur.json')
data = json.load(data_file)
while i < len(data):

    if data[i]["annee"] == str(today.year-1):
        del data[i]
        with open('parseur.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, default=serialiseur_perso)
    i += 1