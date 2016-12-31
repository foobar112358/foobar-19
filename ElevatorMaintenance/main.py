def answer(l):
    # For speed we may do some splitting here and then index the
    # resulting sorted list to the original, but I'm lazy.
    return sorted(l, cmp=elevatorCmp)

def elevatorCmp(a, b):
    verA = a.split(".")
    verB = b.split(".")
    minLen = min(len(verA), len(verB))
    for i in range(minLen):
        if verA[i] != verB[i]:
            return int(verA[i])-int(verB[i])
    
    return len(verA)-len(verB)

l = answer(["1.0", "0.12", "3.4.5", "3.4", "1.0.1"])