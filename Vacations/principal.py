from tkinter import *

class Principal:
    def __init__(self):
        self.window = Tk()
        self.window.title('Principal Window')
        self.window.resizable(False, False)
        self.window.geometry('640x535+380+100')
        self.window.configure(bg='red')
        self.window.iconbitmap(r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\icon0.ico')

        # Options Menu
        self.menubar1 = Menu(self.window)
        self.window.config(menu=self.menubar1)
        self.options1 = Menu(self.menubar1, tearoff=0)
        self.options2 = Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Options', menu=self.options1)
        self.options1.add_command(label='Exit', font=('Arial', 10, 'bold'))

        self.menubar1.add_cascade(label='About of..', menu=self.options2)
        self.options2.add_command(label='Info', font=('Arial', 10, 'bold'))

        self.window.mainloop()

Principal()
