### file_loader.py
def load_words(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file if line.strip()]
