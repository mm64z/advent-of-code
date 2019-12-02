#!/usr/bin/python

def processInput(fileName):
    result = []
    velocities = []
        
    sequenceMatch = re.compile(r'<(.*?)>.*<(.*?)>')
    
    with open(fileName) as f:
        for line in f:
            regexResult = sequenceMatch.search(entry)
            position = regexResult.group(1).split(", ")
            pX = int(position[0])
            pY = int(position[1])
            velocity = regexResult.group(2).split(", ")
            vX = int(velocity[0])
            vY = int(velocity[1])
            
    return result, velocities


def calculateResult(formattedInput, velocities):

    positions = formattedInput
    # TODO look for smallest bound
    
    for entry in formattedInput:

    return result

if __name__ == "__main__":
    import sys
    formattedInput, velocities = processInput(sys.argv[1])
    result = calculateResult(formattedInput, velocities)
    print result
    
