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
        q.enqueue(starting_vertex)

        # keep track of visited nodes
        visited = set()

        # repeat until queue is empty
        while q.size() > 0:
            # dequeue first vert
            current = q.dequeue()
            # if not visited:
            if current not in visited:
                print('current', current)
                # mark as visited
                visited.add(current)

                # get its neighbors. If not yet visited, but make visited and add to the queue.
                neighbors = self.get_neighbors(current)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        # push on our starting node
        # make a set to track if we'vebeen here before
        # while our stack isn't empty
        # pop off whatever's on top, this is current_node
        # if we haven't visited this vertice before
        # mark as visited
        # gets its neighbors
        # for each of the neighbors
        # add to our stack
        # similar to bft except using a stack instead of a queue
        visited = set()
        stack = Stack()

        visited.add(starting_vertex)
        stack.push(starting_vertex)

        while stack.size() > 0:
            current = stack.pop()
            visited.add(current)
            print('current for dft', current)
            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def dft_visit(vertex):
            visited.add(vertex)
            print('vertex for dft recursive', vertex)
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dft_visit(neighbor)

        dft_visit(starting_vertex)

    def dft_recursive2(self, start, visited=None):
        # this version is similar, but subtracts visited in the loop
        if visited is None:
            visited = set()
        visited.add(start)
        print('start for dft_recursive2', start)

        for next in self.get_neighbors(start) - visited:
            self.dft_recursive2(next, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # keep track of all visited nodes
        visited = set()
        # keep track of all the paths to be checked
        # the queue holds sub arrays, the paths, which is different from bft
        q = Queue()
        q.enqueue([starting_vertex])

        # return queue if starting_vertex is the destination_vertex
        if starting_vertex == destination_vertex:
            return q

        # keeps looping until all possible paths have been explored
        while q:
            print('current state of the queue: ' + str(q.queue))
            # get the head from the queue
            current_path = q.dequeue()
            # get the last node from the path
            current_vertex = current_path[-1]
            print('now checking: ' + str(current_vertex) +
                  " that has neighbors: " + str(self.get_neighbors(current_vertex)))

            if current_vertex not in visited:
                neighbors = self.get_neighbors(current_vertex)
                # go through all neighbor nodes
                # construct a new path which has the path with the neighbor appended to it
                # push the new path into the queue
                for neighbor in neighbors:
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                    # return path if the neighbor is destination_vertex
                    if neighbor == destination_vertex:
                        print('found destination_vertex: ' +
                              str(destination_vertex))
                        return new_path
                # mark node as explored
                # visited.append(current_vertex)
                visited.add(current_vertex)
        # if no path between the 2 vertices:
        return None

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

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = {starting_vertex}
        path = [starting_vertex]

        return self.dfs_visit(starting_vertex, destination_vertex, path, visited)

    def dfs_visit(self, vertex, destination_vertex, path, visited):

        print('current vertex: ' + str(vertex))

        if vertex == destination_vertex:
            print("found the destination vertex")
            return path

        neighbors = self.get_neighbors(vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                print('path for dfs_visit', path)
                visited.add(neighbor)
                result = self.dfs_visit(
                    neighbor, destination_vertex, path + [neighbor], visited)
                print('result of recursive dfs: ' + str(result))
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
    print(graph.dft_recursive2(1))

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
