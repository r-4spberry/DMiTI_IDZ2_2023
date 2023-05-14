import inspect

lt = "abcdefg"
sg = "*+/-"
inp = "a\n"
char = ""
ind = -1

def read():
    global char, inp, ind
    #print(inp, inspect.stack()[1][3])
    char = inp[0]
    inp = inp[1:]
    ind += 1
    
def error():
    #print(inp)
    #print(char)
    raise AssertionError()

def psz():
    if char == "(":
        read()
        vir_bks()
        if char == ")":
            read()
            if char == "\n":
                pass
            else:
                error()
        else:
            error()
    elif char == "[":
        read()
        vir()
        if char == "]":
            read()
            if char == "\n":
                pass
            else:
                error()
        else:
            error()
    elif char in lt:
        read()
        if char == "\n":
            pass
        else:
            error()
    else:
        error()

def vir():
    if char == "(":
        read()
        vir_bks()
        if char == ")":
            read()
        else:
            error()
        konec()
        
    elif char == "[":
        read()
        vir()
        if char == "]":
            read()
        else:
            error()
        konec()
        
    elif char in lt:
        read()
        konec_np()
        
    else:
        error()

def vir_ok():
    if char == "(":
        read()
        vir_bks()
        if char == ")":
            read()
        else:
            error()
        
    elif char == "[":
        read()
        vir()
        if char == "]":
            read()
        else:
            error()
            
    elif char in lt:
        read()
        
    else:
        error()

def vir_bks():
    if char == "[":
        read()
        vir()
        if char == "]":
            read()
        else:
            error()
        konec()
        
    elif char in lt:
        read()
        konec_bks_np()
        
    else:
        error()

def vir_bks_ok():
    if char == "[":
        read()
        vir()
        if char == "]":
            read()
        else:
            error()
        
    elif char in lt:
        read()
        
    else:
        error()

def konec():
    if char in sg:
        read()
        vir_ok()
    else:
        pass

def konec_bks():
    if char in sg:
        read()
        vir_bks_ok()
    else:
        pass

def konec_np():
    if char in sg:
        read()
        vir_ok()
    else:
        error()

def konec_bks_np():
    if char in sg:
        read()
        vir_bks_ok()
    else:
        error()

    
if __name__ == "__main__":
    read()
    psz()


import tkinter as tk
from tkinter import messagebox

def confirm_text():
    global inp
    global ind
    ind = -1
    inp = text_field.get()+"\n"
    old_inp = inp
    if inp:
        try:
            read()
            psz()
            messagebox.showinfo("Done!", f"Your string is correct\nYou entered: {old_inp}")
        except:
            messagebox.showinfo("Error!", f"Something wrong with your string\nError symbol: \"{char}\"[{ind}]")
    else:
        messagebox.showerror("Error", "Please enter some text")

# create the main window
root = tk.Tk("DMiTI","DMiTI","DMiTI")
root.geometry("800x180")

# create the text field and button
input_label = tk.Label(root, text="Введите свою строку:")
text_field = tk.Entry(root)
confirm_button = tk.Button(root, text="Confirm", command=confirm_text)

# create the information box
info_label = tk.Label(root, text=
"""Правильная скобочная запись арифметических выражений с двумя видами скобок.
После круглой скобки в строке может стоять только квадратная, после квадратной - не обязательно.
Каждая бинарная операция вместе с операндами берется в скобки.
В правильной записи могут присутствовать “лишние” (двойные) скобки, но одна буква не может браться в скобки.""", anchor='w')

# pack the text field and button into the main window
input_label.pack()
text_field.pack(fill=tk.X, padx=5, pady=5) # fill horizontally, with 5 pixels of padding
confirm_button.pack(padx=5, pady=5)

info_label.pack()
# start the main loop
root.mainloop()
