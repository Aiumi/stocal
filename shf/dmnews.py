from shf import dmsuper, algo, myhtml
#from company_data import company_data
import requests
import json
import urllib.request
import sys
import datetime
import time
import logging
import traceback

class DMNews(dmsuper.DMSuper):
    
    def __init__(self):
        
        self.companyMap = dict()
        self.resultslist = list()
        self.companieslist = list()
        
    def getName(self, param:str) -> str:
    
        return param

    def getWeight(self):
        
        return .3
    
    def read(self):
        
        #newsapi = NewsApiClient(api_key='bf87dc70b9af400d87207c4e23480ded')
        
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        print(date)
        
        queries = [
                'Google',
                'Facebook'
        ]
        
        for query in queries:
            
            #company = company_data(query)
            #self.companieslist.append(company)
            
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
            totals = [0, 0]
            for t in temp:

                try:
                    #log a debug message
                    articleurl = t['url']
                    #log the article url
                    html = urllib.request.urlopen(articleurl).read()
                    #print(articleurl)
                    totals = algo.phraseFreq(myhtml.text_from_html(html))
                    #log a debug message for totals
                    culm[0] += totals[0]
                    culm[1] += totals[1]
                    #company.articles.append(['Headline', articleurl, totals])
                    #break
                    #log another debug message
                except:
                    print("Unexpected error:", sys.exc_info())
                    #traceback.print_exc(file=sys.stdout)
                    #log a warning message
                    #there is a logger.exception where you can pass an exception
            print('NEWS: ' + query + ' Totals: ' + str(culm))
            decision = 'Is Neutral'
            #log the accumulated totals
            if culm[0] + culm[1] >= 50:
                decision = 'Trending Upwards'
            elif culm[0] + culm[1] <= -50:
                decision = 'Trending Downwards'
            #log the decision
        
            #self.companyMap[name] = culm
            resultstuple = tuple([query, decision])

            self.resultslist.append(resultstuple)
            self.resultslist.append(tuple(culm))
            self.resultslist.append(["Articles found: ", len(temp)])
            
        print(len(self.resultslist))
        algo.PhraseMgr.reset()
        return self.resultslist



