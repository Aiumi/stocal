class company_data():
    
    def __init__(self, name):
        
        self.name = name
        self.articles = list()
        #Articles list is a 3 tuple where the first value is the headline, the second value is the url, the third value is the score. 
        
    def get_name(self):
        
        return self.name
    
    def get_trend(self):
        
        decision = 'Neutral'
        accum = self.get_total()
        if accum[0] + accum[1] >= 50:
            decision = 'Trending Upwards'
        elif accum[0] + accum[1] <= -50:
            decision = 'Trending Downwards'
        return decision
    
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
