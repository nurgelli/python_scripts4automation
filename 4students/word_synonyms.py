#!/usr/bin/env python3
import requests


res = requests.get('https://api.datamuse.com/words?ml=duck')
data = res.json()
print(data)
for n, i in enumerate(data, 1):
    print(n, i["word"])
    
    


