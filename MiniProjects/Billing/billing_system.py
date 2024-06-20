from tkinter import*
import random
import os
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")

        bg_color = "#074463"
        title = Label(self.root, text="Billing System", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg='#badc57', fg='Black', relief=GROOVE)
        title.pack(fill=X)

        # ============ Variables ============
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal = IntVar()

        # ============ Grocery ===============
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.fluor = IntVar()
        self.maggi = IntVar()

        # ============ Cold Drinks ===============
        self.sprite = IntVar()
        self.coke = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()

        # ============ Total Product Price & Tax Variables ===============
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        # ============ Customer ==============
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ============ Customer retail details ===============
        F1 = LabelFrame(self.root, text='Customer Details', font=('times new roman', 15, 'bold'), bd=10, fg='Black', bg='#badc57')
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="Bill Number:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cbill_lbl.grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        cbill_txt.grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font='arial 12 bold').grid(row=0, column=6, padx=10, pady=10)
        bill_btn.grid(row=0, column=6, pady=5, padx=10)

        # ============ Medical Details ===============
        F2 = LabelFrame(self.root, text='Medical Details', font=('times new roman', 15, 'bold'), bd=10, fg='Black', bg='#badc57')
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer:", bg=bg_color, font=('times new roman', 15, 'bold'))
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10)
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 15, 'bold'))
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask:", bg=bg_color, font=('times new roman', 15, 'bold'))
        mask_lbl.grid(row=1, column=0, padx=10, pady=10)
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 15, 'bold'))
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves:", bg=bg_color, font=('times new roman', 15, 'bold'))
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10)
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 15, 'bold'))
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        dettol_lbl = Label(F2, text="Dettol:", bg=bg_color, font=('times new roman', 15, 'bold'))
        dettol_lbl.grid(row=3, column=0, padx=10, pady=10)
        dettol_txt = Entry(F2, width=10, textvariable=self.dettol, font=('times new roman', 15, 'bold'))
        dettol_txt.grid(row=3, column=1, padx=10, pady=10)

        newsprin_lbl = Label(F2, text="Newsprin:", bg=bg_color, font=('times new roman', 15, 'bold'))
        newsprin_lbl.grid(row=4, column=0, padx=10, pady=10)
        newsprin_txt = Entry(F2, width=10, textvariable=self.newsprin, font=('times new roman', 15, 'bold'))
        newsprin_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_lbl = Label(F2, text="Thermal:", bg=bg_color, font=('times new roman', 15, 'bold'))
        thermal_lbl.grid(row=5, column=0, padx=10, pady=10)
        thermal_txt = Entry(F2, width=10, textvariable=self.thermal, font=('times new roman', 15, 'bold'))
        thermal_txt.grid(row=5, column=1, padx=10, pady=10)

        # ============ Grocery Items ===============
        F3 = LabelFrame(self.root, text='Grocery Items', font=('times new roman', 15, 'bold'), bd=10, fg='Black', bg='#badc57')
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice:", bg=bg_color, font=('times new roman', 15, 'bold'))
        rice_lbl.grid(row=0, column=0, padx=10, pady=10)
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 15, 'bold'))
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil:", bg=bg_color, font=('times new roman', 15, 'bold'))
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10)
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 15, 'bold'))
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal:", bg=bg_color, font=('times new roman', 15, 'bold'))
        daal_lbl.grid(row=2, column=0, padx=10, pady=10)
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('times new roman', 15, 'bold'))
        daal_txt.grid(row=2, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat:", bg=bg_color, font=('times new roman', 15, 'bold'))
        wheat_lbl.grid(row=3, column=0, padx=10, pady=10)
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 15, 'bold'))
        wheat_txt.grid(row=3, column=1, padx=10, pady=10)

        fluor_lbl = Label(F3, text="Flour:", bg=bg_color, font=('times new roman', 15, 'bold'))
        fluor_lbl.grid(row=4, column=0, padx=10, pady=10)
        fluor_txt = Entry(F3, width=10, textvariable=self.fluor, font=('times new roman', 15, 'bold'))
        fluor_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi:", bg=bg_color, font=('times new roman', 15, 'bold'))
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10)
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 15, 'bold'))
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

        # ============ Cold Drinks ===============
        F4 = LabelFrame(self.root, text='Cold Drinks', font=('times new roman', 15, 'bold'), bd=10, fg='Black', bg='#badc57')
        F4.place(x=675, y=180, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite:", bg=bg_color, font=('times new roman', 15, 'bold'))
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10)
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 15, 'bold'))
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke:", bg=bg_color, font=('times new roman', 15, 'bold'))
        coke_lbl.grid(row=1, column=0, padx=10, pady=10)
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 15, 'bold'))
        coke_txt.grid(row=1, column=1, padx=10, pady=10)

        limka_lbl = Label(F4, text="Limka:", bg=bg_color, font=('times new roman', 15, 'bold'))
        limka_lbl.grid(row=2, column=0, padx=10, pady=10)
        limka_txt = Entry(F4, width=10, textvariable=self.limka, font=('times new roman', 15, 'bold'))
        limka_txt.grid(row=2, column=1, padx=10, pady=10)

        mazza_lbl = Label(F4, text="Mazza:", bg=bg_color, font=('times new roman', 15, 'bold'))
        mazza_lbl.grid(row=3, column=0, padx=10, pady=10)
        mazza_txt = Entry(F4, width=10, textvariable=self.mazza, font=('times new roman', 15, 'bold'))
        mazza_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta:", bg=bg_color, font=('times new roman', 15, 'bold'))
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10)
        fanta_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 15, 'bold'))
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F4, text="Mountain Duo:", bg=bg_color, font=('times new roman', 15, 'bold'))
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10)
        mountain_duo_txt = Entry(F4, width=10, textvariable=self.mountain_duo, font=('times new roman', 15, 'bold'))
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

        # ============ Bill Area ===============
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=340, height=380)

        bill_title = Label(F5, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ============ Button Frame ===============
        F6 = LabelFrame(self.root, text='Bill Menu', font=('times new roman', 15, 'bold'), bd=10, fg='Black', bg='#badc57')
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text='Total Medical Price', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=20, pady=1)
        m1_lbl.grid(row=0, column=0, padx=20, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text='Total Grocery Price', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(row=1, column=0, padx=20, pady=1)
        m2_lbl.grid(row=1, column=0, padx=20, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text='Total Cold Drinks Price', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(row=2, column=0, padx=20, pady=1)
        m3_lbl.grid(row=2, column=0, padx=20, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text='Total Cold Drinks Price', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(row=2, column=0, padx=20, pady=1)
        m4_lbl.grid(row=2, column=0, padx=20, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
        m4_txt.grid(row=2, column=1, padx=18, pady=1)

        m5_lbl = Label(F6, text='Total Cold Drinks Price', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(row=2, column=0, padx=20, pady=1)
        m5_lbl.grid(row=2, column=0, padx=20, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
        m5_txt.grid(row=2, column=1, padx=18, pady=1)

        m6_lbl = Label(F6, text='Total Cold Drinks Price', bg=bg_color, fg='white', font=('times new roman', 15, 'bold')).grid(row=2, column=0, padx=20, pady=1)
        m6_lbl.grid(row=2, column=0, padx=20, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)
        m6_txt.grid(row=2, column=1, padx=18, pady=1)

        # ============== Buttons ===============
        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text='Total', bg='cadetblue', fg='white', pady=15, width=10, bd=5, font='arial 15 bold').grid(row=0, column=0, padx=5, pady=5)
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generate_bill_btn = Button(btn_F, command=self.bill_area, text='Generate Bill', bg='cadetblue', fg='white', pady=15, width=10, bd=5, font='arial 15 bold').grid(row=0, column=1, padx=5, pady=5)
        generate_bill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_F, command=self.clear_data, text='Clear', bg='cadetblue', fg='white', pady=15, width=10, bd=5, font='arial 15 bold').grid(row=0, column=2, padx=5, pady=5)
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_F, command=self.exit_app, text='Exit', bg='cadetblue', fg='white', pady=15, width=10, bd=5, font='arial 15 bold').grid(row=0, column=3, padx=5, pady=5)
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

        # ============== totalBill =================

    def total(self):
        self.total_medical_price = (self.sanitizer.get() * 50 +
                                    self.mask.get() * 40 +
                                    self.hand_gloves.get() * 30 +
                                    self.dettol.get() * 120 +
                                    self.newsprin.get() * 20 +
                                    self.thermal.get() * 150)

        self.medical_price.set("Rs. " + str(self.total_medical_price))

        self.total_grocery_price = (self.rice.get() * 40 +
                                    self.food_oil.get() * 120 +
                                    self.daal.get() * 60 +
                                    self.wheat.get() * 30 +
                                    self.fluor.get() * 20 +
                                    self.maggi.get() * 12)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))

        self.total_cold_drink_price = (self.sprite.get() * 50 +
                                    self.coke.get() * 40 +
                                    self.limka.get() * 30 +
                                    self.mazza.get() * 120 +
                                    self.fanta.get() * 20 +
                                    self.mountain_duo.get() * 150)

        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))

        self.total_bill = self.total_medical_price + self.total_grocery_price + self.total_cold_drink_price




















