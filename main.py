### main.py
from ternary_tree import TernarySearchTree
from file_loader import load_words

def main():
    tree = TernarySearchTree()

    insert_words = load_words("data/search_trees/insert_words.txt")
    not_insert_words = load_words("data/search_trees/not_insert_words.txt")

    for word in insert_words:
        tree.insert(word)

    print("\n✅ Inserted Words - Search Results:")
    for word in insert_words:
        print(f"{word}: {'Found' if tree.search(word) else 'Not Found'}")

    print("\n❌ Not Inserted Words - Search Results:")
    for word in not_insert_words:
        print(f"{word}: {'Found' if tree.search(word) else 'Not Found'}")

if __name__ == "__main__":
    main()