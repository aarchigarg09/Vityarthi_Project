import tkinter as tk
def append_to_display(value):
    current_text = display.get()
    display.set(current_text + str(value))
def clear_display():
    display.set("")
def evaluate_expression():
    try:
        result = eval(display.get())
        display.set(str(result))
    except:
        display.set("Invalid Input")
def on_key_press(event):
    key = event.char
    if key.isdigit() or key in '+-*/.':
        append_to_display(key)
    elif event.keysym == 'Return':
        evaluate_expression()
    elif event.keysym == 'Escape':
        clear_display()
root = tk.Tk()
root.title("Calculator")
root.configure(bg='#2b2b2b')
display = tk.StringVar()
display.set("")
display_label = tk.Label(root, textvariable=display, font=('Arial', 24), bg='#2b2b2b', fg='white', anchor='e', width=20)
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('A', 5, 0)
]
button_bg_color = '#607d8b'
button_fg_color = 'Red'
special_button_bg_color = '#ff5722'
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 18), bg=special_button_bg_color, fg=button_fg_color, command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18), bg=special_button_bg_color, fg=button_fg_color, command=clear_display)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 18), bg=button_bg_color, fg=button_fg_color, command=lambda t=text: append_to_display(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)
root.bind('<Key>', on_key_press)
root.mainloop()