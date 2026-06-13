import string

password = input("Enter a password: ")

length = len(password)

has_upper = False
has_digit = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif char in string.punctuation:
        has_symbol = True

score = 0

if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

if score <= 1:
    print("Password Strength: Weak")
elif score <= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")