#!/usr/bin/python

def processInput(fileName):
    result = {}
    allSteps = []
    with open(fileName) as f:
        for line in f:
            parts = line.split(" ")
            if parts[7] in result:
                result[parts[7]].append(parts[1])
            else:
                result[parts[7]] = [parts[1]]
            if parts[1] not in allSteps:
                allSteps.append(parts[1])
            if parts[7] not in allSteps:
                allSteps.append(parts[7])
                

    # {step -> prereqs}
    return result, allSteps


def calculateResult(formattedInput, allSteps):
    sortedInput = sorted(allSteps)
    print sortedInput
    completionOrder = []
    while len(sortedInput) > 0:
        for entry in sortedInput:
            if entry not in formattedInput:
                sortedInput.remove(entry)
                completionOrder.append(entry)
                break
            else:
                ableToDo = True
                for prereq in formattedInput[entry]:
                    if prereq not in completionOrder:
                        ableToDo = False
                if ableToDo:
                    sortedInput.remove(entry)
                    completionOrder.append(entry)
                    break

    return "".join(completionOrder)

if __name__ == "__main__":
    import sys
    formattedInput, allSteps = processInput(sys.argv[1])
    result = calculateResult(formattedInput, allSteps)
    print result
    
