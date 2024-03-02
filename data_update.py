import requests
import os
from dotenv import load_dotenv
from enum import Enum
from datetime import date, timedelta
import json
from collections import defaultdict
import time
import pandas as pd


start_date = date(2024,2,16) 
end_date = date(2024,2,19)   

delta = end_date - start_date 
drange = []
for i in range(delta.days + 1):
    drange.append(str(start_date + timedelta(days=i)))


class Districts(Enum):
    Thrissur = 'IN-KL-TS'
    Kollam = 'IN-KL-KL'
    Thiruvananthapuram = 'IN-KL-TV'
    Eranakulam = 'IN-KL-ER'
    Wayanad = 'IN-KL-WA'
    Alappuzha = 'IN-KL-AL'
    Kannur = 'IN-KL-KN'
    Kottayam = 'IN-KL-KT'
    Kasaragod = 'IN-KL-KS'
    Pathanamthitta = 'IN-KL-PT'
    Palakkad = 'IN-KL-PL'
    Malappuram = 'IN-KL-MA'
    Kozhikode = 'IN-KL-KZ'
    Idukki = 'IN-KL-ID'
    Kerala = 'IN-KL'

load_dotenv()
api_key = os.getenv("key")

def fetch_data(drange):
    fetched = defaultdict(list)
    for d in drange:
        for p in Districts:

            td = d.split("-")
            r = requests.get(
            f"https://api.ebird.org/v2/product/stats/{p.value}/{td[0]}/{td[1]}/{td[2]}",
            params={'key': api_key}
            )
            jsondata = r.json()
            fetched["district"].append(p.name)
            fetched["Date"].append(d)
            fetched['numChecklists'].append(jsondata.get('numChecklists'))
            fetched['numContributors'].append(jsondata.get('numContributors'))
            fetched['numSpecies'].append(jsondata.get('numSpecies'))

    return fetched


def fetch_all(drange):
    fdict = defaultdict(list)
    for d in drange:
        for p in Districts:
            print(d,p.name)
            td = d.split("-")
            r = requests.get(
            f"https://api.ebird.org/v2/product/lists/{p.value}/{td[0]}/{td[1]}/{td[2]}?maxResults=2000",
            params={'key': api_key}, timeout=10
            )
            jsondata = r.json()
            for j in range(len(jsondata)):
                fdict["Date"].append(d)
                fdict["District"].append(p.name)
                fdict["locId"].append(jsondata[j].get('locId'))
                fdict["subId"].append(jsondata[j].get('subId'))
                fdict['userDisplayName'].append(jsondata[j].get('userDisplayName'))
                fdict['numSpecies'].append(jsondata[j].get('numSpecies'))
                fdict['obsDt'].append(jsondata[j].get('obsDt'))
                fdict['obsTime'].append(jsondata[j].get('obsTime'))
                fdict['isoObsDate'].append(jsondata[j].get('isoObsDate'))
                fdict['subID'].append(jsondata[j].get('subID'))
                loc = jsondata[j].get('loc', {})
                fdict['locId_A'].append(loc.get('locId'))
                fdict['place_name'].append(loc.get('name'))
                fdict['latitude'].append(loc.get('latitude'))
                fdict['longitude'].append(loc.get('longitude'))
                fdict['countryCode'].append(loc.get('countryCode'))
                fdict['countryName'].append(loc.get('countryName'))
                fdict['subnational1Name'].append(loc.get('subnational1Name'))
                fdict['subnational1Code'].append(loc.get('subnational1Code'))
                fdict['subnational2Code'].append(loc.get('subnational2Code'))
                fdict['subnational2Name'].append(loc.get('subnational2Name'))
                fdict['locID'].append(loc.get('locID'))
                fdict['locName'].append(loc.get('locName'))
                fdict['isHotspot'].append(loc.get('isHotspot'))
                fdict['lat'].append(loc.get('lat'))
                fdict['lng'].append(loc.get('lng'))
                fdict['hierarchicalName'].append(loc.get('hierarchicalName'))
                
            time.sleep(10)
    return fdict


if __name__=="__main__":

    overall_stats = fetch_data(drange)
    detailed_stats = fetch_all(drange)

    df = pd.DataFrame(detailed_stats)
    df.to_csv(f"2024/all_{str(start_date)}_{str(end_date)}.csv", index=None)

    df2 = pd.DataFrame(overall_stats)
    df2.to_csv(f"2024/overall_{str(start_date)}_{str(end_date)}.csv", index=None)



                








