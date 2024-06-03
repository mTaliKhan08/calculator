import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

def divide():
    try:
        if float(entry2.get()) != 0:
            result = float(entry1.get()) / float(entry2.get())
            label_result.config(text=f"Result: {result}")
        else:
            messagebox.showerror("Math error", "Division by zero is not allowed")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("GUI Calculator")

# Create and place widgets
tk.Label(root, text="1st No:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=0)

tk.Label(root, text="2nd No:").grid(row=0, column=1)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Addition (+)", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtraction (-)", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiplication (*)", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Division (/)", command=divide).grid(row=3, column=1)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, columnspan=2)

# Start the main event loop
root.mainloop()
