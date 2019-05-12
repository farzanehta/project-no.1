#1(Myself)
numbers = [1, 6, 3, 3, 6, 7, 3, 4, 4, 10]
for i in numbers:
    if numbers.count(i) > 1:
        numbers.remove(i)
print(numbers)
numbers.sort()
numbers.reverse()
print(numbers)

#2(Mosh)
numbers = [1, 6, 3, 3, 6, 7, 3, 4, 4, 10]
uniques = []
for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)
