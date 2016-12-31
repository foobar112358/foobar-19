def answer(l,t):
    start=0
    end=0
    sum=l[0]

    while(1):
        if (sum == t):
            return [start, end]
        elif (sum > t):
            sum = sum - l[start]
            start = start+1
            # Edge case: sitting on one element that exceeds t:
            if (end < start):
                end = start
                sum = l[start]

        else: # sum < t
            end = end+1
            if (end >= len(l)):
                return [-1,-1]
            sum = sum + l[end]
    
    # Didn't find it, hit some weird edge case, so return an error:
    return [-1,-1]

l = answer([4,3,5,7,8], 12)
l = answer([4,3,10,2,8], 12)
l = answer([1,2,3,4], 15)
l = answer([2,3,4,5], 1)