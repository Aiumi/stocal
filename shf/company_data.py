import re
from pathlib import Path

class company_data():
    
    pNameregex = ''
    cpNameregex = re.compile('')
    pPuncregex = ''
    cpPuncregex = re.compile('')
    
    def __init__(self, name):
        
        self.name = name
        self.articles = list()
        #self.get_regex_pattern()
        #Articles list is a 3 tuple where the first value is the headline, the second value is the url, the third value is the score. 
        
    def get_name(self):
        
        return self.name
    
    def get_regex_pattern(self):
        
        textroot = Path('static/data/')
        file = textroot / 'unwantedregex.txt'
        with open(file, 'rt') as file:
            r = file.readlines()
            rlen = len(r)
            pPuncregex = r[0]
            patt = '(.*)('
            for n in range(1, rlen):
                patt = patt + '(' + r[n].strip() + ')|'
            pattlen = len(patt)
            patt = patt[0:pattlen - 1] + ')\\s*(.*)'
        pNameregex = patt
        cpNameregex = re.compile(pNameregex)
        
    def get_stripped_name(self): 
        
        c = self.name
        punc = re.compile('(.*)[\\.,:;\\(\\)](.*)')
        p = re.compile('(.*)((Company)|(corporation)|(Incorporated)|(Technologies)|(Limited)|(Holdings)|(Group)|(Walt)|(Inc)|(Ltd)|(com)|(The))\\s*(.*)', re.IGNORECASE)
        m = punc.match(c)
        while m is not None:
            c = m.group(1).strip() + ' ' + m.group(2).strip()
            m = punc.match(c)
        m = p.match(c)
        while m:
            l = len(m.groups())
            s = m.group(1).strip() + ' ' + m.group(l)
            s = s.strip()
            m = p.match(s)
        return s
    
    def get_trend(self):
        
        decision = 'Neutral'
        percentage = self.get_percentage()
        if percentage == float('inf'):
            decision = 'UNKNOWN'
        elif percentage >= 0.65:
            decision = 'Trending Positively'
        elif percentage <= 0.35:
            decision = 'Trending Negatively'
        else:
            decision = 'Neutral'
                
        return decision
    
    def get_percentage(self) -> float:
        
        rval = float('inf')
        scores = self.get_total()
        total = scores[0] - scores[1]
        if total:
            rval = (scores[0] / total)
        return rval
    
    def get_percentage_as_str(self) -> str:
        
        percentage = self.get_percentage()
        if percentage == float('inf'):
            temp = 'UNKNOWN'
        else:
            iv = int(((percentage * 100) + 0.5))
            temp = str(iv)
        return temp
        
    def get_articles(self):
        
        return self.articles
    
    def add_article(self, articledata):
        
        self.articles.append(articledata)
        
    def get_total(self):
        
        totals = [0, 0]
        for a in self.articles:
            totals[0] += a[2][0]
            totals[1] += a[2][1]
        return totals
    
    def p_score(article):
        
        divisor = article[1]
        if divisor == 0:
            divisor = 0.001
        score = article[0]/divisor
        return score
        
    def get_num_articles(self) -> int:
        
        return len(self.articles)
    
    def get_headlines(self):
        
        headlines = list()
        for a in self.articles:
            headlines.append(a[0])
        return headlines
        
    def __str__(self):
        
        desc = "[company=" + self.name + ", articles="
        for a in self.articles:
            desc += '[title="' + a[0] + '", ' + "url=" + a[1] + '],'
        desc += "]"
        return desc
