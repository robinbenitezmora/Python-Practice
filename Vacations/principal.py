from tkinter import *

class Principal:
    def __init__(self):
        self.window = Tk()
        self.window.title('Principal Window')
        self.window.resizable(False, False)
        self.window.geometry('640x535+380+100')
        self.window.configure(bg='red')
        self.window.iconbitmap(r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\icon0.ico')

        self.window.mainloop()

Principal()
