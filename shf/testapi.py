import requests
import json
import urllib.request
import sys

url = ('https://newsapi.org/v2/everything?'
                   'q=google&'
                   'domains=apnews.com,cnn.com,news.google.com,businessinsider.com,msnbc.com,time.com,economist.com,fortune.com,business.financialpost.com,cnbc.com,wsj.com,nytimes.com,bloomberg.com,bbc.com,reuters.com,apnews.com,ft.com&'
                   'from=01/04/2019&'
                   'sortBy=relevancy&'
                   'pageSize=100&'
                   'apiKey=bf87dc70b9af400d87207c4e23480ded')

getobj = requests.get(url)
            
#response = requests.get(url).json()
#log json_data(getobj.text)
json_data = json.loads(getobj.text)
temp = json_data['articles']
for t in temp:
    try:
        #log a debug message
        articleurl = t['url']
        print(articleurl)
    except:
        print("Unexpected error:", sys.exc_info())
