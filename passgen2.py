from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random as r
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry('350x500')
        self.root.title("Password Generator")
    
# Variables
        self.length_var = IntVar(value="")
        self.upper_var = BooleanVar(value=True)
        self.lower_var = BooleanVar(value=True)
        self.digit_var = BooleanVar(value=True)
        self.special_var = BooleanVar(value=True)
        self.complexity_var = StringVar(value="")
        self.result_var = StringVar(value="| Generated Password will appear here |")
        self.create_widgets()

    def generate_password(self):
        all_chars = ""
        if self.upper_var.get():
            all_chars += string.ascii_uppercase
        if self.lower_var.get():
            all_chars += string.ascii_lowercase
        if self.digit_var.get():
            all_chars += string.digits
        if self.special_var.get():
            all_chars += string.punctuation

        if not all_chars:
            self.result_var.set("Select at least one character type.")
            return

        password = self.generate_complex_password(all_chars)
        self.result_var.set(password)

    def generate_complex_password(self, all_chars):
        password = ''
        complexity = self.complexity_var.get()

        if complexity == "Simple":
            password += ''.join(r.choice(all_chars) for _ in range(self.length_var.get()))

        elif complexity == "Moderate":
            if self.upper_var.get():
                password += r.choice(string.ascii_uppercase)
            if self.lower_var.get():
                password += r.choice(string.ascii_lowercase)
            password += ''.join(r.choice(all_chars) for _ in range(self.length_var.get() - 1))

        elif complexity == "Complex":
            if self.upper_var.get():
                password += r.choice(string.ascii_uppercase)
            if self.lower_var.get():
                password += r.choice(string.ascii_lowercase)
            if self.digit_var.get():
                password += r.choice(string.digits)
            if self.special_var.get():
                password += r.choice(string.punctuation)
            password += ''.join(r.choice(all_chars) for _ in range(self.length_var.get() - 1 ))

        return ''.join(r.sample(password, len(password)))

    def copy_to_clipboard(self):
        generated_password = self.result_var.get()
        pyperclip.copy(generated_password)
        self.result_var.set("Password copied to clipboard!")

    def create_widgets(self):
# Frame
        frame = ttk.Frame(self.root,style="TFrame")
        frame.place(x=20,y=20)

##        ttk.Style().configure("TButton", padding=10)
##        ttk.Style().configure("TRadiobutton", padding=5)

# Labels
        ttk.Label(frame, text="Password Length  : ", style="TLabel").grid(row=0, column=0, sticky="w", pady=10)

# Entry for password length
        length_entry = ttk.Entry(frame, textvariable=self.length_var, width=5)
        length_entry.grid(row=0, column=1, sticky="w", pady=10)

# Checkbuttons for character types
        ttk.Checkbutton(frame, text="Uppercase", variable=self.upper_var, style="TRadiobutton").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Checkbutton(frame, text="Lowercase", variable=self.lower_var, style="TRadiobutton").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Checkbutton(frame, text="Digits", variable=self.digit_var, style="TRadiobutton").grid(row=3, column=0, sticky="w", pady=5)
        ttk.Checkbutton(frame, text="Special Characters", variable=self.special_var, style="TRadiobutton").grid(row=4, column=0, sticky="w", pady=5)

# Combobox for password complexity
        complexity_label = ttk.Label(frame, text="Password Complexity  : ", style="TLabel")
        complexity_label.grid(row=5, column=0, sticky="w", pady=10)
        complexity_combobox = ttk.Combobox(frame, textvariable=self.complexity_var, values=["Simple", "Moderate", "Complex"], style="TCombobox")
        complexity_combobox.grid(row=5, column=1, sticky="w", pady=10)
        complexity_combobox.set("Moderate")

# Button to generate password
        generate_button = Button(frame, text="Generate Password", command=self.generate_password, borderwidth=1) 
        generate_button.grid(row=6, column=0, columnspan=2, pady=20)

# Result label
        result_label = Label(frame, textvariable=self.result_var, wraplength=300, background="#A6ACAF")
        result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Button to copy password to clipboard
        copy_button = Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard, borderwidth=1)
        copy_button.grid(row=8, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()
