# understand

# plan
# graphs problem solving
# translate the problem
## nodes: people
# edges: when a child has a parent

# build our graph, or just define get_neighbors
##

# choose algorithm
# either dfs or bfs

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex not in self.vertices:
            self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]


graph = Graph()


def build_graph(ancestors):
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph

    graph.add_vertex(parent)


def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()

    visited = set()

    s.push([starting_node])

    longest_path = []
    aged_one = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        if len(path) > len(longest_path) or (len(path) == len(longest_path) and current_node < aged_one):
            longest_path = path
            aged_one = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)

    return longest_path[-1]
