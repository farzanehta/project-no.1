phone = input("Phone: ")
output = ""
digit_mapping = {"1": "One", "2": "Two", "3": "Three", "4": "Four"}
for i in phone:
    output += digit_mapping.get(i, "?") + " "
print(output)