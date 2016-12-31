import math

def answer(area):
    squares = []
    while (area > 0):
        largestSquareEdge = int(math.floor(math.sqrt(area)))
        squares.append(largestSquareEdge)
        area = area - largestSquareEdge * largestSquareEdge
    
    return squares