from bs4 import BeautifulSoup

import requests

def get(url):



    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')
 
    data= {}

    date = {}

    events = soup.findAll("div", {"class", "infos-account"})

    for i in events:
        if i.find("div", {"class", "col-xs-8 col-sm-9 col-md-9"}).text.replace("\n", "") == "Colis livré au destinataire":
            data.update({"delivered": True})
        date.update({(i.find("div", {"class", "col-xs-4 col-sm-3 col-md-3"}).text.replace("\n", "")): (i.find("div", {"class", "col-xs-8 col-sm-9 col-md-9"}).text.replace("\n", ""))})

    data.update({"events": date})

    return data

print(get("https://www.mondialrelay.fr/suivi-de-colis/?NumeroExpedition=97602273&CodePostal=92140"))