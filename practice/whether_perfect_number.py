# what is perfect number?
# sum of divisors (except number itself) == number OR sum of all divisors (include number itself) //2 == num

# 1 >> My code


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


print(whether_perfect(33550336))


# 2 >> net code
def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n


print(perfect_number(33550336))
