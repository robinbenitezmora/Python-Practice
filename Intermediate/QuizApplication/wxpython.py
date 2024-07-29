
from wx import *
from wxpython import ValueList

class RadioGroup:
	def __init__(self, labels, positions, size):
		self.labels = labels
		self.positions = positions
		self.size = size

class Canvas(wx.Frame):
    def __init__(self, id, title, width, heigth):
        self.app = wx.App(False)
        wx.Frame.__init__(self, None, id, title, wx.DefaultPosition, wx.Size(width, heigth))
        self.panel = wx.Panel(self, -1)

    def center(self):
        self.Centre()
        self.Show(True)

    def show(self):
        self.Show(True)
        self.app.MainLoop()

    def add(self, widget, field = None):
        widget_type = type(widget)
        if(widget_type==TextArea or isinstance(widget,TextArea)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text, widget.position, widget.size, wx.TE_MULTILINE)
        elif(widget_type==TextLine or isinstance(widget,TextLine)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text, widget.position, widget.size)
        elif(widget_type==Password or isinstance(widget,Password)):
            widget.controller = wx.TextCtrl(self.panel, -1, widget.text, widget.position, widget.size, wx.TE_PASSWORD)
        elif(widget_type==Button or isinstance(widget,Button)):
            widget.controller = wx.Button(self.panel, -1, widget.title, widget.position, widget.size)
            widget.controller.Bind(wx.EVT_BUTTON, widget.callBackMethod)
        elif(widget_type==CheckBox or isinstance(widget,CheckBox)):
            widget.controller = wx.CheckBox(self.panel, -1, widget.title, widget.position, widget.size)
        elif(widget_type==Label or isinstance(widget,Label)):
            widget.controller = wx.StaticText(self.panel, -1, widget.name, widget.position, widget.size)
        elif(widget_type==Slider or isinstance(widget,Slider)):
            widget.controller = wx.Slider(self.panel, -1, widget.start, widget.end, widget.pos, widget.size, wx.SL_AUTOTICKS | wx.SL_LABELS)
        elif(widget_type==SpinBox or isinstance(widget,SpinBox)):
            widget.controller = wx.SpinButton(self.panel, -1, widget.pos, widget.size, wx.SP_VERTICAL)
        elif(widget_type==RadioGroup or isinstance(widget,RadioGroup)):
            widget.controller = []
            for i in range(len(widget.labels)):
                radio = wx.RadioButton(self.panel, -1, widget.labels[i], widget.positions[i], widget.size)
                widget.controller.append(radio)
        elif(widget_type==ValueList or isinstance(widget,ValueList)):
            widget.controller = wx.ComboBox(self.panel, -1, widget.value, widget.position, widget.size, widget.choices, wx.CB_DROPDOWN)
        else:
            print("Widget not supported")
        return True

class Password(wx.TextCtrl):
	controller = None
	def __init__(self,X,Y,width,height):
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text=""
	def setText(self,text):
		self.controller.text = text		
	def appendText(self,text):
		self.controller.text = self.controller.text + text
	def clearText():
		self.controller.text = ""	
	def getText(self):
		return self.controller.GetValue()


class TextArea(wx.TextCtrl):
	controller = None
	def __init__(self,string,X,Y,width,height):
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text = string
	def setText(self,text):
		self.controller.text = text
		
class TextLine(wx.TextCtrl):
	controller = None
	def __init__(self,X,Y,width,height):
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.text=""
	def setText(self,text):
		self.controller.text = text		
	def appendText(self,text):
		self.controller.text = self.controller.text + text
	def clearText():
		self.controller.text = ""	
	def getText(self):
		return self.controller.GetValue()

class Slider(wx.Slider):
	controller = None
	callBackMethod = None
	def __init__(self, start, end, X, Y, width, height):
		self.start=start
		self.end=end
		self.position = (X,Y)
		self.size = (width,height)
	def getValue(self):
		if self.controller is None:
			return ''
		else:
			return self.controller.GetValue()

class Label(wx.StaticText):
	controller =  None
	def __init__(self,name, X,Y, width,height):
		self.position = (X,Y)
		self.size = wx.Size(width, height)
		self.name = name

class SpinBox(wx.SpinButton):
	controller = None
	callBackMethod = None
	def __init__(self,start,end,X,Y,width,height):
		self.start = start
		self.end = end
		self.pos = (X,Y)
		self.size = (width,height)
    
		def getValue(self):
			if(self.controller == None):
				return ''
			else:	
				return self.controller.GetValue()

class Button(wx.Button):
	controller = None
	callBackMethod = None	
	def __init__(self,string,X,Y,width,height):	
		self.position = (X,Y)
		self.size = (width,height)
		self.id = -1
		self.title = string

	def clickListener(self,method):
		self.callBackMethod = method

