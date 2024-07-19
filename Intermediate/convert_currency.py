from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
import tkinter as tk
import datetime as dt
import re

class CurrencyConverter:
    def __init__(self, url):
        self.url = 'https://api.exchangerate.host/latest'
        self.response = requests.get(url)
        self.data = self.response.json()
        self.rates = self.data['rates']

    def convert(self, amount, base_currency, des_currency):
        if base_currency != 'EUR':
            amount = amount / self.rates[base_currency]

        amount = round(amount * self.rates[des_currency], 4)
        return amount
    
class Main(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.currency_converter = converter

        self.geometry("500x200")
        self.configure(bg = 'light blue')
        self.intro_label = Label(self, text = 'Welcome to Real Time Currency Convertor',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font = ('Courier',15,'bold'))

        self.date_label = Label(self, text = f"Date : {dt.datetime.now().date()}", relief = tk.GROOVE, borderwidth = 5)
        self.date_label.config(font = ('Courier', 10, 'bold'))

        self.intro_label.place(x = 10 , y = 5)
        self.date_label.place(x = 350, y = 5)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd = 3, relief = tk.RIDGE, justify = tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
        
        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("EUR") # default value

        font = ('Courier', 12, 'bold')
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable = self.from_currency_variable, values = list(self.currency_converter.rates.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable = self.to_currency_variable, values = list(self.currency_converter.rates.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x = 30, y = 120)
        self.amount_field.place(x = 36, y = 150)
        self.to_currency_dropdown.place(x = 340, y = 120)
        self.converted_amount_field_label.place(x = 346, y = 150)

        # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform)
        self.convert_button.config(font = ('Courier', 10, 'bold'))
        self.convert_button.place(x = 225, y = 135)

    def perform(self):
        amount = float(self.amount_field.get())
        base_currency = self.from_currency_variable.get()
        to_currency = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(amount, base_currency, to_currency)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text = str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))
    
if __name__ == '__main__':
    url = 'https://api.exchangerate.host/latest'
    converter = CurrencyConverter(url)

    Main(converter)
    mainloop()
