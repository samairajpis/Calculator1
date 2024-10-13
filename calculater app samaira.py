import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

# Function to update the input field
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))

# Function to clear the input field
def clear_entry():
    entry.delete(0, tk.END)

# Function to calculate and display the result
def calculate():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Create the main window
root = tk.Tk()
root.title("Calculator App")

# Create the input field
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create the operator buttons
button_add = tk.Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"))
button_equals = tk.Button(root, text="=", padx=40, pady=20, command=calculate)
button_clear = tk.Button(root, text="Clear", padx=40, pady=20, command=clear_entry)

# Grid the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equals.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=4)

# Start the main loop
root.mainloop()
