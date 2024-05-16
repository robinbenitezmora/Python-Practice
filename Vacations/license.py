from tkinter import *

class License:
    def __init__(self):
        self.window = Tk()
        self.window.title('TERMS AND CONDITIONS')
        self.window.resizable(False, False)
        self.window.geometry('600x360+400+200')
        self.window.configure(bg='white')
        self.window.iconbitmap(r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\icon0.ico')

        self.window.mainloop()

License()


