from dmsuper import DMSuper
from algo import phraseFreq
import edgar

class DMSec(DMSuper):
    
    def __init__(self):
        
        self.companyMap = dict()
        
    def getName(self, param:str) -> str:

        strArray = param.split()
        result = strArray[0].lower()
        return result
    
    def getWeight(self):
        
        return .6
    
    def read(self):
    
        #edgar = edgar.Edgar()
        #print(edgar.getCikByCompanyName("APPLE INC"))
        companies = [
                    ('APPLE INC.', '0000320193'),
                    ('GOOGLE INC.', '0001288776')
        ]
        
        for c in companies:
            culm = [0, 0]
            strArray = c[0].split()
            name = self.getName(c[0])
            company = edgar.Company(c[0], c[1])
            tree = company.getAllFilings(filingType = '8-K')
            docs = edgar.getDocuments(tree, noOfDocuments = 5)
            for doc in docs:
                #print('***' + str(c) + '***')
                totals = phraseFreq(doc)
                culm[0] += totals[0]
                culm[1] += totals[1]
            print('SEC: ' + str(c) + ' Totals: ' + str(culm))
            decision = 'Hold'
            if culm[0] + culm[1] >= 6:
                decision = 'Buy'
            elif culm[0] + culm[1] <= -6:
                decision = 'Sell'
            #print(str(c) + ': ' + decision)
            self.companyMap[name] = culm

