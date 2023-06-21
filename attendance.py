import requests
from bs4 import BeautifulSoup
import re

def teacher(response):
    details = response.select("h3.md-card-head-text")
    details = details[0].text.strip()
    details = details.split(" ")
    name = " ".join(details[0:2])
    email = (response.select(".md-card-head-text > span:nth-child(3)")[0]).text
    try:
        number = int((response.select(".md-card-head-text > span:nth-child(4)")[0]).text)
    except:
        number=0
    return {
        'name':name,
        'email':email,
        'number':number
    }

def status(response):

    def requirement(p,a,l):
        total = p+a+l
        for85 = int(total*0.85)-p
        for75 = int(total*0.75)-p
        return {'for85':for85 , 'for75' : for75}

    try:
        present = int(re.findall(r'\d+', (response.select("span.cn-attend")[0]).text)[0])
    except:
        present =0
    try:
        absent = int(re.findall(r'\d+', (response.select("span.uk-label:nth-child(2)")[0]).text)[0])
    except:
        absent=0
    try:
        still = int(re.findall(r'\d+', (response.select("span.uk-label:nth-child(3)")[0]).text)[0])
    except:
        still=0
    
    result={}
    result['present']=present
    result['absent']=absent
    result['left']=still

    result.update(requirement(present,absent,still))
    return result


def present(response):
    table= response.find('table', class_="uk-table uk-table-small cn-attend-list1 uk-table-striped")

    rows = []
    for i, row in enumerate(table.find_all('tr')):
        if i==0:
            continue
        data=[el.text.strip() for el in row.find_all('td')][0:2]
        sample = {data[0]:data[1]}
        rows.append(sample)

    return rows
    

def absent(response):
    table= response.find('table', class_="uk-table uk-table-small cn-attend-list2 uk-table-striped")

    rows = []
    for i, row in enumerate(table.find_all('tr')):
        if i==0:
            continue
        data=[el.text.strip() for el in row.find_all('td')][0:2]
        sample = {data[0]:data[1]}
        rows.append(sample)

    return rows


    
