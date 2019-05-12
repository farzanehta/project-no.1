import random

secret = random.randint(1, 20)
print(secret)
guess_count = 5
for _ in range(5):
    guess = int(input("guess a number: "))
    if guess < secret:
        print("you're guess is LESS than the secret")
    elif guess > secret:
        print("you're guess is GREATER than the secret")
    else:
        print("BINGO!")

print("you're a LOSER!")
