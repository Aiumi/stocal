import re
from pathlib import Path

pNameregex = ''
cpNameregex = re.compile('')
pPuncregex = ''
cpPuncregex = re.compile('')

textroot = Path('static/data/')
file = textroot / 'unwantedregex.txt'
with open(file, 'rt') as file:
    r = file.readlines()
    rlen = len(r)
    punc = r[0]
    patt = '(.*)('
    for n in range(1, rlen):
        patt = patt + '(' + r[n].strip() + ')|'
    pattlen = len(patt)
    patt = patt[0:pattlen - 1] + ')\\s*(.*)'
print('(.*)((Company)|(Corporation)|(Incorporated)|(Technologies)|(Limited)|(Holdings)|(Group)|(Inc)|(Ltd)|(com)|(The))\\s*(.*)')
print(patt)