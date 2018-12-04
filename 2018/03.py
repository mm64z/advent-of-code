#!/usr/bin/python

# top left is 0,0
def processInput(fileName):
    result = 0
    BBoxes = [] # [[UL X, UL Y, LR X, LR Y]]
    maxX = 0
    maxY = 0
    with open(fileName) as f:
        for line in f:
            portions = line.strip().split(' ')
            ULX = int(portions[2].split(',')[0])
            ULY = int(portions[2].split(',')[1].strip(':'))
            LRX = int(portions[3].split('x')[0]) +  ULX - 1
            LRY = int(portions[3].split('x')[1]) +  ULY - 1

            BBoxes.append([ULX, ULY, LRX, LRY])
            if LRX > maxX:
                maxX = LRX
            if LRY > maxY:
                maxY = LRY
            
            
    return (BBoxes, maxX, maxY)

def calculateResult(formattedInput, maxX, maxY):
    seenBBox = []

    result = 0
    # check each square to see if they exist in multiple bbox
    # done this way as each square may belong to more than 2
    #   hence can't check pairwise bbox
    print formattedInput
    print maxX
    print maxY
    for x in range(maxX+1):
        if x % 50 == 0:
            print x
        for y in range(maxY+1):
            inOneBBox = False
            #print "after break"
            for bbox in formattedInput:
                #print "inner for"
                if x >= bbox[0] and x <= bbox[2] and \
                   y >= bbox[1] and y <= bbox[3]:
                    if inOneBBox:
                        result += 1
                        #print "breaking"
                        break # out of for bbox loop
                    else:
                        inOneBBox = True
    return result

def calculateResult2(formattedInput):
    # do pairwise comp, skip if contact any
    bboxes = formattedInput
    for i in range(len(bboxes)):
        touched = False
        for j in range(len(bboxes)):
            if i == j:
                continue
            if bboxTouch(bboxes[i], bboxes[j]):
                touched = True
                break
        if not touched:
            return i+1
            
                
            
def bboxTouch(bbox1, bbox2):
    if bbox1[0] <= bbox2[2] and bbox1[2] >= bbox2[0] and \
       bbox1[1] <= bbox2[3] and bbox1[3] >= bbox2[1]:
        return True
    else:
        return False
    
            
if __name__ == "__main__":
    import sys
    bboxes, maxX, maxY = processInput(sys.argv[1])
    #result = calculateResult(bboxes, maxX, maxY)
    result = calculateResult2(bboxes)
    print result
    