class CheckBox(wx.CheckBox):
	controller = None
	def __init__(self,string,X,Y,width=10,height=10):
		self.position = (	self.cities = ['New Delhi', 'Mumbai', 'Ropar', 'Lucknow', 'Chandigrah', 'Wasseypur', 'Jaipur' ]X,Y)
		width = 0  # Replace 0 with the desired value for width
		self.size = (width, height)
		self.title = string
	def getValue(self):
		if(self.controller == None):
			return False
		else:
			return self.controller.GetValue()
		valuelist = ValueList([], 0, 0, 100, 30)  # Initialize valuelist with appropriate parameters
		report = " Your city is "+ valuelist.getValue()+"\n" "+ valuelist.getValue()+"\n"	
	def getValue(self):
		return
	def SubmitButtonClick(event=None):
		def SubmitButtonClick(self, event=None):
			valuelist = ValueList([], 0, 0, 100, 30)  # Initialize valuelist with appropriate parameters
			report = " Your city is "+ valuelist.getValue()+"\n"

		checkbox1 = CheckBox("I have read the code.",10,45,215,15)  # Define checkbox1
		if(checkbox1.getValue()):    
			report = report + " you have read the code\n"
		else:
			report = report + " you have not read the code\n"x2

		if(checkbox1.getValue()):    
			report = report + " you have read the code\n"
		else:
			report = report + " you have not read the code\n".",10,70,215,15)
		Frame.add(checkbox2)
		if(checkbox2.getValue()):
			report = report + " you have read the documentation\n"
		else:
			report = report + " you have not read the documentation\n")
		
		rb1 = RadioGroup(60,50)
		rb1.addRadioButton("Nice",10,110)
		rb1.addRadioButt		
		rb2 = RadioGroup(60,150)
		rb2.addRadioButton("Option1",10,160)
		rb2.addRadioButton("Option2",70,160)
		rb2.addRadioButton("Option3",140,160)
		rb2.setButtonTrue(1)
		report = report + " you need "+rb2.getValue()+"\n"110)
		rb1.setButtonTrue(2)
		report = report + " you are "+rb1.getValue()+"\n"
		report = report + " you need "+rb2.getValue()+"\n"
		textarea = TextArea("", 0, 0, 0, 0)
		X = 0  # Replace 0 with the desired value for X
		Y = 0  # Replace 0 with the desired value for Y
		width = 100  # Replace 100 with the desired value for width
		height = 30  # Replace 30 with the desired value for height
		pas = Password(X, Y, width, height)
		start = 0  # Replace 0 with the desired value for start
		end = 100  # Replace 100 with the desired value for end
		sli = Slider(start, end, X, Y, width, height)  # Replace start, end, X, Y, width, and height with appropriate values
		spin = SpinBox(start, end, X, Y, width, height)  # Define the spin variable
		textarea.appendText(" password :  \n"+ pas.getText()+"_______________________\n"+report+"\n" + " Slider value " + str(sli.getValue())+" SpinBox value  " + str(spin.getValue())+" \n")
		return True
	
	def getValue(self):
		for i in range(len(self.controller)):
			if self.controller[i].GetValue():
				return i
		return None

	def setButtonTrue(self, index):
		if self.controller is None:
			return
		else:
			self.controller[index].SetValue(True)
			self.selected_index = index

class ValueList(wx.ComboBox):
    controller = None
    def __init__(self,choices,X,Y,width,height,value=""):
        self.choices = choices
        self.position = (X,Y)
        self.size = (width,-1)
        self.value = value

    def getValue(self):
            if(self.controller == None):
                return self.value
            else:
                return self.controller.GetValue()


if __name__ == "__main__":	
	app = wx.App()
		
	def SubmitButtonClick(self, event=None):
		valuelist = ValueList([], 0, 0, 100, 30)
		report = " Your city is "+ valuelist.getValue()+"\n"

	checkbox1 = CheckBox("I have read the code.",10,45,215,15)  # Define checkbox1
	Frame.add(checkbox1)
	
	report = ""  # Initialize the "report" variable
	
	if(checkbox1.getValue()):    
		report = report + " you have read the code\n"
	else:
		report = report + " you have not read the code\n"

	checkbox2 = CheckBox("I have read the documentation.",10,70,215,15)
	Frame.add(checkbox2)

	if(checkbox2.getValue()):
		report = report + " you have read the documentation\n"
	else:
		report = report + " you have not read the documentation\n"

	rb1 = RadioGroup(60,50)
	rb1.addRadioButton("Nice",10,110)
	rb1.addRadioButton("Good",70,110)
	rb1.addRadioButton("Bad",140,110)
	rb1.setButtonTrue(2)
	report = report + " you are "+rb1.getValue()+"\n"

	rb2 = RadioGroup(60,150)
	rb2.addRadioButton("Option1",10,160)
	rb2.addRadioButton("Option2",70,160)
	rb2.addRadioButton("Option3",140,160)
	rb2.setButtonTrue(1)
	report = report + " you need "+rb2.getValue()+"\n"

	textarea = TextArea("", 0, 0, 0, 0)
	X = 0  # Replace 0 with the desired value for X
	Y = 0  # Replace 0 with the desired value for Y
	width = 100  # Replace 100 with the desired value for width
	height = 30  # Replace 30 with the desired value for height
	pas = Password(X, Y, width, height)
	start = 0  # Replace 0 with the desired value for start
	end = 100  # Replace 100 with the desired value for end
	sli = Slider(start, end, X, Y, width, height)  # Replace start, end, X, Y, width, and height with appropriate values
	spin = SpinBox(start, end, X, Y, width, height)  # Define the spin variable
	textarea.appendText(" password :  \n"+ pas.getText()+"_______________________\n"+report+"\n" + " Slider value " + str(sli.getValue())+" SpinBox value  " + str(spin.getValue())+" \n")
	app.MainLoop()
