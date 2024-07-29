import os
import sys
from functools import partial

class SurveyWindow(QtGui.Qwidget):
    parent = None
    def __init__(self, id, title, width, height):
        self.app = QtGui.QApplication(sys.argv)
        super(SurveyWindow, self).__init__()
        self.id = id
        self.text = title
        self.width = width
        self.height = height

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Canvas(object):
    window = None
    def __init__(self, id, title, width, height):
        self.window = SurveyWindow(id, title, width, height)
        self.window.center()

    def show(self):
        self.window.setGeometry(self.window.width, self.window.height, self.window.width, self.window.height)
        self.window.setWindowTitle(self.window.text)
        self.window.show()
        sys.exit(self.window.app.exec_())

    def add(self, widget):
        widgetName = type(widget)

        if (widgetName == Checkbox or isinstance(widget, Checkbox)):
            widget.controller = QtGui.QCheckBox(widget.title, self.window)
            widget.contoller.setChecked(widget.value)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

        elif (widgetName == Button or isinstance(widget, Button)):
            widget.controller = QtGui.QPushButton(widget.title, self.window)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

            if widget.callbackMethod is not None:
                widget.controller.clicked.connect(widget.callbackMethod)

        elif (widgetName == Password or isinstance(widget, Password)):
            widget.controller = QtGui.QLineEdit(widget.title, self.window)
            widget.controller.setEchoMode(QtGui.QLineEdit.Password)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

        elif (widgetName == Slider or isinstance(widget, Slider)):
            widget.controller = QtGui.QSlider(QtCore.Qt.Horizontal, self.window)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

        elif (widgetName == SpinBox or isinstance(widget, SpinBox)):
            widget.controller = QtGui.QSpinBox(self.window)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

        elif (widgetName == Label or isinstance(widget, Label)):
            widget.controller = QtGui.QLabel(widget.title, self.window)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

        elif (widgetName == TextLine or isinstance(widget, TextLine)):
            widget.controller = QtGui.QLineEdit(widget.title, self.window)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

        elif (widgetName == TextArea or isinstance(widget, TextArea)):
            widget.controller = QtGui.QTextEdit(widget.title, self.window)
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

        elif (widgetName == RadioGroup or isinstance(widget, RadioGroup)):
            widget.groupBox = QtGui.QGroupBox(widget.title, self.window)
            widget.controller = []
            radio_controller = QtGui.QRadioButton(widget.label[0], widget.groupBox)
            widget.groupBox.resize(widget.width, widget.height)
            radio_controller.move(0, 0)
            widget.controller.append(radio_controller)

            for i in range(1, len(widget.label)):
                radio_controller = QtGui.QRadioButton(widget.label[i], widget.groupBox)
                radio_controller.resize(widget.width, widget.height)
                radio_controller.move(widget.positionX[0], widget.positionY[i] - widget.positionY[0])
                widget.controller.append(radio_controller)

            if widget.selected_position != None:
                widget.controller[widget.selected_position].setChecked(True)

        elif (widgetName == ValueList or isinstance(widget, ValueList)):
            widget.controller = QtGui.QComboBox(self.window)
            widget.controller.addItems(widget.values)
            for i in range(0, len(widget.choices)):
                widget.controller.setItemData(i, widget.choices[i])
            widget.controller.resize(widget.width, widget.height)
            widget.controller.move(widget.positionX, widget.positionY)

class Password(object):
    controller = None
    callback = None

    def __init__(self, X, Y, width, height):
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

    def getText(self):
        if self.controller == None:
            return ''
        return self.controller.text()
    
    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.controller.setText(text)
        return True
    
class Slider(object):
    controller = None
    callback = None

    def __init__(self, start, end, X, Y, width, height):
        self.start = start
        self.end = end
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

    def getValue(self):
        if self.controller == None:
            return ''
        return self.controller.value()
        
class SpinBox(object):
    controller = None
    callback = None

    def __init__(self, start, end, X, Y, width, height):
        self.start = start
        self.end = end
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

    def getValue(self):
        if self.controller == None:
            return ''
        return self.controller.value()
    
class Label(object):
    controller = None
    callback = None

    def __init__(self, text, X, Y, width, height):
        self.title = text
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

class TextLine(object):
    controller = None
    callback = None

    def __init__(self, text, X, Y, width, height):
        self.title = text
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

    def getText(self):
        if self.controller == None:
            return ''
        return self.controller.text()
    
    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.controller.setText(text)
        return True
    
    def clear(self):
        self.controller.setText('')
        return True
    
class TextArea(object):
    controller = None
    callback = None

    def __init__(self, text, X, Y, width, height):
        self.title = text
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

    def getText(self):
        if self.controller == None:
            return ''
        return self.controller.toPlainText()
    
    def setText(self, text):
        if self.controller == None:
            self.text = text
        else:
            self.controller.setText(text)
        return True
    
    def appendText(self, text):
        if self.controller == None:
            self.text += text
        else:
            self.text = self.controller.toPlainText() + text
            self.controller.setText(self.text)
        return True
    
    def clear(self):
        self.controller.setText('')
        return True
    
class Button(object):
    controller = None
    callback = None

    def __init__(self, text, X, Y, width, height):
        self.title = text
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

        def clickListener(self, method):
            if self.controller == None:
                self.callbackMethod = method
            else:
                self.controller.clicked.connect(method)
            return True
        
class Checkbox(object):
    controller = None
    value = False

    def __init__(self, title, X, Y, width, height):
        self.title = title
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

    def setValue(self, value):
        if self.controller == None:
            self.value = value
        else:
            self.controller.setChecked(value)

    def getValue(self):
        if self.controller == None:
            return self.value
        return self.controller.isChecked()
    
