### ternary_tree.py

# Node class represents each character node in the ternary search tree
class Node:
    def __init__(self, char):
        self.char = char              # The character stored in this node
        self.left = None              # Pointer to left child (characters < char)
        self.eq = None                # Pointer to middle child (next character in word)
        self.right = None             # Pointer to right child (characters > char)
        self.is_end = False           # Flag to indicate end of a valid word


# TernarySearchTree class encapsulates all tree operations
class TernarySearchTree:
    def __init__(self):
        self.root = None              # Root node of the tree
        self._size = 0                # Counter for number of unique words inserted

    # Public insert method
    def insert(self, word):
        if word:
            if not self.search(word):  # Avoid counting duplicates
                self._size += 1
            self.root = self._insert(self.root, word, 0)

    # Recursive insertion helper
    def _insert(self, node, word, index):
        char = word[index]
        if not node:
            node = Node(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.eq = self._insert(node.eq, word, index + 1)
            else:
                node.is_end = True  # Mark end of word
        return node

    # Public search method
    def search(self, word):
        return self._search(self.root, word, 0)

    # Recursive search helper
    def _search(self, node, word, index):
        if not node:
            return False
        char = word[index]

        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index + 1 == len(word):
                return node.is_end  # Word is found if this is the last character and is_end is True
            return self._search(node.eq, word, index + 1)

    # Returns list of all words that start with the given prefix
    def starts_with_prefix(self, prefix):
        node = self._get_prefix_node(self.root, prefix, 0)
        results = []
        if node:
            if node.is_end:
                results.append(prefix)
            self._collect(node.eq, prefix, results)  # Collect words beyond the prefix
        return results

    # Navigates to the node representing the end of the prefix
    def _get_prefix_node(self, node, prefix, index):
        if not node:
            return None
        char = prefix[index]
        if char < node.char:
            return self._get_prefix_node(node.left, prefix, index)
        elif char > node.char:
            return self._get_prefix_node(node.right, prefix, index)
        else:
            if index + 1 == len(prefix):
                return node
            return self._get_prefix_node(node.eq, prefix, index + 1)

    # Returns a list of all complete words stored in the tree
    def get_all_words(self):
        results = []
        self._collect(self.root, "", results)
        return results

    # Helper method to collect all words via in-order traversal
    def _collect(self, node, prefix, results):
        if not node:
            return
        self._collect(node.left, prefix, results)
        if node.is_end:
            results.append(prefix + node.char)
        self._collect(node.eq, prefix + node.char, results)
        self._collect(node.right, prefix, results)

    # Returns the number of unique words stored in the tree
    def size(self):
        return self._size

    # ASCII-style visualization of the tree (for debugging)
    def visualize(self, node=None, indent=""):
        if node is None:
            node = self.root
        if node.right:
            self.visualize(node.right, indent + "   ")
        print(indent + f"{node.char}{'*' if node.is_end else ''}")
        if node.eq:
            self.visualize(node.eq, indent + "   ")
        if node.left:
            self.visualize(node.left, indent + "   ")
