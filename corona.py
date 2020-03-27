import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt
print('\n')
print(os.system("clear && figlet 'CORONA LIVE STATUS' -f digital -c"))

print('\n')
extract_contents = lambda row: [x.text.replace('\n','') for x in row]
URL = 'https://www.mohfw.gov.in/'
SHORT_HEADERS = ['SNo','State','Indian-Confirmed','Foreegn-Confirmed','Cured','Death']
response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents (soup.tr.find_all('td'))
stats = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if stat:
        if len(stat) == 5:
            stat = ['',*stat]
            stats.append(stat)
        elif len(stat) == 6:
            stats.append(stat)

stats[-1][1] = "Total Cases"
stats.remove(stats[-1])
objects = []
for row in stats:
    objects.append(row[1])
y_pos = np.arange(len(objects))
performance = []
for row in stats:
    performance.append(int(row[2]) + int(row[3]))

table = tabulate(stats, headers = SHORT_HEADERS)
print(table)


print('\n')

print('\n')

print('\n')

