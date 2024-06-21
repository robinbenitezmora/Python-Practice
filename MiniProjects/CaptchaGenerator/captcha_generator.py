from io import BytesIO
from tkinter import *
from random import *
import string
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['C:/Users/Administrator/Downloads/ChelseaMarketsr.ttf', 'C:/Users/Administrator/Downloads/DejaVuSanssr.ttf'])
random = str(randint(100000, 999999))
assert isinstance(data, BytesIO)
image.write(random, 'out.png')

def verify():
    global random
    x = t1.get('0.0', END)

    if (int(x) == int(random)):
        messagebox.showinfo('Success', 'Verified')
    else:
        messagebox.showerror('Alert', 'Not Verified')
        refresh()

def refresh():
    random = str(randint(100000, 99999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, 'out.png')
    photo = PhotoImage(file='out.png')
    l1.config(image=photo, heigth=100, width=200)
    l1.update()
    UpdateLabel()

root = Tk()
photo = PhotoImage(file='out.png')

l1 = Label(root, image=photo, heigth=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text='Submit', command=verify)
b2 = Button(root, text='Refresh', command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()




