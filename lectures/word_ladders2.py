import string


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


word_set = set()

with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip()
        word_set.add(line.lower())

# print('ivy' in word_set)
# print('797dsfs' in word_set)

letters = list(string.ascii_lowercase)
# (same as letters= ['a','b','c'....])

# this doesn't actually use a graph, but works with just the get_neighbors function (adjacency list)


def get_neighbors(word):
    neighbors = []

    word_letters = list(word)
    # for each letter in the word
    for i in range(len(word_letters)):
        # replace with all english letters
        for letter in letters:
            # copy the word letters
            t = list(word_letters)
            t[i] = letter

            w = "".join(t)
            # see if we form a word
            if w != word and w in word_set:
                neighbors.append(w)
        # if we do, add it to the neighbors list

    return neighbors

# BFS is the find_word_ladders function - finding the shortest path


def find_word_ladders(begin_word, end_word):
    visited = set()

    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        cur_word = path[-1]  # get last node out of the path

        if cur_word not in visited:
            visited.add(cur_word)

            if cur_word == end_word:
                return path

            for neighbor in get_neighbors(cur_word):
                path_copy = list(path)  # copy the list so far
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None


print(find_word_ladders('mood', 'milk'))
print(find_word_ladders('zebra', 'milk'))
