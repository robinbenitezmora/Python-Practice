from tkinter import *
from tkinter import ttk

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

        # Label Welcome
        self.l_welcome = Label(self.window, text='Welcome!')
        self.l_welcome.config(font=('Andale Mono Regular', 20, 'bold'), bg='red', fg='white')
        self.l_welcome.place(x=380, y=35)

        # Label Detail
        self.l_detail = Label(self.window, text='Data of the worker for the Vacations Calcule')
        self.l_detail.config(font=('Andale Mono Regular', 18, 'bold'), bg='red', fg='white')
        self.l_detail.place(x=60, y=110)

        # Label Name
        self.l_name = Label(self.window, text='Name:')
        self.l_name.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white')
        self.l_name.place(x=60, y=160)

        # Entry Name
        self.data_name = StringVar()
        self.e_name = Entry(self.window, textvariable=self.data_name, bd=2, bg='#eee8e8', fg='red')
        self.e_name.config(font=('Andale Mono Regular', 12, 'bold'), width=27)
        self.e_name.place(x=60, y=190)

        # Label First Name
        self.l_first_name = Label(self.window, text='First Name:')
        self.l_first_name.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white')
        self.l_first_name.place(x=60, y=240)

        # Entry First Name
        self.data_first_name = StringVar()
        self.e_first_name = Entry(self.window, textvariable=self.data_first_name, bd=2, bg='#eee8e8', fg='red')
        self.e_first_name.config(font=('Andale Mono Regular', 12, 'bold'), width=27)
        self.e_first_name.place(x=60, y=270)

        # Label Last Name
        self.l_last_name = Label(self.window, text='Last Name:')
        self.l_last_name.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white')
        self.l_last_name.place(x=60, y=320)

        # Entry Last Name
        self.data_last_name = StringVar()
        self.e_last_name = Entry(self.window, textvariable=self.data_last_name, bd=2, bg='#eee8e8', fg='red')
        self.e_last_name.config(font=('Andale Mono Regular', 12, 'bold'), width=27)
        self.e_last_name.place(x=60, y=350)

        # Select Department
        self.l_department = Label(self.window, text='Select the Department:')
        self.l_department.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white')
        self.l_department.place(x=380, y=160)

        self.var_combo1 = StringVar()
        self.op_combo = (' ', 'Customer Attention', 'Logistic Departmente', 'Management Department')
        self.combobox1 = ttk.Combobox(self.window, state='readonly', values=self.op_combo, textvariable=self.var_combo1, width=25, font=('Andale Mono Regular', 11, 'bold'))
        self.combobox1.current(0)
        self.combobox1.place(x=380, y=190)

        # Select Antiquity
        self.l_antiquity = Label(self.window, text='Select the Antiquity:')
        self.l_antiquity.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white')
        self.l_antiquity.place(x=380, y=240)

        self.var_combo2 = StringVar()
        self.op_combo2 = (' ', '1 year', '2 to 6 years', 'more than 7 years')
        self.combobox2 = ttk.Combobox(self.window, state='readonly', values=self.op_combo2, textvariable=self.var_combo2, width=25, font=('Andale Mono Regular', 11, 'bold'))
        self.combobox2.current(0)
        self.combobox2.place(x=380, y=270)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox', background='red')

        # Result Label
        self.l_result = Label(self.window, text='Result of the Calcule:')
        self.l_result.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white')
        self.l_result.place(x=380, y=320)

        # Text Result
        self.text_result = Text(self.window, width=27, height=7)
        self.text_result.config(font=('Andale Mono Regular', 11, 'bold'), bg='#eee8e8', fg='red', state=DISABLED)
        self.text_result.place(x=380, y=350)

        # Label footer
        self.l_footer = Label(self.window, text='©2024 The Coca-Cola Company.')
        self.l_footer.config(font=('Andale Mono Regular', 10, 'bold'), bg='red', fg='white')
        self.l_footer.place(x=200, y=485)

        # Buttons
        self.b_calculate = Button(self.window, text='Calculate', width=10, height=2)
        self.b_calculate.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white', bd=5)
        self.b_calculate.place(x=190, y=420)

        self.b_clear = Button(self.window, text='Clear', width=10, height=2)
        self.b_clear.config(font=('Andale Mono Regular', 12, 'bold'), bg='red', fg='white', bd=5)
        self.b_clear.place(x=60, y=420)



        self.window.mainloop()

Principal()
