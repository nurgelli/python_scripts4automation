#!/usr/bin/env python3
import requests


res = requests.get('https://api.datamuse.com/words')
data = res.json()
print(data)



