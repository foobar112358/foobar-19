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
    distPairs = []
    dupTriples = {}
    dupPairs = {}

    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                if l[j] == l[i]:
                    # Catch triples:
                    if (i > 0 and l[i-1] == l[i]) or (j < len(l)-1 and l[j] == l[j+1]):
                        dupTriples[l[j]] = 1
                    # Catch pairs; this will fire at least once even when there are triples.
                    else:
                        dupPairs[l[j]] = 1
                else:
                    # Add this pair exactly once: watch out for dups.
                    if (i == 0 or l[i-1] != l[i]) and (j == len(l)-1 or l[j+1] != l[j]):
                        distPairs.append([l[i], l[j]])

    # Total triples; we have one triple for every element in dupTriples (a=b=c)
    totalTriples = len(dupTriples)

    # Scanning for a<b=c and a=b<c:
    for i in range(0, len(l)):
        if i == 0 or l[i] != l[i-1]:
            for dp in dupPairs:
                if dp != l[i]:
                    if dp % l[i] == 0: 
                        totalTriples += 1
                    elif l[i] % dp == 0:
                        totalTriples += 1

    # We're checking for a<b<c. 
    # TODO: Consider reversing the loop order with some indexing (so that we can skip
    # cases where l[i] < lj).
    for i in range(2, len(l)):
        for dp in distPairs:
            if l[i] % dp[1] == 0 and l[i] != dp[0] and l[i] != dp[1]:
                totalTriples += 1

    return totalTriples

print answer([1,1,1])        # Should be 1
print answer([1,2,3,4,5,6])  # Should be 3
print answer([1,1,1,2,2,2])  # Should be 4
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