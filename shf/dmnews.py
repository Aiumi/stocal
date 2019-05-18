from dmsuper import DMSuper
from algo import phraseFreq
from algo import PhraseMgr
import requests
import json
import urllib.request
from myhtml import text_from_html
import sys
import datetime
import time
import logging

class DMNews(DMSuper):
    
    def __init__(self):
        
        self.companyMap = dict()
    
    def getName(self, param:str) -> str:
    
        return param

    def getWeight(self):
        
        return .3
    
    def read(self):
    
        #sys.stdout = open('output.txt', 'w')
        
        #newsapi = NewsApiClient(api_key='bf87dc70b9af400d87207c4e23480ded')
        
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        print(date)
        
        queries = [
                'apple',
                'google'
        ]
        
        for query in queries:
            
            url = ('https://newsapi.org/v2/everything?'
                   'q=' + query + '&'
                   'domains=apnews.com,cnn.com,news.google.com,businessinsider.com,msnbc.com,time.com,economist.com,fortune.com,business.financialpost.com,cnbc.com,wsj.com,nytimes.com,bloomberg.com,bbc.com,reuters.com,apnews.com,ft.com&'
                   'from=' + date + '&'
                   'sortBy=relevancy&'
                   'pageSize=100&'
                   'apiKey=bf87dc70b9af400d87207c4e23480ded')
        
            #log url
            getobj = requests.get(url)
            
            #response = requests.get(url).json()
            #log json_data(getobj.text)
            json_data = json.loads(getobj.text)
            temp = json_data['articles']
            culm = [0, 0]
            name = self.getName(query)
            print(name)
            for t in temp:
                try:
                    #log a debug message
                    articleurl = t['url']
                    #log the article url
                    html = urllib.request.urlopen(articleurl).read()
                    #print(articleurl)
                    totals = phraseFreq(text_from_html(html))
                    #log a debug message for totals
                    culm[0] += totals[0]
                    culm[1] += totals[1]
                    #break
                    #log another debug message
                except:
                    print("Unexpected error:", sys.exc_info())
                    #log a warning message
                    #there is a logger.exception where you can pass an exception
            print('NEWS: ' + query + ' Totals: ' + str(culm))
            decision = 'Hold'
            #log the accumulated totals
            if culm[0] + culm[1] >= 15:
                decision = 'Buy'
            elif culm[0] + culm[1] <= -15:
                decision = 'Sell'
            #log the decision
        
            #print(query + ': ' + decision)
            self.companyMap[name] = culm
                    
    stdout_orig = sys.stdout
    
    PhraseMgr.reset()

    
    sys.stdout = stdout_orig


