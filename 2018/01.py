#!/usr/bin/python


iSeenIt = {0: True}
def processInput(fileName):
    result = 0
    done = False
    while done == False:
        result, done = iterateFile(fileName, result)
    return result

def iterateFile(filename, result):
    with open(filename) as f:
        for line in f:
            result += int(line.strip())
            if result in iSeenIt:
                return (result, True)
            else:
                iSeenIt[result] = True
            
    return (result, False)

if __name__ == "__main__":
    import sys
    result = processInput(sys.argv[1])
    print result
    
