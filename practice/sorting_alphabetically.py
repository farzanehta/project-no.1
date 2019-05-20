import string

text = "green red yellow black white"
lst = text.split()
out = sorted(lst)
print(*out, sep='-')