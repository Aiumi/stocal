#!/usr/bin/python
from os import environ
import cgi, cgitb 
cgitb.enable()
import json
import urllib.request
import sys
import requests
from dmsuper import DMSuper
from algo import phraseFreq
from algo import PhraseMgr
from myhtml import text_from_html
import datetime

def calc(company):
    # Import modules for CGI handling 
    user_id = ''
    password = ''
    
    if 'HTTP_COOKIE' in environ:
       for cookie in map(str.strip, str.split(environ['HTTP_COOKIE'], ';')):
          (key, value ) = str.split(cookie, '=');
          if key == "UserID":
             user_id = value
    
          if key == "Password":
             password = value
    else:
        print('HTTP_COOKIE not found')
    
    print("User ID  = %s" % user_id)
    print("Password = %s" % password)
    
    eol = "\r\n"
    
    print("Set-Cookie:UserID = XYZ;" + eol)
    print("Set-Cookie:Password = XYZ123;" + eol)
    print("Set-Cookie:Expires = Tuesday, 31-Dec-2299 23:12:40 GMT;" + eol)
    print("Set-Cookie:Domain = localhost;" + eol)
    print("Set-Cookie:Path = /cookies;" + eol)
    print("Content-type:text/html" + eol + eol)
    
    form = cgi.FieldStorage() 
    
    query = form.getvalue('Company')
    
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
    if culm[0] + culm[1] >= 15:
        decision = 'Buy'
    elif culm[0] + culm[1] <= -15:
        decision = 'Sell'
    #log the decision
    
    # Import modules for CGI handling 
    
    # Create instance of FieldStorage 
    form = cgi.FieldStorage() 
    
    # Get data from fields
    first_name = form.getvalue('first_name')
    last_name  = form.getvalue('last_name')
    
    #x = int(first_name) - int(last_name)
    
    print("<html>")
    print("<head>")
    print("<title>Hello - Second CGI Program</title>")
    print("</head>")
    print("<body>")
    #print("<h2>Hello %s %s</h2>" + str(x))
    print("</body>")
    print("</html>")


