import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if digit_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one option")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)


# GUI Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title
tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length Input
tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Options
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase Letters", variable=upper_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Lowercase Letters", variable=lower_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Numbers", variable=digit_var).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Symbols", variable=symbol_var).pack(anchor="w", padx=50)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)

# Result
tk.Label(root, text="Generated Password").pack()
result_entry = tk.Entry(root, width=40)
result_entry.pack(pady=5)

root.mainloop()
