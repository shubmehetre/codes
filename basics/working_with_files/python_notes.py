import time
def full_content():
    with open("txt_files/learning_python.txt") as x:
        content = x.read()
        print(f"full print : {content}")

def line_by_line():
    with open("txt_files/learning_python.txt") as x:
        for line in x:
            print(f"line by line : {line.rstrip()}")
            time.sleep(1)

def store_in_list():
    with open("txt_files/learning_python.txt") as x:
        list1 = x.readlines()

    for line in list1:
        print(f"print via list : {line.rstrip()}")


full_content()
print()
line_by_line()
print()
store_in_list()
