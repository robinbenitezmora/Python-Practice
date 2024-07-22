import gtk

class Canvas:
    def __init__(self, id, title, width, height):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect('destroy', gtk.main_quit)
        self.window.set_title(title)
        self.window.set_default_size(width, height)
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.show()

    def show(self):
        self.window.show()
        gtk.main()
        return
    
    def add(self, widget):
        widget_type = type(widget)
        print(widget_type)
        if widget_type == Button:
            widget.controller = gtk.Button(widget.text)
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()
            if widget.callbackMethod:
                widget.controller.connect('clicked', widget.callbackMethod)

        elif widget_type == TextArea:
            widget.controller = gtk.TextView(widget.buffer)
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()
            if widget.callbackMethod != None:
                widget.controller.connect('clicked', widget.callbackMethod)

        elif widget_type == TextLine:
            widget.controller = gtk.Entry()
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()

        elif widget_type == CheckBox:
            widget.controller = gtk.CheckButton(widget.title)
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()
            widget.controller.set_active(widget.value)

        elif widget_type == Password:
            widget.controller = gtk.Entry()
            widget.controller.set_visibility(0)
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()

        elif widget_type == Slider:
            widget.controller = gtk.HScale()
            widget.controller.set_range(widget.start, widget.end)
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()

        elif widget_type == SpinBox:
            widget.controller = gtk.SpinButton()
            widget.controller.set_range(widget.start, widget.end)
            widget.controller.set_increment(1, 1)
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()

        elif widget_type == Label:
            widget.controller = gtk.Label(widget.text)
            widget.controller.set_size_request(widget.width, widget.height)
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)
            widget.controller.show()

        elif widget_type == RadioGroup:
            widget.controller = []
            radio_controller = gtk.RadioButton(None, widget.labels[0])
            radio_controller.set_size_request(widget.width, widget.height)
            self.fixed.put(radio_controller, widget.posit_x[0], widget.posit_y[0])
            radio_controller.show()
            widget.controller.append(radio_controller)
            for i in range(len(1, len(widget.labels))):
                radio_controller = gtk.RadioButton(widget.controller[0], widget.labels[i])
                radio_controller.set_size_request(widget.width, widget.height)
                self.fixed.put(radio_controller, widget.posit_x[i], widget.posit_y[i])
                radio_controller.show()
                widget.controller.append(radio_controller)

            if widget.selected_position != None:
                widget.controller[widget.selected_position].set_active(True)

        elif widget_type == ValueList:
            widget.controller = gtk.OptionMenu()
            widget.contoller.set_size_request(widget.width, widget.height)
            menu = gtk.Menu()
            for name in widget.choices:
                item = gtk.MenuItem(name)
                item.show()
                menu.append(item)
            widget.controller.set_menu(menu)
            widget.controller.show()
            self.fixed.put(widget.controller, widget.posit_x, widget.posit_y)

class Button(gtk.Button):
    controller = None
    callbackMethod = None
    def __init__(self, text, X, Y, width, height):
        self.text = text
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y

    def clickListener(self, method):
        if self.controller == None:
            self.callbackMethod = method
        else:
            self.controller.connect('clicked', method)
        return True
    
class TextArea:
    controller = None
    callbackMethod = None
    def __init__(self, title, X, Y, width, height):
        self.text = title
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y

    def setText(self, text):
        self.buffer.set_text(text)
        return True
    
    def appendText(self, text):
        self.buffer.insert(self.buffer.get_end_iter(), text)
        return True
    
    def clear(self):
        self.buffer.set_text('')
        return True

class Password:
    controller = None
    callback = None
    def __init__(self, X, Y, width, height):
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y

    def getText(self):
        if self.controller == None:
            return ''
        else:
            return self.controller.get_text()
        
    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.controller.set_text(text)
        return True
    
    def clear(self):
        if self.controller != None:
            self.controller.set_text('')
        return True
    
class Slider:
    controller = None
    callback = None
    def __init__(self, X, Y, width, height, start, end):
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y
        self.start = start
        self.end = end

    def getValue(self):
        if self.controller == None:
            return ''
        else:
            return self.controller.get_value()
        
class SpinBox:
    controller = None
    callback = None
    def __init__(self, X, Y, width, height, start, end):
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y
        self.start = start
        self.end = end

    def getValue(self):
        if self.controller == None:
            return ''
        else:
            return self.controller.get_value()
        
class Label(object):
    controller = None
    callback = None
    def __init__(self, text, X, Y, width, height):
        self.text = text
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y

class TextLine(object):
    controller = None
    callback = None
    def __init__(self, X, Y, width, height):
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y

    def getText(self):
        if self.controller == None:
            return ''
        else:
            return self.controller.get_text()
        
    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.controller.set_text(text)
        return True
    
    def clear(self):
        if self.controller != None:
            self.controller.set_text('')
        return True
    
