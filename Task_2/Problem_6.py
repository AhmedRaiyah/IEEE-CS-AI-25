import random
import string

chars = string.ascii_letters + string.digits
chars = tuple(chars)
password = ""

for x in range(0, 8):
    password += random.choice(chars)

print(f"Generated password: {password}")