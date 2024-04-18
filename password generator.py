import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        result_label.config(text="Error: No character set selected")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Random Password Generator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

letters_var = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(frame, text="Letters", variable=letters_var)
letters_checkbox.grid(row=1, column=0, padx=5, pady=5)

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(frame, text="Numbers", variable=numbers_var)
numbers_checkbox.grid(row=1, column=1, padx=5, pady=5)

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(frame, text="Symbols", variable=symbols_var)
symbols_checkbox.grid(row=1, column=2, padx=5, pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()





