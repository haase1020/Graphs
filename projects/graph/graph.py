"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.(connected from 1 direction)
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('vertex does not exits in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)

        # keep track of visited nodes
        visited = set()

        # repeat until queue is empty
        while q.size() > 0:
            # dequeue first vert
            current_node = q.dequeue()
            # if not visited:
            if current_node not in visited:
                # mark as visited
                print('current node in bft', current_node)
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)
                    print('current node in bft again', current_node)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our stack isn't empty
        while s.size() > 0:
            # pop off whatever's on top, this is current_node
            current_node = s.pop()
        # if we haven't visited this vertice before
            if current_node not in visited:
                # run function/print
                print('current node dft', current_node)
        # mark as visited
                visited.add(current_node)
        # gets its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors
                for neighbor in neighbors:
                    # add to our stack
                    s.push(neighbor)
                    print('current node dft2', current_node)
                    print('neighbors dft2', neighbors)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # mark this vertex as visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            # if it's not visited
            if neighbor not in visited:
                # recurse on the neighbor
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # make a queue
        q = Queue()
        # make a set to track nodes we've visited
        visited = set()

        path = [starting_vertex]
        q.enqueue(path)
        # while queue isn't empty
        while q.size() > 0:
            # dequeue the path at the front of the line
            current_path = q.dequeue()
            current_node = current_path[-1]
            # if this node is our target node
            if current_node == destination_vertex:
                # return it!! return TRUE
                return current_path
            # if not visited
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
            # get it's neighbors
                neighbors = self.get_neighbors(current_node)
            # for each neighbor
                for neighbor in neighbors:
                    # copy path so we don't mutate the original path for different nodes
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    # add to our queue
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # like bfs, except using a stack instead of queue
        visited = set()
        stack = Stack()

        visited.add(starting_vertex)
        # unlike dft the stack holds arrays (paths) instead of ints
        stack.push([starting_vertex])

        if starting_vertex == destination_vertex:
            return stack

        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]
            visited.add(current_node)
            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    if neighbor == destination_vertex:
                        return new_path
                    visited.add(neighbor)
                    stack.push(new_path)
        return None

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # mark our node as visited
        visited.add(vertex)
        # check if it's out target node, if so return
        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)
        # iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        # check if visited
        for neighbor in neighbors:
            if neighbor not in visited:
                # if not, recurse with a path
                result = self.dfs_recursive(
                    neighbor, destination_vertex, path + [neighbor], visited)
                # if this recursion returns a path
                if result is not None:
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
