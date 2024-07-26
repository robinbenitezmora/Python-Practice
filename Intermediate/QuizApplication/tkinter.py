from tkinter import messagebox
import tkinter as root

class Canvas(object):
    window = None
    def __init__(self, id, title, width, height):
        self.window = root.Tk()
        self.window.title(title)
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        self.window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def show(self):
        self.window.mainloop()
        return
    
    def add(self, widget):
        widget_type = widget.Type
        if widget_type == 'Button' or isinstance (widget, Button):
            freme = self.abs_frame(widget)
            widget.controller = root.Button(freme, text=widget.text, command=widget.callbackMethod)
            widget.controller.pack(fill=root.X, expand=1)

        elif widget_type == 'TextArea' or isinstance (widget, TextArea):
            frame = self.abs_frame(widget)
            widget.controller = root.Text(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)
            widget.controller.insert(root.INSERT, widget.text)

        elif widget_type == 'Label' or isinstance (widget, Label):
            temp = widget.label_var
            widget.label_var = root.StringVar()
            widget.label_var.set(temp)
            frame = self.abs_frame(widget)
            widget.controller = root.Label(frame, textvariable=widget.label_var)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif widget_type == 'CheckBox' or isinstance (widget, CheckBox):
            frame = self.abs_frame(widget)
            var = widget.value
            widget.var = root.IntVar()
            if var:
                widget.var.set(1)
            else:
                widget.value.set(0)
            widget.controller = root.Checkbutton(frame, text=widget.title, variable=widget.value, onvalue=1, offvalue=0)
            widget.controller.grid(sticky=root.W)
            if widget.value:
                widget.controller.select()
            else:
                widget.controller.deselect()

        elif widget_type == 'RadioGroup' or isinstance (widget, RadioGroup):
            frame = self.abs_frame(widget.width, widget.height, widget.positions_X[0], widget.positions_Y[0])
            widget.controller = []
            radio_var = widget.value
            widget.value = set(radio_var)
            radio_controller = root.Radiobutton(frame, text=widget.labels[0], variable=widget.value, value=0)
            radio_controller.pack(fill=root.BOTH, expand=1)
            widget.controller.append(radio_controller)
            for i in range(1, len(widget.labels)):
                frame = self.abs_frame(widget.width, widget.height, widget.positions_X[i], widget.positions_Y[i])
                radio_controller = root.Radiobutton(frame, text=widget.labels[i], variable=widget.value, value=i)
                radio_controller.pack(fill=root.BOTH, expand=1)
                widget.controller.append(radio_controller)

        elif widget_type == 'ValueList' or isinstance (widget, ValueList):
            array = ['']
            array[0] == widget.value
            array += widget.choices
            widget.list_var = root.StringVar()
            widget.list_var.set(array[0])
            frame = self.abs_frame(widget)
            widget.controller = root.OptionMenu(frame, widget.list_var, *array)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif widget_type == 'SpinBox' or isinstance (widget, SpinBox):
            frame = self.abs_frame(widget)
            widget.controller = root.Spinbox(frame, from_=widget.start, to=widget.end)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif widget_type == 'Slider' or isinstance (widget, Slider):
            frame = self.abs_frame(widget)
            widget.controller = root.Scale(frame, from_=widget.start, to=widget.end, orient=root.HORIZONTAL)
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif widget_type == 'Password' or isinstance (widget, Slider):
            frame = self.abs_frame(widget)
            widget.controller = root.Entry(frame, show='*')
            widget.controller.pack(fill=root.BOTH, expand=1)

        elif widget_type == 'TextLine' or isinstance (widget, Slider):
            frame = self.abs_frame(widget)
            widget.controller = root.Entry(frame)
            widget.controller.pack(fill=root.BOTH, expand=1)

    def abs_frame(self, widget):
        frame = root.Frame(self.window, width=widget.width, height=widget.height)
        frame.pack_propagate(0)
        frame.pack()
        frame.place(x=widget.positions_X, y=widget.positions_Y)
        return frame
    
    def abs_frame1(self, W, H, X, Y):
        frame = root.Frame(self.window, width=W, height=H)
        frame.pack_propagate(0)
        frame.pack()
        frame.place(x=X, y=Y)
        return frame
    
