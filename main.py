
from ternary_tree import TernarySearchTree
from file_loader import load_words
from time import time

def main():
    tree = TernarySearchTree()

    insert_words = load_words("data/search_trees/insert_words.txt")
    not_insert_words = load_words("data/search_trees/not_insert_words.txt")

    # Benchmark insertion
    start_insert = time()
    for word in insert_words:
        tree.insert(word)
    end_insert = time()

    # Benchmark search
    start_search = time()
    results_found = sum(1 for word in insert_words if tree.search(word))
    end_search = time()

    # Output summary to terminal
    print(f"\n Benchmark Summary")
    print(f"Inserted {len(insert_words)} words in {end_insert - start_insert:.4f} seconds")
    print(f"Searched {len(insert_words)} words in {end_search - start_search:.4f} seconds")
    print(f"Words found: {results_found} / {len(insert_words)}")

    # Optional test output
    print("\n Not Inserted Words - Search Results (sample):")
    for word in not_insert_words[:10]:
        print(f"{word}: {'Found' if tree.search(word) else 'Not Found'}")

if __name__ == "__main__":
    main()