class RadioGroup(object):
    controller = None
    selected_position = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.labels = []
        self.positionX = []
        self.positionY = []

        def addRadioButton(self, label, X, Y):
            self.labels.append(label)
            self.positionX.append(X)
            self.positionY.append(Y)
            return True
        
        def getValue(self):
            for i in range(len(self.controller)):
                if self.controller[i].isChecked():
                    return self.labels[i]
            return None
        
        def setButtonTrue(self, position):
            if self.controller == None:
                self.selected_position = position
            else:
                button_controller = self.controller[position]
                button_controller.setChecked(True)

class ValueList(object):
    controller = None

    def __init__(self, choices, X, Y, width, height, value=''):
        self.values = value
        self.choices = choices
        self.positionX = X
        self.positionY = Y
        self.width = width
        self.height = height

    def getValue(self):
        if self.controller == None:
            return self.value 
        else:
            return self.choices[self.controller.currentIndex() - 1]
        
if __name__ == '__main__':
    global i, j

    def SubmitButtonClick(event = None):
        if ValueList.getValue() == 'Maths':
            TextArea.setText('')
            global i
            i = 1
            global j
            j = 0

            TextArea.setText('You are taking a Maths quiz\n')

        if ValueList.getValue() == 'General Knowledge':
            TextArea.setText('')
            global i
            i = 2
            global j
            j = 0

            TextArea.setText('You are taking a General Knowledge quiz\n')

        return True
    
    def NextButtonClick(event = None):
        global i
        global j

        if i == 1:
            if j == 0:
                textarea.setText('QUESTION 1: \n101 is a prime number. True or False?')
                j += 1
            elif j == 1:
                textarea.setText('QUESTION 2: \n729 is divisible by 9. True or False?')
                j += 1
            elif j == 2:
                textarea.setText('YOUR ANSWERS HAVE BEEN SUBMITTED')

        if i == 2:
            if j == 0:
                textarea.setText('QUESTION 1: \nWho is the current president of Nigeria?')
                j += 1
            elif j == 1:
                textarea.setText('QUESTION 2: \nWhat is the capital of Nigeria?')
                j += 1
            elif j == 2:
                textarea.setText('YOUR ANSWERS HAVE BEEN SUBMITTED')

        def AboutButtonClick(event = None):
            textarea.setText('This is a quiz application\n')
            return True
        
        def review(event = None):
            report = '\n\n' + text.getText() + ',\n you selected ' + rb2.getValue() + 'as the difficulty level \n\n You would like to add '

            if checkbox1.getValue():
                report += 'History '

            if checkbox2.getValue():
                report += 'Philosophy '

            if checkbox3.getValue():
                report += 'Geography '

            report += ' subjects in the future\n'
            r = str(spin.getValue())
            report += 'You rated the application ' + r + ' out of 10\n'

            textarea1.appendText(report)
            return True
        
        Frame = Canvas(1, 'Survey ', 500, 500)

        cities = ['General Knowledge', 'Maths']
        valuelist = ValueList(cities, 80, 30, 200, 30, 'Choose a quiz subject')
        Frame.add(valuelist)

        rb1 = RadioGroup(100, 100)
        rb1.addRadioButton('TRUE', 475, 210)
        rb1.addRadioButton('FALSE', 475, 230)
        rb1.setButtonTrue(0)
        Frame.add(rb1)

        rb2 = RadioGroup(100, 100)
        rb2.addRadioButton('Easy', 475, 210)
        rb2.addRadioButton('Medium', 475, 230)
        rb2.addRadioButton('Hard', 475, 250)
        rb2.setButtonTrue(0)
        Frame.add(rb2)

        textarea = TextArea('\n Question will be displayed here', 20, 20, 400, 200)
        Frame.add(textarea)
        textarea1 = TextArea('\nYour Review will be displayed here', 20, 20, 400, 200)
        Frame.add(textarea1)
        submit = Button('Start Quiz', 20, 400, 100, 30)
        about = Button('About', 150, 400, 100, 30)
        nextbtn = Button('Next', 280, 400, 100, 30)
        Frame.add(submit)
        submit.clickListener(review)
        nextbtn.clickListener(NextButtonClick)
        Frame.add(nextbtn)
        submit.clickListener(SubmitButtonClick)
        about.clickListener(AboutButtonClick)

        label3 = Label('Difficulty Level', 20, 200, 100, 30)
        label4 = Label('Selected the topics you would like to add in the future', 20, 250, 300, 30)
        Frame.add(label4)
        checkbox1 = Checkbox('History', 20, 280, 100, 30)
        Frame.add(checkbox1)
        checkbox2 = Checkbox('Philosophy', 20, 310, 100, 30)
        Frame.add(checkbox2)
        checkbox3 = Checkbox('Geography', 20, 340, 100, 30)
        Frame.add(checkbox3)
        label6 = Label('Please enter username and password', 20, 400, 300, 30)
        Frame.add(label6)
        password = Password(20, 430, 100, 30)
        Frame.add(password)
        sli = Slider(0, 100, 20, 460, 100, 30)
        Frame.add(sli)
        spin = SpinBox(0, 100, 20, 490, 100, 30)
        Frame.add(spin)
        label = label('How was your quiz experience?', 20, 520, 300, 30)
        Frame.add(label)
        label1 = Label('Select the subject whose Quiz you want to take', 20, 20, 300, 30)
        Frame.add(label1)
        label9 = Label('Number of questions you would like to have in the next quiz', 20, 490, 300, 30)
        Frame.add(label9)
        label7 = Label('Username', 20, 430, 100, 30)
        Frame.add(label7)
        label8 = Label('Password', 20, 460, 100, 30)
        Frame.add(label8)
        text = TextLine('', 20, 520, 300, 30)
        Frame.add(text)

        Frame.show()