from tkinter import *

class Welcome:
    def __init__(self):
        self.window = Tk()
        self.window.title('Access')
        self.window.resizable(False, False)
        self.window.geometry('350x450+500+150')
        self.window.configure(bg='red')
        self.window.iconbitmap(r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\icon0.ico')

        self.background = PhotoImage(file=r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\logo-coca.png')
        Label(self.window, image=self.background, bg='red').pack()

        # Labels
        self.label1 = Label(self.window, text='Vacational Control System')
        self.label1.config(font=('Andale Mono Regular', 18, 'italic'), bg='red', fg='white')
        self.label1.place(x=25, y=140)

        self.label2 = Label(self.window, text='Write your name')
        self.label2.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white')
        self.label2.place(x=50, y=220)

        self.label3 = Label(self.window, text='©2024 The Coca-Cola Company.')
        self.label3.config(font=('Andale Mono Regular', 10, 'bold'), bg='red', fg='white')
        self.label3.place(x=70, y=400)

        # Entry User name
        self.data1 = StringVar()
        self.entry1 = Entry(self.window, textvariable=self.data1, bd=2, bg='#eee8e8', fg='red')
        self.entry1.config(font=('Andale Mono Regular', 12, 'bold'), width=27)
        self.entry1.place(x=50, y=250)

        # Button
        self.button1 = Button(self.window, text='Entry', bd=2, bg='white', fg='red')
        self.button1.config(font=('Andale Mono Regular', 14,), width=12)
        self.button1.place(x=100, y=290)

        self.window.mainloop()

Welcome()


