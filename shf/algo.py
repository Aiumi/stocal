class PhraseMgr:

    listMap = dict()
    list = list()
    
    def __init__(self, p, w):
        self.phrase = p
        self.weight = w
    
    def __str__(self):
        return self.phrase + ': ' + str(self.weight) 
    
    def reset():
        PhraseMgr.listMap = dict()
        PhraseMgr.list = list()

    def getLists():
        
        textroot = 'shf\\buzzphrases\\'
        #listMap = self.listMap
        #list = self.list
        if len(PhraseMgr.listMap) > 0:
            return PhraseMgr.listMap
        
        files = [
                textroot + 'Legal.txt',
                textroot + 'Management.txt',
                textroot + 'Operating.txt',
                textroot + 'Market_Vocabulary.txt',
                textroot + 'Political.txt'
                ]
        
        for f in files:
            with open(f, 'rt') as file:
                #weight = 0.0
                
                #list = []
                for line in file:
                    line = line.strip() 
                    try:
                        if len(line) > 0 and line[0] != '#': 
                            words = line.split(' ') 
                            if len(words) == 2 and words[0] == 'w': 
                                weight = float(words[1])
                                if weight in PhraseMgr.listMap:
                                    PhraseMgr.list = PhraseMgr.listMap[weight]                                
                                else:
                                    PhraseMgr.list = list()
                                    PhraseMgr.listMap[weight] = PhraseMgr.list     
                            else:
                                 PhraseMgr.list.append(PhraseMgr(line, weight))   
                    except Exception as exc:
                        print(exc)
                        #sys.exit(1)
        return PhraseMgr.listMap

def phraseFreq(text):
    
    # every element of listOfLists is another list (specifically of PhraseMgr)
    
    listMap = PhraseMgr.getLists()
    
    countMap = {}
    
    # the curly braces define a dictionary (map)
    # example: countMap[-5.0] = count
    # a map or dictionary is a collection of key/value pairs
    # weight is the key, and count is the value
    
    for weight in listMap.keys():
        list = listMap[weight]
        length = len(list)
        weight = list[0].weight
        countMap[weight] = 0
        for x in range(length):
            count = text.count(list[x].phrase)
            #print(list[x].phrase + ': ' + str(count))
            countMap[weight] = countMap[weight] + count
    
    # the outer for loop traverses listOfLists, and the inner for loop traverses a specific list from listOfLists
    # we take the first element's weight for each list because the way it's organized, all weights within the same list are the same
    # countMap[weight] starts out at zero 
            # calculate a count for each item in the list
            # stores the sum of all counts in the map (accumulator)
    
    totalPositive = 0
    totalNegative = 0
    
    for weight in listMap:
        list = listMap[weight]
        #print(weight + 1)
        count = countMap[weight]
        total = str(weight * count)
        if weight > 0:
            totalPositive += count * weight
        else:
            totalNegative += count * weight
        #print(str(weight) + ': ' + str(countMap[weight]) + ' (' + total +')')
    
    # This function compiles the total weight for both the positive and negative phrases by multiplying the phrase frequency and its weight
    
    #print('Total Positive: ' + str(totalPositive))
    #print('Total Negative: ' + str(totalNegative))
    
    decision = 'Neutral'
    if totalPositive + totalNegative >= 50:
        decision = 'Upwards'
    elif totalPositive + totalNegative <= -50:
        decision = 'Downwards'
    
    #print(decision)
    return(totalPositive, totalNegative)

