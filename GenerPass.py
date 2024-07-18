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


if __name__ == "__main__":
    password_length = int(input("Enter the password legnth required: "))
    uppercase_present =input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    digits_present = input("Include digits? (yes/no): ").lower() == 'yes'
    special_chars_present= input("Include special characters? (yes/no) ").lower() == 'yes'

    try:
        generated_password = gen_password(password_length, uppercase_present, digits_present, special_chars_present)
        print(f"Generated password: {generated_password}")
    except ValueError as e:
        print(e)