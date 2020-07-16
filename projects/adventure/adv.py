from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack

# Load world
world = World()

# 500 rooms
# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# My code starts here

# create function to backtrack


def reversePath(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"

# move through rooms


def traverseRooms(starting_room):
    stack = Stack()  # DF
    visited = set()
    # identify where player is starting from
    starting_room = player.current_room
    # iterate through exits
    # loop through until all room visited
    while len(visited) < len(world.rooms):
        # create a path list to record path travelled
        path = []
        for room_exit in player.current_room.get_exits():
            # if an exit exists
            if room_exit is not None:
                if player.current_room.get_room_in_direction(room_exit) not in visited:
                    # append room_exit if not already visited
                    path.append(room_exit)
                    print('path', path)
        # if exit has not been visited, travel to that exit
        visited.add(player.current_room)

        if len(path) != 0:
            # generate random movement
            # randint() has (start, end) values so go one less than path or goes out of range
            move = random.randint(0, len(path) - 1)
            stack.push(path[move])
            # move from one room to the next
            player.travel(path[move])
            # add to travel_path
            traversal_path.append(path[move])

        else:
            # return last from stack
            last = stack.pop()
            # backtrack
            player.travel(reversePath(last))
            # add to travel_path
            traversal_path.append(reversePath(last))


# call the function starting at 0
traverseRooms(0)

# TRAVERSAL TEST - DO NOT CHANGE
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

# my additions from readme
# player.current_room.id
# player.current_room.get_exits()
# player.travel(directions)
