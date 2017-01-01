import random

def naiveAnswer(start, length):
    # Let's keep it big and dumb for now: do the O(length^2) algorithm
    # that just xors one at a time.
    xor = 0
    # For (every queue):
    #   - get the queue length and the start of the queue
    #   - xor in everything in that queue
    for i in range(length):
        qlen = length - i
        qstart = start + i*length
        for j in range(qlen):
            xor = xor ^ qstart + j
    
    return xor

def answer(start, length):
    xor = 0
    # Yeah, I'm not bitmasking here. Wompwomp.
    # We always end up with a matching number of 1s every other row
    # except if:
    #  - we start with an even number and have 4k+2 length, giving 2k+1 1s
    #  - we start with an odd number and have 4k+1 length, giving 2k+1 1s
    # In those cases we just set this to 1:
    # (Note: we're doing this because the algorithm following this will fail
    # for the lsb.)
    if (start % 2 == 0 and length % 4 == 2):
        xor = 1
    elif (start % 2 == 1 and length % 4 == 1):
        xor = 1
    
    # For every queue:
    # - for every bit position:
    #   - The bit position will determine how many ids, when masked by 
    #     the bits to the right of the current position, need to be counted. 
    #   - Count the stragglers at the beginning and end. 
    #   - Ignore anything in between.
    for i in range(length):
        qlen = length - i
        qstart = start + i*length
        qend = qstart + qlen - 1
        for bitpos in range(1, numbits(qend)):
            currPosMask = 1 << bitpos          # Bit 2, this would be 100
            nextPosBitmask = currPosMask << 1  # Bit 2, this would be 1000
            fullBitmask = nextPosBitmask - 1  # Bit 2, this would be 111
            qstartOffset = qstart & fullBitmask  # Start with 1101, bit 2, this would be 101
            qstartCount = 0
            # Need to count from the next bit position if this starts with 1:
            if (qstart & currPosMask == 1):
                qstartCount = nextPosBitmask - qstartOffset
            # Need to count from current bit position if this starts with 0:
            else:
                qstartCount = currPosMask - qstartOffset

            # If the offset bit is 1, then we'll want to xor it in qstartCount times.
            # So just look at the last bit for qstartCount.
            xor = xor ^ ((qstart & currPosMask) * (qstartCount & 0b1))

            # Repeat for the end:
            if (qstartCount < qlen):
                qendCount = (qend & fullBitmask >> 1) + 1   # Ends with 10001, bit 2, this would be 2
                xor = xor ^ ((qend & currPosMask) * (qendCount & 0b1))

    return xor

def numbits(n):
    if (n == 0):
        return 0
    
    count = 0
    while (n > 0):
        n = n >> 1
        count = count+1
    
    return count

print answer(0, 3)
print answer(17, 4)

for i in range(10):
    start = random.randrange(32, 128)
    length = random.randrange(3, 10)
    shouldBe = naiveAnswer(start, length)
    callWeGot = answer(start, length)
    if (shouldBe != callWeGot):
        print "Mismatch for start=%d, length=%d; should be %d, got %d" % (start, length, shouldBe, callWeGot)

print "done"
