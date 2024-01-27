import random
import string


def hard_pass_gen():
    strings = ''
    for _ in range(16):
        a = random.choice(string.ascii_uppercase)
        b = random.choice(string.ascii_lowercase)
        c = random.choice(string.digits)
        d = random.choice(string.punctuation)
        l = [a, b, c, d]
        strings += random.choice(l)
    return strings

def medium_pass_gen():
    strings = ''
    for _ in range(12):
        a = random.choice(string.ascii_uppercase)
        b = random.choice(string.ascii_lowercase)
        c = random.choice(string.digits)
        d = random.choice(string.punctuation)
        l = [a, b, c, d]
        strings += random.choice(l)
    return strings
        
def easy_pass_gen():
    strings = ''
    for _ in range(8):
        a = random.choice(string.ascii_uppercase)
        b = random.choice(string.ascii_lowercase)
        c = random.choice(string.digits)
        l = [a, b, c]
        strings += random.choice(l)
    return strings

