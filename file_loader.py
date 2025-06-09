### file_loader.py

# This function loads a list of words from a text file.
# Each word is expected to be on a separate line.
# Empty lines are ignored, and each word is stripped of leading/trailing whitespace.
def load_words(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file if line.strip()]        
