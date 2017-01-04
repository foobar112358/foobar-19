from collections import defaultdict

def actualAnswer(l):
    l = sorted(l)
    count = 0
    # i < j < k, so i < len(l)-2, j < len(l)-1.
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            if l[j] % l[i] == 0:
                for k in range(j+1, len(l)):
                    if l[k] % l[j] == 0:
                        count = count+1
    return count

# I don't have a linear-time algorithm for this, so all I can
# do is something that's similar to dynamic programming in terms
# of building up successive pairs. So on one pass this will determine
# whether a number x divides y for all x and y, x < y. That will take
# time O(n^2) (sad trombone). Then we'll repeat this again, but this
# time the highest number of the pairs, y, will be again checked
# against all numbers in the list. That will again take time O(n^2).
def answer(l):
    if len(l) < 3:
        return 0

    # Since we're going to take time O(n^2), we may want to sort:
    l = sorted(l)

    # So for a triple (a,b,c), we will have:
    # a=b=c: a exists in dupTriples
    # a=b<c: b exists in dupPairs
    # a<b=c: b exists in distPairCounts; scan for c%b, add b to dupPairsScanned
    # a<b<c: b exists in distPairCounts; scan for c%b, c!=b

    # Get the duplicate pairs, duplicate triples (a=b=c), and, for each b,
    # count for all a such that b % a (which we jam into distPairCounts).
    dupTriples = {}
    dupPairs = {}
    elemCount = defaultdict(int)
    for i in range(len(l)):
        elemCount[l[i]] += 1
        if elemCount[l[i]] >= 2:
            dupPairs[l[i]] = 1
            if elemCount[l[i]] >= 3:
                dupTriples[l[i]] = 1

    # One triple for every duplicate triple (e.g., [1,1,1]). Count it once
    # even if the number shows up more than three times (e.g., count [1,1,1,1,1] 
    # as 1 triple).
    totalTriples = len(dupTriples)

    # Get distinct pairs; record the count for the higher number, as we can't 
    # afford to count pairs.
    distPairCounts = defaultdict(int)
    distinctNums = sorted(list(set(l)))
    for i in range(len(distinctNums)-1):
        for j in range(i+1, len(distinctNums)):
            if distinctNums[j] != distinctNums[i] and distinctNums[j] % distinctNums[i] == 0:
                distPairCounts[distinctNums[j]] += 1

    # Count the pairs: a<b=c and a=b<c.
    # Then count the distinct triples: a<b<c
    for i in range(len(distinctNums)):
        for dp in dupPairs:
            if distinctNums[i] != dp:
                if distinctNums[i] % dp == 0:
                    totalTriples += 1
                elif dp % distinctNums[i] == 0:
                    totalTriples += 1
        
        for d in distPairCounts:
            if distinctNums[i] > d and distinctNums[i] % d == 0:
                totalTriples += distPairCounts[d]

    return totalTriples

def check(l):
    a = answer(l)
    b = actualAnswer(l)
    if a != b:
        print "Got %d for answer, which should be %d for %s" % (a,b,l)
    else:
        print "%d: %s" % (a,l)
    
#check([1,1,1])        # Should be 1
#check([1,2,3,4,5,6])  # Should be 3
#check([1,1,1,2,2,2])  # Should be 4
#check([1,1,1,1,2])    # Should be 2
#check([1,2,3,4,6,9,12,16,18,24,27,32,36])  # ???
#check([1,3,5])
#check([1,2])
#check([1,2,4,8])  # 4
check([1,1,1,2,4,8])    # 8: 1,1,1  1,1,2  1,1,4  1,1,8  1,2,4  1,2,8  1,4,8  2,4,8
check([1,1,1,2,2,2,3,3,3,4])  # 10: 1,1,1  2,2,2  3,3,3  1,1,2  1,2,2  1,1,3  1,3,3  1,1,4  1,2,4  2,2,4
check([1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2])  # Should be 4: 1,1,1  1,1,2  1,2,2  2,2,2
#print answer([1,2,3,3,4,5,6]) # Should be 4
#print answer([1,2,3,3,3,4,5,6]) # Should be 5

#for i in range(10):
#    randDict = {}
#    randList = []
#    for j in range(50):
#        k = random.randrange(2,100)
#        if k not in randDict:
#            randDict[k] = 1
#            randList.append(k)

#    a = answer(randList)
#    b = actualAnswer(randList)
#    if a != b:
#        print "Failed on list %s: %d actual, got %d" % (randList, b, a)

print "done"