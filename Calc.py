#!/usr/bin/python
from os import environ
import json
import urllib.request
import sys
import requests
#from shf import dmsuper
from shf import algo, myhtml
import datetime

def calc(company):
    
    query = company
    
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    
    url = ('https://newsapi.org/v2/everything?'
                       'q=' + query + '&'
                       'domains=apnews.com,cnn.com,news.google.com,businessinsider.com,msnbc.com,time.com,economist.com,fortune.com,business.financialpost.com,cnbc.com,wsj.com,nytimes.com,bloomberg.com,bbc.com,reuters.com,apnews.com,ft.com&'
                       'from=' + date + '&'
                       'sortBy=relevancy&'
                       'pageSize=100&'
                       'apiKey=bf87dc70b9af400d87207c4e23480ded')
    
    getobj = requests.get(url)
                
    #response = requests.get(url).json()
    #log json_data(getobj.text)
    json_data = json.loads(getobj.text)
    temp = json_data['articles']
    culm = [0, 0]
    for t in temp:
        try:
            #log a debug message
            articleurl = t['url']
            print(articleurl)
            html = urllib.request.urlopen(articleurl).read()
            #print(articleurl)
            totals = phraseFreq(text_from_html(html))
            #log a debug message for totals
            culm[0] += totals[0]
            culm[1] += totals[1]
            break
        except:
            print("Unexpected error:", sys.exc_info())
    print('NEWS: ' + query + ' Totals: ' + str(culm))
    decision = 'Hold'
    #log the accumulated totals
    if culm[0] + culm[1] >= 5:
        decision = 'Buy'
    elif culm[0] + culm[1] <= -5:
        decision = 'Sell'
    return company + ': ' + decision
    #log the decision