class Button(object):
    controller = None
    callbackMethod = None
    Type = None
    def __init__(self, title, X, Y, width, height):
        self.Type = 'Button'
        self.text = title
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height
        self.Type = 'Button'

        def clickListener(self, method):
            if self.controller == None:
                self.callbackMethod = method
            else:
                self.controller.config(command=method)
            return True
        
class Slider(object):
    controller = None
    callaback = None
    Type = 'Slider'
    def __init__(self, X, Y, width, height, start, end):
        self.Type = 'Slider'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height
        self.start = start
        self.end = end

    def getValue(self):
        if self.controller == None:
            return ''
        return self.controller.get()
    
class Password(object):
    controller = None
    callaback = None
    Type = 'Password'
    def __init__(self, X, Y, width, height):
        self.Type = 'Password'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height

    def getText(self):
        if self.controller == None:
            return ''
        return self.controller.get()
    
class TextArea(object):
    controller = None
    callaback = None
    Type = None
    def __init__(self, X, Y, width, height, title):
        self.Type = 'TextArea'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height
        self.text = title

    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.controller.delete(1.0, root.END)
            self.controller.insert(root.INSERT, text)
        return True
    
    def getText(self):
        if self.controller == None:
            return self.text
        return self.controller.get(1.0, root.END)
    
    def appendText(self, text):
        if self.controller == None:
            self.text += text
        else:
            self.controller.insert(root.INSERT, text)
        return True
    
    def clear(self):
        if self.controller == None:
            self.text = ''
        else:
            self.controller.delete(1.0, root.END)
        return True
    
class Label(object):
    controller = None
    Type = None
    label_var = 0
    def __init__(self, X, Y, width, height, text):
        self.Type = 'Label'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height
        self.label_var = text

    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.label_var.set(text)
        return True
    
class CheckBox(object):
    controller = None
    value = False
    Type = None
    def __init__(self, X, Y, width, height, title):
        self.Type = 'CheckBox'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height
        self.title = title

    def setValue(self, value):
        if self.controller == None:
            self.value = value
        else:
            if value:
                self.controller.select()
            else:
                self.controller.deselect()
        return True
    
    def getValue(self):
        if self.controller == None:
            return self.value
        return self.controller.get()
    
class SpinBox(object):
    controller = None
    callback = None
    Type = None
    def __init__(self, X, Y, width, height, start, end):
        self.Type = 'SpinBox'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height
        self.start = start
        self.end = end

    def getValue(self):
        if self.controller == None:
            return ''
        return self.controller.get()
    
class RadioGroup(object):
    controller = []
    selected_index = None
    Type = None
    value = 0
    def __init__(self, width, height):
        self.Type = 'RadioGroup'
        self.width = width
        self.height = height
        self.positions_X = []
        self.positions_Y = []
        self.labels = []

    def addRadioButton(self, label, X, Y):
        self.labels.append(label)
        self.positions_X.append(X)
        self.positions_Y.append(Y)
        return True
    
    def getValue(self):
        for i in range(len(self.controller)):
            if self.value.get() == i:
                return self.labels[i]
        return None
    
    def setButtonTrue(self, index):
        if self.controller == None:
            self.value = index
        else:
            button_controller = self.controller[index]
            button_controller.select()

class TextLine(object):
    controller = None
    callback = None
    Type = 'TextLine'
    def __init__(self, X, Y, width, height):
        self.Type = 'TextLine'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height

    def getText(self):
        if self.controller == None:
            return ''
        return self.controller.get()
    
    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.controller.delete(0, root.END)
            self.controller.insert(0, text)
        return True

    def clear(self):
        if self.controller == None:
            self.text = ''
        else:
            self.controller.delete(0, root.END)
        return True
    
class ValueList(object):
    controller = None
    callback = None
    Type = 'ValueList'
    def __init__(self, X, Y, width, height, value):
        self.Type = 'ValueList'
        self.positions_X = X
        self.positions_Y = Y
        self.width = width
        self.height = height
        self.value = value
        self.choices = []

    def addValue(self, value):
        self.choices.append(value)
        return True
    
    def getValue(self):
        if self.controller == None:
            return ''
        return self.controller.get()
    
    def setValue(self, value):
        if self.controller == None:
            self.value = value
        else:
            self.controller.set(value)
        return True
    
