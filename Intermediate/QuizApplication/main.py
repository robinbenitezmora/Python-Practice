
import sys
import anygui # type: ignore

#************************************************************
def Main():
    sampleProgram()

def sampleProgram():
    print('Enter your choice:\n')
    print('1. pyGTK GUI\n')
    print('2. wXPython GUI\n')
    print('3. pyQT GUI\n')
    print('4. tkinter\n')
    print('5. Exit\n')

    loop = 0

    while loop == 0:
        try:
            x = int(input())
            loop = 1
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5\n')
            loop = 0

    if x == 1:
        import gi.repository as anygui # type: ignore

    elif x == 2:
        import wxpython as anygui # type: ignore

    elif x == 3:
        import pyqt as anygui # type: ignore

    elif x == 4:
        import tkinter as anygui

    elif x == 5:
        sys.exit()

    else:
        print('Invalid input. Please enter a number between 1 and 5\n')
        sampleProgram()

    if x != 1 and x != 2 and x != 3 and x != 4:
        sys.exit()

def SubmitButtonClick(event = None):
    report = 'You are giving your review of the following disshes of ' + valuelist.getValue() + ' .\n' + valuelist.getValue() + '\n'
    
    if checkbox1.getValue():
        report += 'Pizza\n'

    if checkbox2.getValue():
        report += 'Burger\n'

    if checkbox3.getValue():
        report += 'Pasta\n'

    checkbox4 = anygui.CheckBox('Sandwich', 100, 160) # type: ignore
    Frame.add(checkbox4)
    
    if checkbox4.getValue():
        report += 'Sandwich\n'

    if checkbox5.getValue(): # type: ignore
        report += 'Noodles\n'

    if checkbox6.getValue(): # type: ignore
        report += 'Momos\n'

    if checkbox7.getValue(): # type: ignore
        report += 'Spring Rolls\n'

    if checkbox8.getValue(): # type: ignore
        report += 'Manchurian\n'

    if checkbox9.getValue(): # type: ignore
        report += 'Chowmein\n'

    if checkbox10.getValue(): # type: ignore
        report += 'Chilli Potato\n'

    report += 'You felt food was ' + rb1.getValue() + ' and service was ' + rb2.getValue() + '.\n'

    if rb2.getValue() == 'Not for me':
        report += 'You would not revisit the restaurant.\n'
    else:
        report += 'You would revisit the restaurant.\n'

    textarea.appendText(report + '\n' + ' Slider value: ' + str(sli.getValue()) + '\n')

    return True

def AboutButtonClick(event = None):
    textarea.setText('This is a quiz application.\n')

    return True

Frame = anygui.Canvas(1, 'Quiz Application', 810, 600)
global i, j

def SubmitButtonClick(event = None):
    if valuelist.getValue() == 'Maths':
        textarea.setText('')
        global i
        i = 1
        global j
        j = 0

        textarea.setText('You are taking a quiz on Maths.\n')

    if valuelist.getValue() == 'General Knowledge':
        textarea.setText('')
        global i
        i = 2
        global j
        j = 0

        textarea.setText('You are taking a quiz on General Knowledge.\n')

        return True
    
def nextbuttonclick(event = None):
    global i
    global j

    if i == 1:
        if j == 0:
            textarea.setText('QUESTION 1: \n101 is a prime number.\n')
            j += 1
        elif j == 1:
            textarea.setText('QUESTION 2: \n729 is a perfect square.\n')
            j += 1
        elif j == 2:
            textarea.setText('YOUR ANSWERS HAVE BEEN SUBMITTED.\n')

    if i == 2:
        if j == 0:
            textarea.setText('QUESTION 1: \nWho is the Prime Minister of India?\n')
            j += 1
        elif j == 1:
            textarea.setText('QUESTION 2: \nWho is the President of India?\n')
            j += 1
        elif j == 2:
            textarea.setText('YOUR ANSWERS HAVE BEEN SUBMITTED.\n')

    return True

def AboutButtonClick(event = None):
    textarea.setText('This is a quiz application.\n')

    return True

def review(event = None):
    report = '\n\n' + text.getText() + ',\n you selected ' + rb2.getValue() + ' as the difficulty level.\n\n You would like to add '

    if checkbox1.getValue():
        report += 'History\n'

    if checkbox2.getValue():
        report += 'Geography\n'

    if checkbox3.getValue():
        report += 'Science\n'

    report += 'subjetct in the future.\n'
    r = str(spin.getValue())
    report += 'You also selected ' + r + ' as the number of questions you would like to attempt.\n'

    textarea1.appendText(report + '\n')

    return True

cities = ['General Knowledge', 'Maths']
valuelist = anygui.ValueList(cities, 90, 30, 200, 20, 'Choose the subject of the quiz:')
Frame.add(valuelist)

rb1 = anygui.RadioGroup(100, 50)
rb1.addRadioButton('TRUE', 100, 100)
rb1.addRadioButton('FALSE', 100, 120)
rb1.setButtonTrue(0)

Frame.add(rb1)

rb2 = anygui.RadioGroup(100, 50)
rb2.addRadioButton('Easy', 100, 100)
rb2.addRadioButton('Medium', 100, 120)
rb2.addRadioButton('Hard', 100, 140)
rb2.setButtonTrue(0)

Frame.add(rb2)

textarea = anygui.TextArea('\n Questions appear here.\n', 300, 50, 400, 200)
Frame.add(textarea)
textarea1 = anygui.TextArea('\n Your review appears here.\n', 300, 300, 400, 200)
Frame.add(textarea1)

startBtn = anygui.Button('Start Quiz-', 100, 200, 100, 30, SubmitButtonClick)
aboutBtn = anygui.Button('About', 100, 250, 100, 30, AboutButtonClick)
nextBtn = anygui.Button('Next', 100, 200, 100, 30, nextbuttonclick)
submit = anygui.Button('Submit', 100, 250, 100, 30, review)

Frame.add(submit)
submit.clickListener(review)
nextBtn.clickListener(nextbuttonclick)
Frame.add(nextBtn)

submit.clickListener(SubmitButtonClick)
aboutBtn.clickListener(AboutButtonClick)

label3 = anygui.Label('Select the difficulty level:', 100, 50)
label4 = anygui.Lab

checkbox1 = anygui.CheckBox('History', 100, 100)
checkbox2 = anygui.CheckBox('Geography', 100, 120)
checkbox3 = anygui.CheckBox('Science', 100, 140)
Frame.add(checkbox1)
Frame.add(checkbox2)
Frame.add(checkbox3)
Frame.add(label3)

label5 = anygui.Label('Please enter your username and password:', 10, 450, 200, 20)
Frame.add(label5)
pas = anygui.Password(10, 470, 200, 20)
Frame.add(pas)
sli = anygui.Slider(10, 500, 200, 20)
Frame.add(sli)
spin = anygui.SpinBox(10, 530, 200, 20)
Frame.add(spin)
label = anygui.Label('How was the Quiz?', 10, 550, 200, 20)
Frame.add(label)
label1 = anygui.Label('Select the subject of the quiz:', 10, 30, 200, 20)
Frame.add(label1)
label9 = anygui.Label('Select the number of questions:', 10, 510, 200, 20)
Frame.add(label9)
label7 = anygui.Label('Username:', 10, 470, 200, 20)
Frame.add(label7)
label8 = anygui.Label('Password:', 10, 490, 200, 20)
Frame.add(label8)
text = anygui.TextField(10, 470, 200, 20)
Frame.add(text)
Frame.add(submit)
Frame.show()

if __name__ == '__main__':
    Main()
