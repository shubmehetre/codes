# EASY: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    list1 = []
    dict1 = {}

    for _ in range(N):
        op, *line = input().split()
        args = list(line)
        dict1[op] = args

    print(dict1)

#   while(N):
#       if(N == 'insert'):
