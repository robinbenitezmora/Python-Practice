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
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_s_p = self.sanitizer.get()*2
        self.m_m_p = self.mask.get()*5
        self.m_d_p = self.dettol.get()*30
        self.m_n_p = self.newsprin.get()*5
        self.m_t_g_p = self.thermal_gun.get()*15
        self.total_medical_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.medical_price.set('Rs. ' + str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set('Rs ' + str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.food_oil.get()*10
        self.g_d_p = self.daal.get()*6
        self.g_w_p = self.wheat.get()*10
        self.g_f_p = self.flour.get()*8
        self.g_m_p = self.maggi.get()*5
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_d_p+self.g_w_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set('Rs. ' + str(self.total_grocery_price))
        self.c_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set('Rs ' + str(self.c_tax))

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_l_p = self.limka.get()*10
        self.c_d_c_p = self.coke.get()*15
        self.c_d_m_p = self.mazza.get()*10
        self.c_d_f_p = self.fanta.get()*15
        self.c_d_m_d_p = self.mountain_duo.get()*10
        self.total_cold_drink_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_c_p+self.c_d_m_p+self.c_d_f_p+self.c_d_m_d_p)

        self.cold_drink_price.set('Rs. ' + str(self.total_cold_drink_price))
        self.c_tax = round((self.total_cold_drink_price * 0.05), 2)
        self.cold_drink_tax.set('Rs ' + str(self.c_tax))

        self.Total_bill = float(self.total_medical_price+self.total_grocery_price+self.total_cold_drink_price+self.c_tax)

        # ============= Welcome Bill ==============
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, '\tWelcome Webcode Retail\n')
        self.txtarea.insert(END, '\n')
        self.txtarea.insert(END, f'\n Bill Number : {self.bill_no.get()}')
        self.txtarea.insert(END, f'\n Customer Name : {self.c_name.get()}')
        self.txtarea.insert(END, f'\n Phone Number : {self.c_phone.get()}')
        self.txtarea.insert(END, f'\n =====================================')
        self.txtarea.insert(END, f'\n Products\t\tQTY\t\tPrice')
        self.txtarea.insert(END, f'\n =====================================')

        # ============= Bill Area ==============
    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # ============= Medical ==============
            if self.sanitizer.get() != 0:
                self.txtarea.insert(END, f'\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}')
            if self.mask.get() != 0:
                self.txtarea.insert(END, f'\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}')
            if self.hand_gloves.get() != 0:
                self.txtarea.insert(END, f'\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}')
            if self.dettol.get() != 0:
                self.txtarea.insert(END, f'\n Dettol\t\t{self.dettol.get()}\t\t{self.m_d_p}')
            if self.newsprin.get() != 0:
                self.txtarea.insert(END, f'\n Newsprin\t\t{self.newsprin.get()}\t\t{self.m_n_p}')
            if self.thermal.get() != 0:
                self.txtarea.insert(END, f'\n Thermal Gun\t\t{self.thermal.get()}\t\t{self.m_t_g_p}')

            # ============= Grocery ==============
            if self.rice.get() != 0:
                self.txtarea.insert(END, f'\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}')
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f'\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}')
            if self.daal.get() != 0:
                self.txtarea.insert(END, f'\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}')
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f'\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}')
            if self.flour.get() != 0:
                self.txtarea.insert(END, f'\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}')
            if self.maggi.get() != 0:
                self.txtarea.insert(END, f'\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}')

            # ============= Cold Drinks ==============
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f'\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}')
            if self.limka.get() != 0:
                self.txtarea.insert(END, f'\n Limka\t\t{self.limka.get()}\t\t{self.c_d_l_p}')
            if self.coke.get() != 0:
                self.txtarea.insert(END, f'\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}')
            if self.mazza.get() != 0:
                self.txtarea.insert(END, f'\n Mazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}')
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f'\n Fanta\t\t{self.fanta.get()}\t\t{self.c_d_f_p}')
            if self.mountain_duo.get() != 0:
                self.txtarea.insert(END, f'\n Mountain Dew\t\t{self.mountain_duo.get()}\t\t{self.c_d_m_d_p}')

            # ============ Taxes ==============
            if self.medical_tax.get() != '0.0':
                self.txtarea.insert(END, f'\n -------------------------------------')
                self.txtarea.insert(END, f'\n Medical Tax\t\t\t\t{self.medical_tax.get()}')
            if self.grocery_tax.get() != '0.0':
                self.txtarea.insert(END, f'\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}')
            if self.cold_drink_tax.get() != '0.0':
                self.txtarea.insert(END, f'\n Cold Drink Tax\t\t\t\t{self.cold_drink_tax.get()}')

            self.txtarea.insert(END, f'\n Total Bill : \t\t\t Rs. {self.Total_bill}')
            self.txtarea.insert(END, f'\n -------------------------------------')
            self.save_bill()

            # ============ Save Bill =============
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill No. : {self.bill_no.get()} Saved Successfully")
        else:
            return

        # ============ Find Bill =============
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

        # ============ Clear Data =============
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear the data?")
        if op > 0:
            # ============ Medical ==============
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.newsprin.set(0)
            self.thermal.set(0)

            # ============ Grocery ==============
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.flour.set(0)
            self.maggi.set(0)

            # ============ Cold Drinks ==============
            self.sprite.set(0)
            self.coke.set(0)
            self.limka.set(0)
            self.mazza.set(0)
            self.fanta.set(0)
            self.mountain_duo.set(0)

            # ============ Total Product Price & Tax Variables ==============
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            # ============ Customer ==============
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")

            self.welcome_bill()

        # ============ Exit App =============
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()
        