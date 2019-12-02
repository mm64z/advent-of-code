#!/usr/bin/python

def processInput(fileName):
    result = []
    maxX = 0
    maxY = 0
    i = 0
    with open(fileName) as f:
        for line in f:
            points = line.strip().split(', ')
            x = int(points[0])
            y = int(points[1])
            if x > maxX:
                maxX = x
            if y > maxY:
                maxY = y
            result.append([x, y, i])
            i += 1
            
    return result, maxX, maxY

# input is [x, y, i]
def calculateResult(formattedInput, maxX, maxY):
    closestPoints = []
    disqualified = []
    for i in range(maxX+2):
        if i % 50 == 0:
            print i
        for j in range(maxY+2):
            #print "j " + str(j)
            closest = []
            closestDistance = 9999
            for point in formattedInput:
                diff = abs(point[0] - i) + abs(point[1] - j)
                
                #print diff, closestDistance
                if diff < closestDistance:
                    #print "making new"
                    closestDistance = diff
                    closest = [point[2]]
                elif diff == closestDistance:
                    closest.append(point[2])
            closestPoints.append(closest)


            if (i == 0 or i == maxX+1 or \
               j == 0 or j == maxY+1) and len(closest) == 1:
                #print closest
                for point in closest:
                    if point not in disqualified:
                        disqualified.append(point)

    #print closestPoints
    # {i -> count)
    counts = {}
    for square in closestPoints:
        if len(square) == 1:
            if square[0] in counts:
                counts[square[0]] += 1
            else:
                counts[square[0]] = 1
            

    # find max, not counting disqualified
    maxCount = 0
    for point in counts:
        if point not in disqualified:
            if counts[point] > maxCount:
                maxCount =  counts[point]
    
    return maxCount

def calculateResult2(formattedInput, maxX, maxY):
    maxDistance = 10000
    validCount = 0
    for i in range(maxX+2):
        if i % 50 == 0:
            print i
        for j in range(maxY+2):
            sumDistance = 0
            for point in formattedInput:
                sumDistance += abs(point[0] - i) + abs(point[1] - j)
            if sumDistance < maxDistance:
                validCount += 1
    return validCount

if __name__ == "__main__":
    import sys
    formattedInput, maxX, maxY = processInput(sys.argv[1])
    result = calculateResult2(formattedInput, maxX, maxY)
    print result
    
