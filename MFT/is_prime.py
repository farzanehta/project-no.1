num = 1
while num < 100:
    num += 1
    is_prime = True
    i = 1
    while i < num - 1:
        i += 1
        if num % i == 0:
            is_prime = False
    if is_prime:
        print(num)

num = 13
i = 2
while num % i != 0:
    i += 1
print(i == num)
