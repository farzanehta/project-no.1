# 1
lst = [1, 1]
i = 2

while i < 22:
    new_member = lst[i - 1] + lst[i - 2]
    lst = lst + [new_member]
    i += 1
    print(lst)

# 2
member = 22
seq = [1, 1]
while len(seq) < member:
    new_member = seq[-1] + seq[-2]
    seq.append(new_member)
    print(*seq, sep='...')
