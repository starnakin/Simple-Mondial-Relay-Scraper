import requests
from bs4 import BeautifulSoup 
import datetime

def get(url):
    with requests.session() as rs:
        rs.get(url)
        login_data = {'referer': url}
        respond = rs.post(url, data=login_data)
        soup = BeautifulSoup(respond.text, 'lxml')

        data= {"delivered": False}

        events = {}

        for date in soup.findAll("div", {"class", "infos-account"}):
            event_date=date.findAll("strong")[0].text.split("/")
            year = int(event_date[2])
            month = int(event_date[1])
            day = int(event_date[0])
            for step in date.findAll("div", {"class", "step-suivi line-t"}):
                try:
                    event = step.findAll("p")[1].text.replace("\n", "")
                    if event == "Colis livré au destinataire":
                        data.update({"delivered": True})
                    event_date = step.findAll("p")[0].text.replace("\n", "").split(":")
                    hour=int(event_date[0])
                    minute=int(event_date[1])
                    date_data=datetime.datetime(year, month, day, hour, minute)
                    event_data=event
                    if events.get(date_data) == None:
                        events.update({date_data:[event_data]})
                    else:
                        event_by_date = events.get(date_data)
                        event_by_date.append(event_data)
                        events.update({date_data:event_by_date})
                except:
                    pass

        data.update({"events": events})


        return data
