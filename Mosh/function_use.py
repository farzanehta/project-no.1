def emoji_converter(message):
    words = message.split(" ")
    emoji = {":)": "😊", ":(": "☹", ";)": "😉", ":|": "😐"}
    output = ""
    for w in words:
        output += emoji.get(w, w) + " "
    return output


message = ":)"
print(emoji_converter(message))


# --------------------------------------------
def sum_num(lst):
    total = 0
    for i in lst:
        total += i
    return total


lst = [8, 2, 3, 0, 7]
print(sum_num(lst))


# -------------------------------------------
def multiply(numbers):
    total = 1
    for i in lst:
        total *= i
    return total


lst = [8, 2, 3, -1, 7]
print(multiply(lst))


# -------------------------------------------
def reverse(message):
    return message[::-1]


message = "1234abcd"
print(reverse(message))


# ------------------------------------------
def fact(number):
    total = 1
    i = 1
    while i <= number:
        total *= i
        i += 1
    return total


print(fact(4))


# -------------------------------------------
def whether_in_range(number):
    in_range = True
    if number not in range(3, 5):
        in_range = False
    return in_range


print(whether_in_range(5))


# --------------------------------------------
def unique(numbers):
    for i in numbers:
        if numbers.count(i) > 1:
            numbers.remove(i)
    return numbers


lst_new = [1, 2, 3, 3, 3, 4, 5, 5]
print(unique(lst_new))


# ---------------------------------------------
def check_prime(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    return is_prime


print(check_prime(31 ))


# -----------------------------------------------
def even_num(lst):
    res = []
    for i in lst:
        if i % 2 == 0:
            res.append(i)
    return res


lst = range(1, 21)
print(even_num(lst))
# ------------------------------------------------
