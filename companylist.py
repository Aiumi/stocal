#from app import app
import pandas as pd
from app.models import User

#df = pd.read_csv('../data/companylist.csv', sep=',')
nasdaqURL = 'https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'
nyseURL = 'https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download'
df1 = pd.read_csv(nasdaqURL, sep=',')
df2 = pd.read_csv(nyseURL, sep=',')
dfmerge = pd.merge(df1, df2, on='Symbol')

c_dict = {}

for s in df1.values:
    c_dict.update({s[0] : s[1]})

for s in df2.values:
    c_dict.update({s[0] : s[1]})
print(c_dict)


'''frames = [df1, df2]
c_list = pd.concat(frames)
c_names = c_list["Name"].values
c_symbols = c_list["Symbol"].values'''
#print(c_names)

