import random
import string

def gen_password(length = 12, upper_include = True, digits_include = True, specialChars_include = True):
    if length < 5:
        raise ValueError("Password must be at least six characters")

    characters = list(string.ascii_letters)
    if upper_include:
        characters += list(string.ascii_uppercase)
    if digits_include:
        characters += list(string.digits)
    if specialChars_include:
        characters += list(string.punctuation)

#Ensures that the password contains at least one character from each selected category

    password = []
    if upper_include:
        password.append(random.choice(string.ascii_uppercase))
    if digits_include:
        password.append(random.choice(string.digits))
    if specialChars_include:
        password.append(random.choice(string.punctuation))
    password += [random.choice(characters) for _ in range(length = len(password))]

    #Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)