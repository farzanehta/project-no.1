def shift_max(lst):
    is_sorted = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            is_sorted = False
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return is_sorted


lst = [3, 9, 4, 5, 1, 8, 2, 6, 7]
print(lst)

while True:
    is_sorted = shift_max(lst)
    print(lst)
    if is_sorted:
        break
