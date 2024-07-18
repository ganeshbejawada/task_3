#TASK 3
#PASSWORD GENERATOR

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        # Create a frame for the password generator
        self.generator_frame = tk.Frame(self.root, padx=20, pady=20)
        self.generator_frame.pack()
        
        # Header label
        self.header_label = tk.Label(self.generator_frame, text="Password Generator", font=("Helvetica", 20, "bold"), pady=10)
        self.header_label.grid(row=0, column=0, columnspan=2)
        
        # Length label and entry
        self.length_label = tk.Label(self.generator_frame, text="Password Length:", font=("Helvetica", 14))
        self.length_label.grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
        self.length_entry = tk.Entry(self.generator_frame, font=("Helvetica", 14), width=10)
        self.length_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Complexity label and checkbuttons
        self.complexity_label = tk.Label(self.generator_frame, text="Complexity:", font=("Helvetica", 14))
        self.complexity_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
        
        self.use_lower = tk.IntVar()
        self.lower_check = tk.Checkbutton(self.generator_frame, text="Lowercase (a-z)", font=("Helvetica", 12), variable=self.use_lower)
        self.lower_check.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.use_upper = tk.IntVar()
        self.upper_check = tk.Checkbutton(self.generator_frame, text="Uppercase (A-Z)", font=("Helvetica", 12), variable=self.use_upper)
        self.upper_check.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.use_digits = tk.IntVar()
        self.digits_check = tk.Checkbutton(self.generator_frame, text="Digits (0-9)", font=("Helvetica", 12), variable=self.use_digits)
        self.digits_check.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.use_symbols = tk.IntVar()
        self.symbols_check = tk.Checkbutton(self.generator_frame, text="Symbols (!@#$%^&*)", font=("Helvetica", 12), variable=self.use_symbols)
        self.symbols_check.grid(row=5, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Generate button
        self.generate_button = tk.Button(self.generator_frame, text="Generate Password", font=("Helvetica", 14), command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Password display label
        self.password_label = tk.Label(self.generator_frame, text="Your Generated Password", font=("Helvetica", 16, "bold"))
        self.password_label.grid(row=7, column=0, columnspan=2, pady=10)
        
        self.password_display = tk.Text(self.generator_frame, height=3, font=("Courier", 14))
        self.password_display.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
        
    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit() or int(length) <= 0:
            messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
            return
        
        length = int(length)
        
        # Check if at least one checkbox is selected
        if not any([self.use_lower.get(), self.use_upper.get(), self.use_digits.get(), self.use_symbols.get()]):
            messagebox.showerror("Error", "Please select at least one option for password complexity.")
            return
        
        password_characters = ""
        
        if self.use_lower.get():
            password_characters += string.ascii_lowercase
        if self.use_upper.get():
            password_characters += string.ascii_uppercase
        if self.use_digits.get():
            password_characters += string.digits
        if self.use_symbols.get():
            password_characters += string.punctuation
        
        generated_password = ''.join(random.choice(password_characters) for _ in range(length))
        
        self.password_display.delete(1.0, tk.END)
        self.password_display.insert(tk.END, generated_password)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
