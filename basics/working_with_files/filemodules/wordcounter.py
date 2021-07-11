import re
def count_words(filename):
    try:
        with open(filename) as x:
            contents = x.read()

        list_of_words = contents.split()
        num_of_words = len(list_of_words)
        print(f"Words in {filename} - {num_of_words} words")
    except FileNotFoundError:
        pass

