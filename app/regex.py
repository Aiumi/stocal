import re

companies = ['Microsoft Corporation',
             'Amazon.com, Inc.',
             'Uber Technologies, Inc.',
             'Walt Disney Company (The)',
             'The Small Consulting Group, Incorporated',
             'A.B;C,D:E.F;G,H:Inc.']

punc = re.compile('(.*)[\\.,:;\\(\\)](.*)')
p = re.compile('(.*)((Company)|(Corporation)|(Incorporated)|(Technologies)|(Limited)|(Holdings)|(Group)|(Inc)|(Ltd)|(com)|(The))\\s*(.*)', re.IGNORECASE)
for c in companies:
    m = punc.match(c)
    while m is not None:
        c = m.group(1).strip() + ' ' + m.group(2).strip()
        m = punc.match(c)
    #print('***' + c + '***')
    m = p.match(c)
    while m:
        l = len(m.groups())
        s = m.group(1).strip() + ' ' + m.group(l)
        s = s.strip()
        m = p.match(s)
    print('')
    print('>>>' + s + '<<<')
    