if __name__ == '__main__':
    def SubmitButtonClick(event = None):
        report = ' Your city is ' + ValueList.getValue() + '\n'

        if checkbox1.getValue():
            report += 'You are a student\n'
        else:
            report += 'You are not a student\n'

        if checkbox2.getValue():
            report += 'You are a teacher\n'
        else:
            report += 'You are not a teacher\n'

        report += 'You are a ' + rb1.getValue() + '\n'
        report += 'Your need ' + rb2.getValue() + '\n'

        textarea.appendText(' password: \n' + password.getText() + '\n' + report + '\n' 'Slider value: ' + str(sli.getValue()) + 'Spinbox value: ' + str(spin.getValue()) + '\n')
        return True
    
def AboutButtonClick(event = None):
    textarea.setText('This is a simple quiz application\n')
    return True

Frame = Canvas('Survey', 500, 500)

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Indianapolis', 'San Francisco', 'Columbus', 'Fort Worth', 'Charlotte', 'Detroit', 'El Paso', 'Memphis', 'Boston', 'Seattle', 'Denver', 'Washington', 'Nashville', 'Baltimore', 'Louisville', 'Portland', 'Oklahoma City', 'Milwaukee', 'Las Vegas', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach', 'Kansas City', 'Mesa', 'Atlanta', 'Virginia Beach', 'Omaha', 'Colorado Springs', 'Raleigh', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St. Louis', 'Riverside', 'Corpus Christi', 'Lexington', 'Pittsburgh', 'Anchorage', 'Stockton', 'Cincinnati', 'St. Paul', 'Toledo', 'Greensboro', 'Newark', 'Plano', 'Henderson', 'Lincoln', 'Buffalo', 'Jersey City', 'Chula Vista', 'Fort Wayne', 'Orlando', 'St. Petersburg', 'Chandler', 'Laredo', 'Norfolk', 'Durham', 'Madison', 'Lubbock', 'Irvine', 'Winston-Salem', 'Glendale', 'Garland', 'Hialeah', 'Reno', 'Chesapeake', 'Gilbert', 'Baton Rouge', 'Irving', 'Scottsdale', 'North Las Vegas', 'Fremont', 'Boise', 'Richmond', 'San Bernardino', 'Birmingham', 'Spokane', 'Rochester', 'Des Moines', 'Modesto', 'Fayetteville', 'Tacoma', 'Oxnard', 'Fontana', 'Columbus', 'Montgomery', 'Moreno Valley', 'Shreveport', 'Aurora', 'Yonkers', 'Akron', 'Huntington Beach', 'Little Rock', 'August']

ValueList = ValueList(cities, 100, 100, 100, 100, 'Select your city')
Frame.add(ValueList)

checkbox1 = CheckBox('I have read the code', 100, 200, 100, 100)
Frame.add(checkbox1)

checkbox2 = CheckBox('I have understood the code', 100, 300, 100, 100)
Frame.add(checkbox2)

rb1 = RadioGroup(100, 400)
rb1.addRadioButton('Nice', 100, 400)
rb1.addRadioButton('Good', 100, 450)
rb1.addRadioButton('Very Good', 100, 500)
rb1.addRadioButton('Excellent', 100, 550)
rb1.setButtonTrue(2)

Frame.add(rb1)

rb2 = RadioGroup(100, 600)
rb2.addRadioButton('Option 1', 100, 600)
rb2.addRadioButton('Option 2', 100, 650)
rb2.addRadioButton('Option 3', 100, 700)
rb2.addRadioButton('Option 4', 100, 750)
rb2.setButtonTrue(1)

Frame.add(rb2)

textarea = TextArea('\n Click submit button to see the report', 300, 200, 200, 200)
Frame.add(textarea)

submit = Button('Submit', 300, 400, 100, 100)
about = Button('About', 300, 500, 100, 100)

submit.clickListener(SubmitButtonClick)
about.clickListener(AboutButtonClick)

password = Password(300, 600, 100, 100)
Frame.add(password)
sli = Slider(300, 700, 100, 100, 0, 100)
Frame.add(sli)
spin = SpinBox(300, 800, 100, 100, 0, 100)
Frame.add(spin)
label = Label('This is a simple quiz application', 300, 900, 100, 100)
Frame.add(label)
text = TextLine(300, 1000, 100, 100)
Frame.add(text)
Frame.add(submit)
Frame.add(about)
Frame.show()
