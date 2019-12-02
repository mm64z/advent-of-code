#!/usr/bin/python

def processInput(fileName):
    result = 0
    with open(fileName) as f:
        for line in f:
            result = line.strip()
    return result


def compare(char1, char2):
    if abs(ord(char1) - ord(char2)) == 32: # diff between capital and lower
        return True
    else:
        return False

def calculateResult(formattedInput):
    import string
    minCount = len(formattedInput)
    for letter in string.ascii_lowercase:
        bigString = formattedInput.replace(letter, "")
        bigString = bigString.replace(chr(ord(letter)-32), "")
        #print bigString
        count = calculateResultSub(bigString)
        #print letter
        #print count
        if count < minCount:
            minCount = count

    return minCount
    
    
def calculateResultSub(formattedInput):
    change = True
    bigString = formattedInput
    while change:
        change = False
        #print change
        try:
            for i in range(1, len(bigString)):
                #print bigString[i] + bigString[i-1]
                if compare(bigString[i], bigString[i-1]):
                    #print "removed"
                    change = True
                    bigString = bigString[:i-1] + bigString[i+1:]
        except IndexError:
            continue
    
    return len(bigString)

if __name__ == "__main__":
    import sys
    formattedInput = processInput(sys.argv[1])
    result = calculateResult(formattedInput)
    print result
    
