# Print nth number in fibo series (Iterative Approach)


def fibo_nth(n) -> int:
    n1 = 0
    n2 = 1
    temp = 0

    if n == 0:
        return n1
    if n == 1:
        return n2

    while n - 2 > 0:
        temp = n1 + n2
        n1 = n2
        n2 = temp
        n -= 1
    return temp


print(fibo_nth(4))
