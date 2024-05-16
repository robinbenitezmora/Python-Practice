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

        # Logo Image
        self.background = PhotoImage(file = r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\coca-cola-p.png')
        Label(self.window, image=self.background, bg='red').place(x=0, y=0)

        # Labels
        self.l_welcome = Label(self.window, text='Welcome!')
        self.l_welcome.config(font=('Andale Mono Regular', 20, 'bold'), bg='red', fg='white')
        self.l_welcome.place(x=380, y=35)

        self.l_detail = Label(self.window, text='Data of the worker for the Vacations Calcule')
        self.l_detail.config(font=('Andale Mono Regular', 18, 'bold'), bg='red', fg='white')
        self.l_detail.place(x=60, y=110)

        self.window.mainloop()

Principal()
