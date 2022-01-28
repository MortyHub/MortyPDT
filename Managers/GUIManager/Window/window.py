from tkinter import *

class window:
    def __init__(self, x, y, bgc, name):
        self.window = Tk()
        self.window.configure(background=bgc)
        self.window.geometry(f"{str(x)}x{str(y)}")
        self.window.title(name)
    
    def addButton(self,x, y, text, font, size, fg, call = None):
        self.Button = Button(self.window, text=f"{text}", fg=f"{fg}", font=(f"{font}", size), command=call)
        self.Button.place(x=x,y=y)
    
    def addTextBox(self, x, y, width, height, font, fos):
        self.TextBox = Text(self.window, height=height, width=width, font=(f"{font}", fos))
        self.TextBox.place(x=x, y=y)
    
    def addLabel(self, x, y, text, font, fs):
        self.Label = Label(self.window, text=text, font=(f"{font}", fs))
        self.Label.place(x=x,y=y)

    def toolLoop(self):
        self.window.mainloop()
