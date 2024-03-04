import tkinter as tk

# Get the button number to display
def append_to_display(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + char)
    
# Clear the display when click C button
def clear_display():
    entry.delete(0, tk.END)

# calculate base on the appen
def calculate_result():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# Create the main application window
root = tk.Tk()
root.title("Simple Calculator App")
root.geometry("300x400")

# Creating the display field
entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a button
buttons = [
    ("7", lambda: append_to_display("7")),
    ("8", lambda: append_to_display("8")),
    ("9", lambda: append_to_display("9")),
    ("/", lambda: append_to_display("/")),
    ("4", lambda: append_to_display("4")),
    ("5", lambda: append_to_display("5")),
    ("6", lambda: append_to_display("6")),
    ("*", lambda: append_to_display("*")),
    ("1", lambda: append_to_display("1")),
    ("2", lambda: append_to_display("2")),
    ("3", lambda: append_to_display("3")),
    ("-", lambda: append_to_display("-")),
    ("0", lambda: append_to_display("0")),
    (".", lambda: append_to_display(".")),
    ("C", clear_display),
    ("+", lambda: append_to_display("+")),
    ("=", calculate_result)
]
# Create buttons
for i, (text, command) in enumerate(buttons):
    button = tk.Button(root, text=text, width=5, height=2, command=command)
    button.grid(row=i // 4 + 1, column=i % 4, padx=5, pady=5)

# Run the main event loop
root.mainloop()
