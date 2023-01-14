import requests
import json
import time
import os
import pprint


def getPage(page = 0):
    params = {
        'text': 'NAME:analyst',
        'area': 1,
        'page': page,
        'per_page': 100,
        'order_by': 'publication_time'
    }
    req = requests.get('https://api.hh.ru/vacancies', params=params)
    data = req.content.decode()
    return data


def vacs():
    jsOBJ = json.loads(getPage())
    objects = []
    i = 0
    for item in jsOBJ['items']:
        post = {}

        if item['name']:
            post['name'] = item['name']

        if item['snippet']['requirement']:
            post['requir'] = item['snippet']['requirement']
            
        if item['snippet']['responsibility']:
            post['respon'] = item['snippet']['responsibility']
        
        if item['department']:
            post['dep'] = item['department']['name']
        else:
            post['dep'] = 'Не указано'

        if item['salary']:
            post['salary'] = item['salary']
            
        if item['area']['name']:
            post['area'] = item['area']['name']
        
        if item['published_at']:
            post['published_at'] = item['published_at'][0:10]

        objects.append(post)

        i += 1
        if i == 10:
            break
    return objects
# name snippet['requirement'] snippet['responsibility'] department['name'] salary area['name'] published_at 