class CheckBox(gtk.CheckButton):
    controller = None
    value = False
    def __init__(self, title, X, Y, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y

    def getValue(self):
        if self.controller == None:
            return self.value
        else:
            return self.controller.get_active()
        
    def setValue(self, value):
        if value != True or value != False:
            return
        if self.controller == None:
            self.value = value
        else:
            self.controller.set_active(value)
        return True
    
class RadioGroup(gtk.RadioButton):
    GroupController = None
    controller = None
    selected_position = None
    def __init__(self, width, height):
        self.labels = []
        self.width = width
        self.height = height
        self.posit_x = []
        self.posit_y = []
        self.GroupController = None

    def addRadioButton(self, label, X, Y):
        self.labels.append(label)
        self.posit_x.append(X)
        self.posit_y.append(Y)
        return True
    
    def getValue(self):
        for i in range(len(self.controller)):
            if self.controller[i].get_active():
                return self.labels[i]
        return 'None'
    
    def setButtonTrue(self, position):
        if self.controller == None:
            self.selected_position = position
        else:
            buton_controller = self.controller[position]
            buton_controller.set_active(True)

class ValueList(gtk.OptionMenu):
    controller = None
    def __init__(self, choices, X, Y, width, height, value = ''):
        self.value = value
        self.width = width
        self.height = height
        self.posit_x = X
        self.posit_y = Y
        self.title = ''
        temp = [value]

        for i in range(len(choices)):
            temp.append(choices[i])
        self.choices = temp

    def getValue(self):
        if self.controller == None:
            return self.value
        else:
            IntValue = self.controller.get_history()
            if IntValue < 0:
                return None
            return self.choices[IntValue]
        
if __name__ == '__main__':
    def SubmitButtonClick(event = None):
        report = 'You are giving your review of the following dishes of ' + relist.getValue() + ' .\n' + ValueList.getValue() + '\n'

        if checkbox1.getValue():
            report += 'Pizza\n'

        if checkbox2.getValue():
            report += 'Burger\n'

        if checkbox3.getValue():
            report += 'Pasta\n'

        if checkbox4.getValue():
            report += 'Sandwich\n'

        report += 'You felt food was ---> ' + rb1.getValue() + '.\n'

        if rb2.getValue() == 'Not for me':
            report += 'You would not revisit the restaurant.\n'
        else:
            report += 'You would revisit the restaurant.\n'

        sli = Slider(0, 0, 0, 0, 0, 0)  # Replace the values with appropriate values for the Slider
        textarea.appendText(report + '\n' + ' Slider value: ' + str(sli.getValue()) + '\n')

        return True
    
    def AboutButtonClick(event = None):
        textarea.setText('This is a quiz application.\n')

        return True
    
    Frame = Canvas(1, 'Quiz Application', 810, 600)

    cities = ['Roma', 'Paris', 'New York', 'London', 'Tokyo', 'Delhi', 'Beijing', 'Moscow', 'Cairo', 'Sydney']
    restaurants = ['Pizza Hut', 'McDonalds', 'Dominos', 'Subway', 'KFC', 'Burger King', 'Starbucks', 'Dunkin Donuts', 'Taco Bell', 'Papa Johns']

    valuelist = ValueList(cities, 100, 100, 100, 30, ' Select City')
    relist = ValueList(restaurants, 100, 100, 100, 30, ' Select Restaurant')
    Frame.add(valuelist)
    Frame.add(relist)

    checkbox1 = CheckBox('Pizza', 100, 130, 100, 30)
    checkbox2 = CheckBox('Burger', 100, 160, 100, 30)
    checkbox3 = CheckBox('Pasta', 100, 190, 100, 30)
    checkbox4 = CheckBox('Sandwich', 100, 220, 100, 30)

    checkbox1.setValue(True)
    Frame.add(checkbox1)
    Frame.add(checkbox2)
    Frame.add(checkbox3)
    Frame.add(checkbox4)

    rb1 = RadioGroup(100, 30)
    rb1.addRadioButton('Excellent', 100, 250)
    rb1.addRadioButton('Good', 100, 280)
    rb1.addRadioButton('Average', 100, 310)
    rb1.addRadioButton('Poor', 100, 340)
    rb1.addRadioButton('Very Poor', 100, 370)
    rb1.setButtonTrue(1)

    Frame.add(rb1)

    rb2 = RadioGroup(100, 30)
    rb2.addRadioButton('Yes', 100, 400)
    rb2.addRadioButton('No', 100, 430)
    rb2.addRadioButton('Not for me', 100, 460)
    rb2.setButtonTrue(0)

    Frame.add(rb2)

    textarea = TextArea('This is a quiz application.\n', 100, 500, 600, 100)
    Frame.add(textarea)

    submit = Button('Submit', 100, 600, 100, 30)
    about = Button('About', 200, 600, 100, 30)
    submit.clickListener(SubmitButtonClick)
    about.clickListener(AboutButtonClick)
    Frame.add(submit)
    Frame.add(about)
    Frame.show()