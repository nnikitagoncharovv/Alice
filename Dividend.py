from bs4 import BeautifulSoup
import requests
import re

def dividend(a):
    tickers = []
    names = []
    f = []
    q = []
    base_url = "https://www.dohod.ru/ik/analytics/dividend/" 
    response = requests.get(base_url)
    if response.status_code == 200:
        html = response.text 
    soup = BeautifulSoup(html, "html.parser")
    dividend = soup.find(id = 'table-dividend')
    t = soup.find_all('td')
    for td in t:
        if td.find('a'):
            u = td.find('a').get('href').split('/ik/analytics/dividend/')[1:]
            tickers.append(u)
            b = td.find('a').text
            names.append(b)
            list(names)     
    tickers = sum(tickers, [])
    for i in tickers:
        if i != a:
            f.append(i)
            if len(f) > len(tickers):
                break
        else:
            break
    f=len(f)
    for i in names:
        if i != a:
            q.append(i)
            if len(q) > len(names):
               break
        else:
            break
    q=len(q)
    if f > q:
        f = q
    url = base_url+tickers[f]
    namepaper = names[f]
    responsee = requests.get(url).text
    soupp = BeautifulSoup(responsee, "html.parser")
    divdoh = soupp.find('td').text
    print('Дивидендная доходность акции',namepaper, '=', divdoh)

while True:
    dividend(input())
