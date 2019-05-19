def check_palindrome(msg):
    is_palindrome = False
    if msg[::-1] == msg:
        is_palindrome = True
    return is_palindrome


msg = "madam"
print(check_palindrome(msg))
