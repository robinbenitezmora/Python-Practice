from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
import tkinter as tk
import datetime as dt

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount
    
    def convert_currency(self):
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        amount = float(self.amount_field.get())
        converted_amount = self.convert(from_currency, to_currency, amount)
        self.converted_amount_field.insert(0, str(converted_amount))

    def init_gui(self):
        self.root = Tk()
        self.root.title("Currency Converter")
        self.root.geometry("500x200")
        self.root.config(bg = "light blue")
        
        self.amount_field = Entry(self.root, bd = 3)
        self.amount_field.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        self.from_currency = ttk.Combobox(self.root, values = list(self.currencies.keys()))
        self.to_currency = ttk.Combobox(self.root, values = list(self.currencies.keys()))
        
        self.from_currency.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.to_currency.grid(row = 2, column = 1, padx = 5, pady = 5)
        
        self.from_currency.set("USD")
        self.to_currency.set("USD")
        
        self.converted_amount_field = Entry(self.root, bd = 3)
        self.converted_amount_field.grid(row = 3, column = 1, padx = 5, pady = 5)
        
        self.result_label = Label(self.root, text = "", bg = "light blue")
        self.result_label.grid(row = 3, column = 0, padx = 5, pady = 5)
        
        self.convert_button = Button(self.root, text = "Convert", command = self.convert_currency)
        self.convert_button.grid(row = 2, column = 0, padx = 5, pady = 5)
        
        self.root.mainloop()

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
converter.init_gui()

