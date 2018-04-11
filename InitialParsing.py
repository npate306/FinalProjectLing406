def parseFile():
    #positive and negative list of words
    pos = []
    neg = []
    #open file, read line by line
    with open("SampleData.txt", "r") as file:
        for line in file:
            count = 0
            posNum = 0
            negNum = 0
            word = []
            #put into positive or negative terms
            for string in line:
                count = count + 1
                if count == 3:
                    posNum = float(string)
                if count == 4:
                    negNum = float(string)
                if count == 5:
                    for c in string:
                        if c == '#':
                            break
                        word.append(c)
            string = ''.join(word)
            if posNum > 0 and posNum > negNum:
                pos.append(string)
            if negNum > 0 and negNum > posNum:
                neg.append(string)
    classifyReview(pos, neg)
def classifyReview(pos, neg) :
    #open review file
    reviewFile = open("Positive3 (2).txt", "r").read().split()
    posNum = 0
    negNum = 0
    #classify based off most common
    for string in reviewFile:
        if string in pos:
            posNum = posNum + 1
        if string in neg:
            negNum = negNum + 1
    if (posNum > negNum):
        print("Positive")
    else :
        print("Negative")
parseFile()