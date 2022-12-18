#//for loop for creating 100000 dictionary?

def returnMaxFrequency(ar):   
    freqDict = {x:0 for x in ar}
    for val in ar:
        freqDict[val] = freqDict[val] + 1
    maxFreq = max(freqDict.values())
    return maxFreq


print(returnMaxFrequency(4000))
