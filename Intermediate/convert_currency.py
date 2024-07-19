from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
import tkinter as tk
import datetime as dt

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
    
    def get_rates(self):
        return self.rates
    
    def get_currencies(self):
        return self.rates.keys()
    
class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Currency Converter')
        self.root.geometry('500x300')
        self.root.resizable(False, False)
        
        self.currency_converter = CurrencyConverter('https://api.exchangerate.host/latest')
        
        self.amount = DoubleVar()
        self.base_currency = StringVar()
        self.des_currency = StringVar()
        self.result = StringVar()
        
        self.base_currency.set('USD')
        self.des_currency.set('EUR')
        
        self.create_widgets()
    
    def create_widgets(self):
        amount_label = Label(self.root, text='Amount:', font=('Arial', 12))
        amount_label.place(x=50, y=50)
        
        amount_entry = Entry(self.root, textvariable=self.amount, font=('Arial', 12))
        amount_entry.place(x=150, y=50)
        
        base_currency_label = Label(self.root, text='From Currency:', font=('Arial', 12))
        base_currency_label.place(x=50, y=100)
        
        base_currency_combobox = ttk.Combobox(self.root, textvariable=self.base_currency, values=list(self.currency_converter.get_currencies()), font=('Arial', 12))
        base_currency_combobox.place(x=150, y=100)
        
        des_currency_label = Label(self.root, text='To Currency:', font=('Arial', 12))
        des_currency_label.place(x=50, y=150)
        
        des_currency_combobox = ttk.Combobox(self.root, textvariable=self.des_currency, values=list(self.currency_converter.get_currencies()), font=('Arial', 12))
        des_currency_combobox.place(x=150, y=150)
        
        convert_button = Button(self.root, text='Convert', font=('Arial', 12), command=self.convert)
        convert_button.place(x=200, y=200)
        
        result_label = Label(self.root, text='Result:', font=('Arial', 12))
        result_label.place(x=50, y=250)
        
        result_entry = Entry(self.root, textvariable=self.result, font=('Arial', 12))
        result_entry.place(x=150, y=250)
    
    def convert(self):
        try:
            amount = float(self.amount.get())
            base_currency = self.base_currency.get()
            des_currency = self.des_currency.get()
            
            result = self.currency_converter.convert(amount, base_currency, des_currency)

            self.result.set(result)
        except:
            messagebox.showerror('Error', 'Invalid input')

root = Tk()
app = CurrencyConverterApp(root)
root.mainloop()
