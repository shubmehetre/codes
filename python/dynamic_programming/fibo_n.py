# Print n number of fibo series.


def fibo_till_n(n) -> None:
    n1 = 0
    n2 = 1
    temp = 0

    print(n1, n2, end=" ")

    while n - 2 > 0:
        temp = n1 + n2
        print(temp, end=" ")
        n1 = n2
        n2 = temp
        n -= 1


n = int(input("Enter Fibo limit: "))
fibo_till_n(n)
