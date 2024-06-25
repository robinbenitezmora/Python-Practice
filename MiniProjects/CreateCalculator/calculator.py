from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial

def get_input(entry, argu):
    entry.insert(END, argu)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0, END)

def calculate(entry):
    input_text = entry.get()
    try:
        result = str(eval(input_text.strip()))
    except ZeroDivisionError:
        popupmsg()
        result = ""
    except Exception:
        result = "Invalid input"
    finally:
        entry.delete(0, END)
        entry.insert(END, result)

def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry('120x100')
    popup.title("Alert")
    label = Label(popup, text="Cannot divide by zero", font=("Verdana", 10))
    label.pack(side="top", fill="x", pady=10)
    ok_button = Button(popup, text="Okay", command=popup.destroy)
    ok_button.pack()
    
def create_calculator():
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)
    entry_font = font.Font(size=15)
    entry = Entry(root, font=entry_font, justify="right")
    entry.grid(row=0, column=0, columnspan=4, sticky=N+S+E+W, padx=5, pady=5)
    
    cal_button_bg = '#FF6600'
    num_button_bg = '#4B4B4B'
    other_button_bg = '#DDDDDD'
    text_fg = '#FFFFFF'
    button_active_bg = '#C0C0C0'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg, padx=10, pady=3, activatbackground=button_active_bg)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg, padx=10, pady=3, activatbackground=button_active_bg)
    button7 = num_button(text='7', bg=num_button_bg, command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0, pady=5)

    button8 = num_button(text='8', bg=num_button_bg, command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1, pady=5)

    button9 = num_button(text='9', bg=num_button_bg, command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2, pady=5)

    button10 = num_button(text='10', bg=num_button_bg, command=lambda: get_input(entry, '10'))
    button10.grid(row=4, column=3, pady=5)

    button4 = num_button(text='4', bg=num_button_bg, command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0, pady=5)

    button5 = num_button(text='5', bg=num_button_bg, command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1, pady=5)

    button6 = num_button(text='6', bg=num_button_bg, command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=1, pady=5)

    button11 = num_button(text='11', bg=num_button_bg, command=lambda: get_input(entry, '11'))
    button11.grid(row=2, column=2, pady=5)

    button1 = num_button(text='1', bg=num_button_bg, command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0, pady=5)

    button2 = num_button(text='2', bg=num_button_bg, command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1, pady=5)

    button3 = num_button(text='3', bg=num_button_bg, command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2, pady=5)

    button12 = num_button(text='*', bg=num_button_bg, command=lambda: get_input(entry, '*'))
    button12.grid(row=2, column=3, pady=5)

    button0 = num_button(text='0', bg=num_button_bg, command=lambda: get_input(entry, '0'))
    button0.grid(row=5, column=0, pady=5)

    button13 = num_button(text='.', bg=num_button_bg, command=lambda: get_input(entry, '.'))
    button13.grid(row=5, column=1, pady=5)

    button14 = Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '/'))
    button14.grid(row=1, column=3, pady=5)

    button15 = Button(root, text='<-', bg=other_button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=1, column=0, columnspan=2,
                  padx=3, pady=5, sticky=N + S + E + W)

    button16 = Button(root, text='C', bg=other_button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=1, column=2, pady=5)

    button17 = Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=3, pady=5)

    button18 = Button(root, text='^', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '**'))
    button18.grid(row=5, column=2, pady=5)
    def quit():
        exit['command'] = root.quit()
    exit = Button(root, text='Quit', fg='white', bg='black', command=quit, height=1, width=7)
    exit.grid(row=6, column=1)

    root.mainloop()

if __name__ == '__main__':
    create_calculator()




