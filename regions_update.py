import requests
import os
from dotenv import load_dotenv
import yaml
import json


load_dotenv()
api_key = os.getenv("key")

p = {}
q = {}

r = requests.get(
        f"https://api.ebird.org/v2/ref/region/list/subnational1/IN",
        params={'key': api_key}
        )


for dct in r.json():
    r1 = requests.get(
        f"https://api.ebird.org/v2/ref/region/list/subnational2/{dct['code']}",
        params={'key': api_key}
        )
    q[dct['name']] = dct['code']
    p[dct['name']] = {}
    for pp in r1.json():
        p[dct['name']][pp['name']]= pp['code']

states = dict()
states["states"] = q
subr = {}
subr["subregions"] = p

with open("subregion_list_india.yml","w") as f:
    yaml.dump(states,f)

with open("subregion_list_india.yml","a") as f:
    yaml_text = yaml.dump(subr)
    f.write(yaml_text)