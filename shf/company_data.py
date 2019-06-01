class company_data():
    
    def __init__(self, name):
        
        self.name = str()
        self.verdict = str()
        self.score = str()
        self.articles = list()
        #Articles list is a 3 tuple where the first value is the headline, the second value is the url, the third value is the score. 
        #[headline, url, score]
        
