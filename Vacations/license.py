from tkinter import *

class License:
    def __init__(self):
        self.window = Tk()
        self.window.title('TERMS AND CONDITIONS')
        self.window.resizable(False, False)
        self.window.geometry('600x360+400+200')
        self.window.configure(bg='white')
        self.window.iconbitmap(r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\icon0.ico')

        self.background = PhotoImage(file = r'C:\Users\Robin\PYTHON PROJECTS\Launch_School\Python-Practice\Vacations\coca-cola-l.png')
        Label(self.window, image=self.background, bg='white').place(x=300, y=220)

        # Labels
        self.label1 = Label(self.window, text='TERMS AND CONDITIONS')
        self.label1.config(font=('Arial', 13, 'bold'), bg='white', fg='black')
        self.label1.place(x=180, y=10)

        self.conditions_text = Text(self.window, width=96, height=12)
        self.conditions_text.configure(font=('Arial', 8), bg='white', state=NORMAL)
        self.conditions_text.insert(INSERT, '''       
    TÉRMINOS Y CONDICIONES"

    A.  PROHIBIDA SU VENTA O DISTRIBUCIÓN SIN AUTORIZACIÓN DE INFORMATICONFIG.
    B.  PROHIBIDA LA ALTERACIÓN DEL CÓDIGO FUENTE O DISEÑO DE LAS INTERFACES GRÁFICAS.
    C.  INFORMATICONFIG DE ERNESTO NO SE HACE RESPONSABLE DEL MAL USO DE ESTE SOFTWARE.

    LOS ACUERDOS LEGALES EXPUESTOS A CONTINUACION RIGEN EL USO QUE USTED HAGA DE ESTE SOFTWARE
    (INFORMATICONFIG), NO SE RESPONSABILIZA DEL USO QUE USTED"
    HAGA CON ESTE SOFTWARE Y SUS SERVICIOS. PARA ACEPTAR ESTOS TERMINOS HAGA CLIC EN (ACEPTO)"
    SI USTED NO ACEPTA ESTOS TERMINOS, HAGA CLIC EN (NO ACEPTO) Y NO UTILICE ESTE SOFTWARE."
         ''')
        self.conditions_text.place(x=10, y=40)
        self.conditions_text.config(state=DISABLED)

        # Checkbuttons
        self.accept = IntVar()
        self.check_accept = Checkbutton(self.window, text='I Accept', font=('Arial', 12, 'bold'))
        self.check_accept.place(x=10, y=260)

        # Buttons
        self.continuing = Button(self.window, text='Accept', font=('Arial', 11, 'bold'), width=7, height=2, bd=3, state=DISABLED)
        self.continuing.place(x=10, y=290)
        self.cancel = Button(self.window, text='Cancel', font=('Arial', 11, 'bold'), width=7, height=2, bd=3)
        self.cancel.place(x=100, y=290)

        self.window.mainloop()

License()


