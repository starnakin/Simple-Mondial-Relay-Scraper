from bs4 import BeautifulSoup

import requests

def get(url):



    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')
 
    data= {}

    date = {}

    events = soup.findAll("div", {"class", "infos-account"})
    for i in events:
        event_date=i.findAll("strong")[0].text
        for j in i.findAll("div", {"class", "step-suivi line-t"}):
            try:
                if j.findAll("p")[1].text.replace("\n", "") == "Colis livré au destinataire":
                    data.update({"delivered": True})
                date.update({event_date+j.findAll("p")[0].text.replace("\n", ""): j.findAll("p")[1].text.replace("\n", "")})
            except:
                pass
    data.update({"events": date})

    return data

print(get("https://www.mondialrelay.fr/suivi-de-colis/?NumeroExpedition=97602273&CodePostal=92140"))