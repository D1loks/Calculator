import tkinter as tk


def button_click(value):
    current_text = ent.get()

    if value == 'AC':
        ent.delete(0, tk.END)
    elif value == '+/-':
        if current_text and current_text[0] == '-':
            ent.delete(0)
        else:
            ent.insert(0, '-')
    elif value == '%':
        if current_text and current_text[-1] not in ['%', '*', '/', '+', '-']:
            try:
                result = eval(current_text) / 100
                ent.delete(0, tk.END)
                ent.insert(tk.END, str(result))
            except (SyntaxError, ZeroDivisionError, ValueError):
                ent.delete(0, tk.END)
                ent.insert(tk.END, "Error")
    elif value == '=':
        try:
            result = eval(current_text)
            ent.delete(0, tk.END)
            ent.insert(tk.END, str(result))
        except (SyntaxError, ZeroDivisionError, ValueError):
            ent.delete(0, tk.END)
            ent.insert(tk.END, "Error")
    elif value == '☀️':
        toggle_dark_mode()
    else:
        ent.insert(tk.END, value)


def toggle_dark_mode():
    current_bg = root.cget('bg')
    new_bg = '#121212' if current_bg == '#F9F9F9' else '#F9F9F9'

    current_text_color = ent.cget('fg')  # Get the current text color
    new_text_color = '#FFFFFF' if current_text_color == '#000000' else '#000000'

    current_button_color = buttons[0].cget('bg')  # Get the current button color
    new_button_color = '#333333' if current_button_color == '#DDDDDD' else '#DDDDDD'

    ent.configure(bg=new_bg, fg=new_text_color)
    root.configure(bg=new_bg)

    for button in buttons:
        button.configure(bg=new_button_color, fg=new_text_color)


root = tk.Tk()
lt = [
    "AC", '+/-', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=', '☀️'
]
w = root.winfo_screenwidth() // 2 - 150
h = root.winfo_screenheight() // 2 - 200
root.geometry(f'300x400+{w}+{h}')
root.configure(bg='#F9F9F9')

ent = tk.Entry(root, width=20, font=('Arial', 14), justify='right', bg='#F9F9F9', fg='#000000')
ent.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

count = 0
buttons = []
for r in range(1, 6):
    for c in range(4):
        if count < len(lt):
            button_value = lt[count]
            btn = tk.Button(root, text=button_value, width=5, height=2,
                            command=lambda val=button_value: button_click(val),
                            bg='#DDDDDD', fg='#000000')
            btn.grid(row=r, column=c)
            buttons.append(btn)
            count += 1

root.mainloop()
