answer = 0
i = 0
#target = 1.08232323371113819151600 # s = 4
target = 1.64493406684822643647241 # s = 2
err = (answer - target) / target
s = 2

while abs(err) > 0.001:
    i += 1
    answer = answer + 1 / i ** s
    err = (answer - target) / target

print(i)

