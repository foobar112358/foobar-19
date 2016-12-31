import math

def answer(area):
    squares = []
    while (area > 0):
        largestSquareEdge = int(math.floor(math.sqrt(area)))
        largestSquare = largestSquareEdge * largestSquareEdge
        squares.append(largestSquare)
        area = area - largestSquare
    
    return squares

list1 = answer(101)
list2 = answer(12)
