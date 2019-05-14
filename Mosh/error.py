def string_test(s):
    d = {"upper_case": 0, "lower_case": 0}
    for c in s:
        if c.isupper():
            d["upper_case"] += 1
        elif c.islower():
            d["lower_case"] += 1
        else:
            pass


print(d["upper_case"])
print(d["lower_case"])
string_test("The quick Brown Fox")