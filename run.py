#! /usr/bin/env python3

import requests
import os
import json

url = 'http://localhost/fruits/'
dir ='supplier-data/descriptions/'

for f in os.listdir(dir):
    dict = {}
    if f.endswith('.txt'):
        with open(dir+f,encoding='utf-8') as fh:
            line=fh.readlines()
            dict['name'] = line[0].strip()
            dict['weight'] = int(line[1].strip().strip('lbs').strip())
            dict['description'] = line[2].strip()
            dict['image_name'] = f.strip('txt')+'jpeg'

    res=requests.post(url,data=dict)
    if res.status_code ==201:
        print ("Uploaded Data for : ", f)
