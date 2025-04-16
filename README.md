### README.md
# Ternary Search Tree Project

## Overview
This project implements a Ternary Search Tree (TST) in Python using an object-oriented approach. It includes functionality to insert and search for words, and loads test words from provided input files.

## Project Structure
```
ternary-search-tree/
├── main.py                  # Runs insertion/search using provided data files
├── ternary_tree.py          # TST logic (Node and TST class)
├── file_loader.py           # Helper function to load words from file
├── data/
│   └── search_trees/
│       ├── insert_words
│       ├── not_insert_words
│       └── corncob_lowercase
```

## How to Run
Make sure you are in the project directory, then run:
```bash
python main.py
```

## Files Explained
- `main.py`: Main script to load words and test insert/search
- `ternary_tree.py`: Contains the Ternary Search Tree implementation
- `file_loader.py`: Loads lines from a word file
- `data/search_trees/`: Contains your insert/test word files

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