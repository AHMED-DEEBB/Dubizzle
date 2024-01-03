# -*- coding: utf-8 -*-
"""Dubizzle Web Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CVf5xKuLSXToxvHY5JI3EBDbvkDQw2ew
"""

import requests
from bs4 import BeautifulSoup
import json

import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'referer': 'https://uae.dubizzle.com/en/property-for-sale/residential/'}

Dataset = []

for i in range(1, 10):

    url = 'https://uae.dubizzle.com/property-for-sale/residential/?page={i}'

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    posters = soup.find_all('a', class_='sc-fzQBhs sc-cDvQBt ffWDOe cLPeYo')


    for poster in posters:
        price = poster.find('div', class_='sc-fBWQRz sc-jGKxIK fEbvgi cKudTj').text
        property_type = poster.find('h2', attrs={'data-testid':'subheading-text'}).text
        bedrooms = poster.find('div', attrs={'data-testid':'listing-bedrooms'}).text
        bathrooms = poster.find('div', attrs={'data-testid':'listing-bathrooms'}).text
        size = poster.find('div', attrs={'data-testid':'listing-size'}).text
        location = poster.find('span', class_='MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-ncavm4').text

        Dataset.append([property_type, bedrooms, bathrooms, size, location, price])

df = pd.DataFrame(Dataset, columns=['property_type', 'bedrooms', 'bathrooms', 'size', 'location', 'price'])
df.head()

df.replace(r'', 1)

df.shape



dataset = df.to_json('Dubizzle_Dataset.json', orient='records')

print(dataset)

dataset = df.to_json(orient = 'columns')

# with open(r'Dubizzle_Dataset.json','a') as f:
#     json.dump(dataset,f,indent=2,sort_keys=True)

# print(dataset)




































data
