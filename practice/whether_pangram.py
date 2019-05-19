import string


def is_pangram(phrase):
    alphabet = string.ascii_lowercase
    for char in alphabet:
        if char not in phrase:
            return False
    return True


text = "The quick brown fox jumps over the lazy dog"
print(is_pangram(text))
