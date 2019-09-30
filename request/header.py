#!/usr/bin/python

import requests

myheaders = {'User-Agen' : 'Windows 10'}
r = requests.get('http://arh.bg.ac.rs',headers=myheaders)

print r.text
