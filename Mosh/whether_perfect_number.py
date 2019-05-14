def whether_perfect(num):
    is_perfect = False
    i = 1
    divisors = []
    for i in range(i, num + 1):
        if num % i == 0:
            divisors.append(i)
        else:
            pass
    print(divisors)

    if sum(divisors) - num == num:
        is_perfect = True
    return is_perfect


print(whether_perfect(8128))
