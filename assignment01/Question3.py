lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
left = lst[:5] + lst[4::-1]
right = lst[-1:-6:-1] + lst[5:]
print(left)
print(right)