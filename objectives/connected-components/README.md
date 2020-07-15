# Connected Components in a Graph

A _connected component_ of a graph is a subgraph where all vertices are
reachable via edges in the subgraph.

Here's an example of a graph with 8 connected components:

![Connected Components](img/connected-components.png)

(Two of the connected components are single verts.)

## Usefulness of Connected Components

There are a lot of theoretical uses of connected components that are beyond the scope of the course. But on the more practical front, here are some potential uses:

* Look for people you might know in a social network.
* Predict the spread of zombie apocalypse or other disease within social groups.
* Determining which parts of a computer network are reachable from another.
* Finding clusters of related information.

## Finding Connected Components

If you have a BFS or DFS, finding connected components is pretty
straightforward if you modify your search to return a list of verts
visited. (Also modify the search to not always color the verts white at
the start.)

```pseudocode
connected_components = [];

for v in graph.vertexes:
  v.color = white

for v in graph.vertexes:
  if v.color == white:
    component = bfs(v)
	connected_components.push(component);
```

## Exercises

Draw a graph of 8 vertexes with 3 connected components.

### My notes from CS29 Beej Jorgensen
parts of the graph that are connected but disjoint from other parts of the graph.
....assume for examples using undirected graphs

For each node:
    if node not visited:
    traverse from that node
    increment counter

Graph:       
    nodes = [1,2,3,4,5] ## using array
    edges: [(1,2), (2,3),(3,4),(4,5)]

counter = 3

Graph: 
    nodes = [(1,(2)),2,(3,(4,6),4,5] ## using adjacency list
    edges: [(1,2), (2,3),(3,4),(4,5)]


## questions
difference between linked list and array