### README.md
# Ternary Search Tree Project

## Overview
This project implements a Ternary Search Tree (TST) in Python using an object-oriented approach. It includes functionality to insert and search for words, and loads test words from provided input files.

## Project Structure
```
ternary-search-tree/
├── main.py # Script to insert/search words using data files
├── ternary_tree.py # TST logic (Node and TernarySearchTree classes)
├── file_loader.py # Utility for loading word lists from text files
├── TernaryTree_Demo.ipynb # Jupyter notebook demo and test examples
├── data/
│ └── search_trees/
│ ├── insert_words.txt
│ ├── not_insert_words.txt
│ └── corncob_lowercase.txt
```

## How to Run

### 🔹 From the command line:
```bash
cd ternary-search-tree
python main.py
```
Open TernaryTree_Demo.ipynb in VS Code or Jupyter and run the cells to interactively test the tree.

## Files Explained
- `main.py`: Loads test word files and runs insert/search operations.
- `ternary_tree.py`: Contains the full Ternary Search Tree implementation.
- `file_loader.py`: Helper for reading word lists from .txt files.
- `TernaryTree_Demo.ipynb`: Jupyter notebook to demonstrate and benchmark the tree.
- `data/search_trees/`: Folder with input word lists for testing.

## Sample Output
```
✅ Inserted Words - Search Results:
combine: Found
combinations: Found
...

❌ Not Inserted Words - Search Results:
futures: Not Found
fontains: Not Found
...
```

## Notes
- Duplicate words are handled.
- All word input is assumed lowercase, no special preprocessing.

---
Created for course assignment on Ternary Search Trees.