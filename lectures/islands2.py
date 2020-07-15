# plan
# iterate through the matrix
# when we see a 1, if it's not been visited
# increment our islands counter
# run a traversal
# mark things as visited

def get_neighbors():
    pass


def dft_recursive(node, visited, matrix):
    if node not in visited:
        visited.add(node)

        neighbors = get_neighbors(node, matrix)
        for neighbor in neighbors:
            dft_recursive(neighbor, visited, matrix)
            print(neighbor, visited, matrix)


def islands_counter(isles):
    visited = set()
    number_islands = 0

    for row in range(len(isles)):
        for col in range(len(isles[row])):
            node = (row, col)
            if node not in visited and isles[row][col] == 1:
                number_islands += 1
                dft_recursive(node)

    return number_islands
