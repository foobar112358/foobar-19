def answer(f):
    fi = int(f)
    ops = 0
    while (fi) > 1:
        # We have an even number: adding pellets will only
        # help once we get to the
        if fi & 0b1 == 0:
            fi = fi/2
            ops = ops+1
        # So we're down to 1 mod 4. Then adding pellets and dividing
        # requires at least four ops, while subtracting and dividing
        # uses only three ops. This was found while examining 3, 5, and 7
        # as examples.
        elif fi & 0b11 == 0b01:
            fi = (fi-1)/4
            ops = ops+3
        # We have 3 mod 4. There are two cases:
        # - This is actually 3. Then we can subtract a pellet and divide by two,
        #   which is two ops.
        # - This is not 3. If this is 7, then adding one and dividing by four
        #   is a wash with the previous method. If it's anything else, it will
        #   be faster to add one and divide by four. So do that instead.
        elif fi & 0b11 == 0b11:
            if fi == 3:
                ops = ops+2
                fi = 1
            else:
                fi = (fi+1)/4
                ops = ops+3
    
    return ops

print answer(3)
print answer(4)
print answer(15)
print answer(25)
print "done"