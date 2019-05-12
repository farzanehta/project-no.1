lst = [99, 21, 1, 2, 3, 4, 5, 6, 7, 8, 77, 9, 10, 11]
# average left list- average right list
mid_member = len(lst) // 2
print(lst[mid_member])
left_list = lst[:mid_member]
right_list = lst[mid_member:]
left_average = sum(left_list) / len(left_list)
right_average = sum(right_list) / len(right_list)
print(left_average - right_average)
