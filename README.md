# Ternary Search Tree Project

## Overview
This project implements a Ternary Search Tree (TST) in Python using an object-oriented approach. It supports efficient insertion and search operations, prefix matching, and word retrieval. The implementation includes benchmarking, complexity analysis, and a comparison with B-tree performance.

The project is tested both as a standalone script (`main.py`) and interactively via a Jupyter notebook.

## Project Structure
```
ternary-search-tree/
├── main.py                  # CLI script for benchmarking and summary output
├── ternary_tree.py          # TST logic (Node and TernarySearchTree classes)
├── file_loader.py           # Utility for loading word lists from text files
├── TernaryTree_Demo_Final_Complete.ipynb  # Jupyter notebook with all benchmarks and analysis
├── data/
│   └── search_trees/
│       ├── insert_words.txt
│       ├── not_insert_words.txt
│       └── corncob_lowercase.txt
```

## How to Run

### 🔹 From the Command Line:
```bash
cd ternary-search-tree
python main.py
```

### 🔹 From Jupyter Notebook:
Open `TernaryTree_Demo_Final_Complete.ipynb` in VS Code or Jupyter and run the cells to interactively:
- Insert/search words
- Run benchmarks
- Visualize performance plots
- Compare TST and B-tree timing

## Files Explained
- `main.py`: Benchmark insert/search, prints summary to console.
- `ternary_tree.py`: Fully documented Ternary Search Tree implementation.
- `file_loader.py`: Loads word lists from `.txt` files.
- `TernaryTree_Demo_Final_Complete.ipynb`: Full demonstration and analysis notebook.
- `data/search_trees/`: Word lists for input and performance testing.

## Features
- Insert/search functionality
- Prefix-based word retrieval
- Word count tracking
- ASCII-style tree visualization
- Benchmarking with large dataset
- Performance plots using `matplotlib`
- B-tree comparison via `bintrees`
- Time and space complexity analysis
- HPC usage note (for remote job submissions)

## Sample Output

Benchmark Summary:
```
Inserted 4000 words in 0.0194 seconds
Searched 4000 words in 0.0152 seconds
Words found: 4000 / 4000
```

Inserted Words - Search Results:
```
combine: Found
combinations: Found
...
```

Not Inserted Words - Search Results:
```
futures: Not Found
fontains: Not Found
...
```

---

## Notes
- All input words are assumed lowercase.
- Duplicate inserts are ignored internally.
- Performance metrics vary depending on machine specs and dataset size.

---

**Created for course assignment on Ternary Search Trees.**
