import random
import string
import tkinter as tk
from tkinter import messagebox

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


def generate_password():
    try:
        length = int(entry_length.get())
        upper = var_upper.get()
        digits = var_digits.get()
        special_chars = var_special.get()

        password = gen_password(length, upper, digits, special_chars)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

#Setting up the GUI
root = tk.Tk()
root.title("GenerPass")

#Password Length
tk.Label(root, text = "Password Length: ").grid(row = 0, column = 0, padx = 10, pady = 10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column = 1, padx = 10, pady = 10)

#Uppercase Letters
var_upper = tk.BooleanVar()
tk.Checkbutton(root, text = "Include Upper Case Letters", variable=var_upper).grid(row=1, column =0, columnspan=2)

#Digits
var_digits = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable = var_digits).grid(row=2, column = 0, columnspan =2)

# Special Characters
var_special = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).grid(row=3, column=0, columnspan=2)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)

# Result
tk.Label(root, text="Generated Password:").grid(row=5, column=0, padx=10, pady=10)
entry_result = tk.Entry(root, width=30)
entry_result.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()