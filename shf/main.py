from dmsec import DMSec
from dmnews import DMNews
from dmtwitter import DMTwitter
import time
import sys

class Main:
    
    def __init__(self):
        
        pass
    
    def main(self):
        
        #sys.stdout = open('output.txt', 'w')
        
        companies = [
                    'apple',
                    'facebook',
                    'google',
                    'microsoft',
                    'tesla'
        ]
        
        start = time.time()

        objSec = DMSec()
        objNews = DMNews()
        objTwitter = DMTwitter()
        
        #objSec.read()
        #objNews.read()
        #objTwitter.read()
        
        #print(objSec.totals)
        #print(objNews.totals)
        #print(objTwitter.totals)
        
        objSec.read()
        objNews.read()
        
        print(objSec.companyMap)
        print(objNews.companyMap)
        for company in companies:
            culm = [0, 0]
            
            '''companyMap = objNews.companyMap
            if company in companyMap:
                print(company + str(companyMap[company]))
            else:
                print('No results for ' + company)'''
            if company in objSec.companyMap:
                weight = objSec.getWeight()
                totals = objSec.companyMap[company]
                culm[0] += totals[0]
                culm[1] += totals[1]
            else:
                print('No SEC results for ' + company)
            if company in objNews.companyMap:
                weight = objNews.getWeight()
                totals = objNews.companyMap[company]
                culm[0] += totals[0]
                culm[1] += totals[1]
            else:
                print('No NEWS results for ' + company)
            
            print('* ' + company + ' Totals: ' + str(culm))       
        
        end = time.time()
        print(end - start)
        
stdout_orig = sys.stdout
        
obj = Main()

sys.stdout = stdout_orig

obj.main()
