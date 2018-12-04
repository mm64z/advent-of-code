#!/usr/bin/python

def processInput(fileName):
    result = 0
    count2 = 0
    count3 = 0
    iSeenString = []
    with open(fileName) as f:
        for line in f:
            line = line.strip()
            iSeenIt = {}

            splitLine = list(line)
            #print iSeenString
            for already in iSeenString:
                splitComp = list(already)
                diff, indices = diffLists(splitLine, splitComp)
                #print len(diff)
                if len(diff) == 1:
                    print line
                    print already
                    print diff
                    
                    return "".join(splitLine[:indices[0]] + splitLine[indices[0]+1:])
            #print line
            iSeenString.append(line)

def diffLists(a, b):
    result = []
    resultIndices = []
    for i in range(len(a)): # a and b same length
        if a[i] != b[i]:
            result.append(a[i])
            resultIndices.append(i)
    return result, resultIndices
            

            # part A
            ####################################
            # for letter in line:              #
            #     try:                         #
            #         if iSeenIt[letter]:      #
            #             iSeenIt[letter] += 1 #
            #     except KeyError:             #
            #         iSeenIt[letter] = 1      #
            # seen2 = False                    #
            # seen3 = False                    #
            # for key in iSeenIt:              #
            #     if iSeenIt[key] == 2:        #
            #         seen2 = True             #
            #     elif iSeenIt[key] == 3:      #
            #         seen3 = True             #
            # if seen2 == True:                #
            #     count2 += 1                  #
            # if seen3 == True:                #
            #     count3 += 1                  #
            ####################################
               

if __name__ == "__main__":
    import sys
    result = processInput(sys.argv[1])
    print result
    
