limit = 1000000
answer_1 = 0
answer_2 = 0
i = 0

while i < limit:
    i += 1
    answer_1 = answer_1 + 1 / i ** 2
    answer_2 = answer_2 + 1 / i ** 4

pi_approximate_1 = (answer_1 * 6)**0.5
pi_approximate_2 = (answer_2 * 90)**0.25

print(pi_approximate_1)
print(pi_approximate_2)
