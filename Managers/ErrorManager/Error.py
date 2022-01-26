Types = ["Error: ", "Warning: ", "Alert: "]

Name_History = {

}

Type_History = {

}

Text_History = {

}

class Error:
    def __init__(self, name, text, typee):
        self.errorName = name
        self.errorText = text
        self.errorType = typee
        Name_History[self.errorName] = self.errorName
        Type_History[self.errorName] = self.errorType
        Text_History[self.errorName] = self.errorText

    def printError(self):
        if self.errorType == "Error":
            colored(255, 51, 51, "Error: " + self.errorText)
        
        if self.errorType == "Warning":
            colored(235, 94, 94, "Warning: " + self.errorText)
        
        if self.errorType == "Alert":
            colored(255, 245, 84, "Alert: " + self.errorText)

    def returnName(self):
        return self.errorName

    def returnType(self):
        return self.errorType

    def returnText(self):
        return self.errorText
    
    def changeName(self, name):
        self.errorName = name
        Name_History[self.errorName] = self.errorName

    def changeText(self, Text):
        self.errorText = Text
        Type_History[self.errorName] = self.errorType

    def changeType(self, typeq):
        self.errorType = typeq
        Text_History[self.errorName] = self.errorText

    def getNameHistory(self):
        return Name_History
    
    def getTypeHistory(self):
        return Type_History
    
    def getTextHistory(self):
        return Text_History

def colored(r, g, b, text):
    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))

Error1 = Error("Sus", "ee", "Error")
Error1.printError()