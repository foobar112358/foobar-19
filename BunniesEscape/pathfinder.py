def answer(maze):
    # Calculate the length without subtracting a wall:
    baseLen = solveMaze(maze)

    # If it's not already optimal, then check other paths:


def solveMaze(maze):
    dim = len(maze)
    # Create shadow copy of maze:
    visited = [[0]*dim for _ in range(len)]
    # We know that [0][0] is empty, so add the directions right and down to the stack:
    movesToCheck = []
    pos = [0,0]
    addMovesToCheck(maze, pos, movesToCheck)

    while len(movesToCheck) > 0:
        pos = movesToCheck[-1][0]
        del movesToCheck[-1][0]
        if len(movesToCheck[-1]) == 0:
            del movesToCheck[-1]
        if pos == 0 and visited[pos[0], pos[1]] == 0:
            visited[pos[0], pos[1]] = 1
            addMovesToCheck(maze, pos, movesToCheck)

# Push an empty list on the end and then add each viable direction:
def addMovesToCheck(maze, pos, moves):
    dim = len(maze)
    moves.append([])
    if pos[0]+1 < dim:
        moves[-1].append([pos[0]+1, pos[1]])
    if pos[1]+1 < dim:
        moves[-1].append(pos[0], pos[1]+1)
    if pos[0] >= 1:
        moves[-1].append(pos[0]-1, pos[1])
    if pos[1] >= 1:
        moves[-1].append(pos[0], pos[1]-1)