from collections import defaultdict

# To print all words from a dictionary that can be found on a Boggle board, you typically use depth-first search (DFS) combined with backtracking.
# First, you construct a trie (prefix tree) from the dictionary words for efficient prefix matching during the search.
# Then, you traverse the Boggle board, exploring all possible paths to form valid words.


# TrieNode class for Trie construction
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False


# Trie class
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the trie
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True


# Boggle board search function
def boggle_search(board, trie):
    def dfs(i, j, node, prefix):
        if node.is_end_of_word:
            found_words.add(prefix)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        char = board[i][j]
        if char not in node.children:
            return
        temp, board[i][j] = board[i][j], '#'
        next_node = node.children[char]
        for dx, dy in directions:
            dfs(i + dx, j + dy, next_node, prefix + char)
        board[i][j] = temp

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    found_words = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, trie.root, "")
    return found_words


if __name__ == "__main__":

    # Example usage
    dictionary = ["apple", "banana", "peach", "pear", "pin", "pine", "applepin"]
    boggle_board = [
        ['a', 'p', 'e', 'x'],
        ['p', 'i', 'p', 'n'],
        ['l', 'n', 'e', 'n'],
        ['a', 'b', 'c', 'd']
    ]

    # Construct trie from dictionary
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    # Search for words on the Boggle board
    found_words = boggle_search(boggle_board, trie)
    print(found_words)  # Output: {'pin', 'pine'}
