lst = [5, 26, 45, 89, 99, 31, 13]
mx = lst[0]
for i in lst:
    if i > mx:
        mx = i
print(mx)


def find_max(lst):
    mx = lst[0]
    for i in lst:
        if i > mx:
            mx = i
    return mx

lst = [55, 41, 102, 98, 1]
print(find_max(lst))

