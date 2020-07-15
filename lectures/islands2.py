"""
Write a function that takes a 2D binary array and returns the number of 1 islands. 
An island consists of 1s that are connected to the north, south, east or west. For example:

island_counter(islands) # returns 4

Describe the problem in terms of graphs
nodes: 1s
edge: connected n/s/w/e

islands: connected components

Build our graph or just define getNeighbors()


visited = set((0, 1))


Plan
## Iterate through the matrix
### When we see a 1, if it's not been visited
#### Increment our islands counter
#### run a traversal
##### mark things as visited

"""

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0]]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
               [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
               [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# stepNorth = row > 0


def get_neighbors(node, matrix):
    row, col = node
    neighbors = []

    stepNorth = stepSouth = stepWest = stepEast = False
    # take a step north
    if row > 0:
        stepNorth = row - 1
    # take a step south
    print('length of matrix', len(matrix))
    if row < len(matrix) - 1:
        stepSouth = row + 1
    # take a step east
    print('length of matrix[row]', len(matrix[row]))
    if col < len(matrix[row]) - 1:
        stepEast = col + 1
    # take a step west
    if col > 0:
        stepWest = col - 1

    if stepNorth is not False and matrix[stepNorth][col] == 1:
        neighbors.append((stepSouth, col))
    if stepSouth is not False and matrix[stepSouth][col] == 1:
        neighbors.append((stepSouth, col))
    if stepEast is not False and matrix[row][stepEast] == 1:
        neighbors.append((row, stepEast))
    if stepWest is not False and matrix[row][stepWest] == 1:
        neighbors.append((row, stepWest))

    return neighbors


def dft_recursive(node, visited, matrix):
    if node not in visited:
        visited.add(node)

        neighbors = get_neighbors(node, matrix)
        for neighbor in neighbors:
            print(neighbor, visited, matrix)
            dft_recursive(neighbor, visited, matrix)


def islands_counter(isles):
    visited = set()
    number_islands = 0

    for row in range(len(isles)):
        for col in range(len(isles[row])):
            print('isles in islands_counter fn', isles)
            node = (row, col)
            if node not in visited and isles[row][col] == 1:
                number_islands += 1
                dft_recursive(node, visited, isles)

    return number_islands


print(islands_counter(islands))
