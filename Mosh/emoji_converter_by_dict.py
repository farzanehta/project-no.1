message = input("> ")
words = message.split(" ")
emojis = {":)": "😊", ":(": "☹", ";)": "😉", ":|": "😐"}
output = ""
for w in words:
        output += emojis.get(w, w) + " "

print(output)
