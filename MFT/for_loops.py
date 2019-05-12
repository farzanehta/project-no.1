fact = 1
for i in range(1, 11):
    print(i, fact)
    fact = fact * i
print(fact)

for num in range(2, 11):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    print(num, is_prime)

s = 4
answer = 0
for i in range(1, 1001):
    answer = answer + 1 / i ** s

pi_approximate = (answer * 90) ** 0.25
print(pi_approximate)
