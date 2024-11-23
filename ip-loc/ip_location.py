#!/usr/bin/env python3
import requests

res = requests.get('https://ipinfo.io/')
data = res.json()


def get_nested_dict(d):
    
    for k,v in d.items():
        if isinstance(v, dict):
            print('Found nested dictionary')
            get_nested_dict(v)
        else:
            print(f'{k}: {v}')
            
get_nested_dict(data)


