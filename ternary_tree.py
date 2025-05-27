
### ternary_tree.py
class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False

class TernarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, word):
        if word:
            if not self.search(word):  # Only increment if word wasn't already there
                self._size += 1
            self.root = self._insert(self.root, word, 0)

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
                node.is_end = True
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

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
                return node.is_end
            return self._search(node.eq, word, index + 1)

    def starts_with_prefix(self, prefix):
        node = self._get_prefix_node(self.root, prefix, 0)
        results = []
        if node:
            if node.is_end:
                results.append(prefix)
            self._collect(node.eq, prefix, results)
        return results

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

    def get_all_words(self):
        results = []
        self._collect(self.root, "", results)
        return results

    def _collect(self, node, prefix, results):
        if not node:
            return
        self._collect(node.left, prefix, results)
        if node.is_end:
            results.append(prefix + node.char)
        self._collect(node.eq, prefix + node.char, results)
        self._collect(node.right, prefix, results)

    def size(self):
        return self._size

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
