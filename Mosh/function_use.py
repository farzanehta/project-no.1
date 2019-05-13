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

def detector(msg):
    d = {"upper_case": 0,
         "lower_case": 0}
    for c in msg:
        if c.isupper():
            d["upper_case"] += 1
        elif c.islower():
            d["lower_case"] += 1
        else:
            pass
    return msg


msg = "The quick Brown Fox"
print(d["upper_case"])
print(d["lower_case"])
