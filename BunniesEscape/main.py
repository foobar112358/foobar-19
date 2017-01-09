import math

def answer(maze):
    # Generate graph for base maze and calculate length:
    minLen = solveMaze(maze)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                maze[i][j] = 0
                minLen = min(minLen, solveMaze(maze))
                maze[i][j] = 1
    
    if math.isinf(minLen):
        return -1
    else:
        return minLen

def solveMaze(maze):
    h = len(maze)
    w = len(maze[0])
    # Initialize 2d matrix to infinity except for starting point at 0,0:
    dist = [[float('inf')]*w for _ in range(h)]
    dist[0][0] = 1

    # Nothing has been visited except the start
    visited = [[False]*w for _ in range(h)]
    visited[0][0] = True
    # Build a queue of points that need checking. 
    q = [ [y, x] for x in range(w) for y in range(h) ]

    # While (we have visitable nodes in the queue):
    # - check the nodes above, to the right, below, and to the left, in that order
    # - maze walls count as having infinite distance
    # - if we 
    while True:
        # Reduce isn't working, so bail for now. I need to level up my Python kung fu...
        #minVertex = reduce((lambda x,y: if dist[x] < dist[y]{ return x } else{ return y }), q)
        v = [-1,-1]
        qIndex = -1  # Used for making deletion a bit snappier
        minQDist = float('inf')
        for i in range(len(q)):
            nextV = q[i]
            if dist[nextV[0]][nextV[1]] < minQDist:
                v = nextV
                minQDist = dist[v[0]][v[1]]
                qIndex = i
        
        if math.isinf(minQDist):
            return dist[h-1][w-1]

        minTentDist = float('inf')
        minTentDist = min(minTentDist, checkPos(v, [v[0], v[1]-1], maze, dist))
        minTentDist = min(minTentDist, checkPos(v, [v[0]+1, v[1]], maze, dist))
        minTentDist = min(minTentDist, checkPos(v, [v[0], v[1]+1], maze, dist))
        minTentDist = min(minTentDist, checkPos(v, [v[0]-1, v[1]], maze, dist))
        del q[qIndex]

            
def checkPos(currVert, nextVert, maze, dist):
    # Out of bounds: ignore it
    if nextVert[0] < 0 or nextVert[0] >= len(maze) or nextVert[1] < 0 or nextVert[1] >= len(maze[0]):
        return float('inf')

    # It's a wall: ignore it:
    if maze[nextVert[0]][nextVert[1]] == 1:
        return float('inf')

    # We can get to it, so compare current distance with the distance to current vertex + 1:
    distViaCurr = dist[currVert[0]][currVert[1]]+1
    distToNext = dist[nextVert[0]][nextVert[1]]
    if distViaCurr < distToNext:
        dist[nextVert[0]][nextVert[1]] = distViaCurr

    return dist[nextVert[0]][nextVert[1]]



print answer([[0, 0, 1], [1, 0, 1]])
print answer([[0, 0], [1, 0], [1, 0]])
print answer([[0, 0, 1], [1, 0, 1], [1, 0, 0]])
print answer([[0, 0, 1], [1, 1, 1], [1, 0, 0]])
print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])