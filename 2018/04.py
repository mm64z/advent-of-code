#!/usr/bin/python

def processInput(fileName):
    import re
    result = []
    with open(fileName) as f:
        for line in f:
            result.append(line.strip())
    
    result.sort()
    
    lastGuardSeen = -1
    sequenceMatch = re.compile(r'\d{2}:(\d{2})\] [^ ]* ([^ ]*)')
    startTime = 0
    guardSleep = {} # guard -> [[start, end]]
    for entry in result:
        regexResult = sequenceMatch.search(entry)
        decider = regexResult.group(2)
        if decider[0] == '#':
            lastGuardSeen = int(decider[1:])
        elif decider == 'asleep':
            startTime = int(regexResult.group(1))
        elif decider == 'up':
            endTime = int(regexResult.group(1))
            guardSleep = addGuardTime(guardSleep, lastGuardSeen, startTime, endTime)
    #print guardSleep
    return guardSleep
        
def addGuardTime(guardSleep, guardNum, startTime, endTime):
    if guardNum in guardSleep:
        guardSleep[guardNum].append([startTime, endTime])
    else:
        guardSleep[guardNum] = [[startTime, endTime]]
    return guardSleep


def calculateResult(formattedInput):
    guardSleep = formattedInput # guard -> [[start, end]]
    guardTime = {} # guard -> time
    #print guardSleep
    for entry in guardSleep:
        for timePair in guardSleep[entry]:
            try:
                guardTime[entry] += timePair[1] - timePair[0]
            except KeyError:
                guardTime[entry] = timePair[1] - timePair[0]

    maxSleep = 0
    sleepiestGuard = 0
    for entry in guardTime:
        if guardTime[entry] > maxSleep:
            maxSleep = guardTime[entry]
            sleepiestGuard = entry

    maxSleepMinute = 0
    maxSleepIndex = 0
    maxSleepGuard = 0
    for guard in guardSleep:  #part B
        sleepTime = [0]*60
        for entry in guardSleep[guard]:
            for i in range(entry[0], entry[1]):
                sleepTime[i] += 1
                if (sleepTime[i] > maxSleepMinute):
                    maxSleepMinute = sleepTime[i]
                    maxSleepIndex = i
                    maxSleepGuard = guard

    print maxSleepGuard
    print maxSleepIndex
    return maxSleepGuard*maxSleepIndex

if __name__ == "__main__":
    import sys
    formattedInput = processInput(sys.argv[1])
    result = calculateResult(formattedInput)
    print result
    
