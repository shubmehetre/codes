import file2
from filemodules.file_words_counter import count_words

filename = "txt_and_json_files/pi_digits.txt"
ans = count_words(filename)
print(f"words in the file : {ans}")


if __name__ == "__main__":
    print(f"file1 __name__ is {__name__}")