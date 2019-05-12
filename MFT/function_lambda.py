import math

distance = lambda x, y: math.sqrt(x ** 2 + y ** 2)
print(distance(3, 4))


right = lambda lst: lst[len(lst)//2:][::-1] + lst[len(lst)//2:]
left = lambda lst: lst[:len(lst)//2] + lst[:len(lst)//2:][::-1]
lst = list(range(1,11))
print(left(lst))