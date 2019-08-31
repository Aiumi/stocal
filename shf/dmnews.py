from shf import dmsuper, algo, myhtml, company_data
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

        self.companieslist = list()
        
    def getName(self, param:str) -> str:
    
        return param

    def getWeight(self):
        
        return .3
    
    def read(self, queries):
        
        #newsapi = NewsApiClient(api_key='bf87dc70b9af400d87207c4e23480ded')
        
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        print(date)
        
        '''queries = [
                'Uber',
                'Lyft',
                'Nintendo'
        ]'''
        
        for query in queries:
            
            c_data = company_data.company_data(query)
            self.companieslist.append(c_data)
            
            print("***")
            name = c_data.get_stripped_name()
            print(">>>" + name + "<<<")
            
            url = ('https://newsapi.org/v2/everything?'
                   'q=' + name + '&'
                   'domains=apnews.com,cnn.com,news.google.com,businessinsider.com,fool.com,msnbc.com,time.com,economist.com,fortune.com,business.financialpost.com,cnbc.com,wsj.com,nytimes.com,bloomberg.com,bbc.com,reuters.com,apnews.com,ft.com,techcrunch.com,techradar.com&'
                   'language=en&'
                   'from=' + date + '&'
                   'sortBy=relevancy&'
                   'pageSize=100&'
                   'apiKey=bf87dc70b9af400d87207c4e23480ded')

            getobj = requests.get(url)

            json_data = json.loads(getobj.text)
            art = json_data['articles']
            #name = self.getName(query)
            totals = [float(0), float(0)]
            count = 0
            for t in art:
                count += 1
                if count >= 8:
                    break
                try:
                    #log a debug message
                    articleurl = t['url']
                    articletitle = t['title']

                    html = urllib.request.urlopen(articleurl).read()
                    #print(articleurl)
                    totals = algo.phraseFreq(myhtml.text_from_html(html))
                    #log a debug message for totals
                    c_data.add_article([articletitle, articleurl, totals])
                    print(totals)
                except:
                    print("Unexpected error:", sys.exc_info())
                    #traceback.print_exc(file=sys.stdout)
                    #there is a logger.exception where you can pass an exception

            print(c_data.get_name())
            print(c_data.get_total())
            print(c_data.get_trend())
            print(c_data.get_num_articles())

        algo.PhraseMgr.reset()
        return self.companieslist



