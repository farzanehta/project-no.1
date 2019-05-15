def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s


def combination(n, k):
    res = factorial(n) // (factorial(k) * factorial(n - k))
    return res


def pascal_row(n):
    row = []
    for i in range(0, n + 1):
        temp = combination(n, i)
        row += [temp]
    return row


print(pascal_row(8))


def pascal_member(n, k):
    res = combination(n, k)
    return res


print(pascal_member(8, 3))
