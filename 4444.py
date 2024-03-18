import tkinter as tk
import math

def on_button_click(event):
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def add_to_expression(value):
    entry.insert(tk.END, value)

def clear_expression():
    entry.delete(0, tk.END)

def calculate_square_root():
    try:
        expression = entry.get()
        result = math.sqrt(float(expression))
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def calculate_power():
    try:
        expression = entry.get()
        base, exponent = expression.split('^')
        result = float(base) ** float(exponent)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def calculate_log():
    try:
        expression = entry.get()
        result = math.log10(float(expression))
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def calculate_sin():
    try:
        expression = entry.get()
        result = math.sin(math.radians(float(expression)))
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def calculate_cos():
    try:
        expression = entry.get()
        result = math.cos(math.radians(float(expression)))
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'log',
    'C', '0', '=', '+', 'sqrt', '^'
]

row = 1
col = 0
for button_value in buttons:
    if button_value == 'C':
        button = tk.Button(root, text=button_value, command=clear_expression)
    elif button_value == '=':
        button = tk.Button(root, text=button_value, command=on_button_click)
    elif button_value == 'sqrt':
        button = tk.Button(root, text=button_value, command=calculate_square_root)
    elif button_value == '^':
        button = tk.Button(root, text=button_value, command=calculate_power)
    elif button_value == 'log':
        button = tk.Button(root, text=button_value, command=calculate_log)
    elif button_value == 'sin':
        button = tk.Button(root, text=button_value, command=calculate_sin)
    elif button_value == 'cos':
        button = tk.Button(root, text=button_value, command=calculate_cos)
    else:
        button = tk.Button(root, text=button_value, command=lambda value=button_value: add_to_expression(value))
    button.grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=row, column=0, columnspan=5)

root.mainloop()
