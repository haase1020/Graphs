
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


my_file = open('words.txt', 'r')
words = my_file.read().split("\n")
my_file.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(start_word):
    neighbors = []
# for every letter in the word,
    for letter_index in range(len(start_word)):
        # for every letter in the alphabet
        for letter in string.ascii_lowercase:

            # turn our start word into a list, then back again
            word_list = list(start_word)
        # swap out a letter in the alphabet
            word_list[letter_index] = letter

            word = "".join(word_list)

        # if the result is in our words list, it's a neighbor!
            if word in word_set and word != start_word:
                neighbors.append(word)

    return neighbors


# BFS
def word_ladders(start_word, end_word):
    q = Queue()

    visited = set()

    q.enqueue([start_word])

    while q.size() > 0:

        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visited:
            visited.add(current_word)

            neighbors = get_neighbors(current_word)

            for neighbor in neighbors:
                path_copy = list(current_path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print(word_ladders('sail', 'boat'))
