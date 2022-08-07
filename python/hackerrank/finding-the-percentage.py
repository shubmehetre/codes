if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # First solution:
#   sum = 0
#   subjects = len(student_marks[query_name])
#   for i in range(subjects):
#       sum = sum + student_marks[query_name][i]

#   avg = "{0:.2f}".format(sum/subjects)
#   print(avg)

    # ALTERNATIVE
    query_scores_list = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores_list) / len(query_scores_list)))
