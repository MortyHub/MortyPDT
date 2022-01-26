class Keywords:
    def __init__(self, name, keyword):
        self.name = name
        self.keyword = keyword
    
    def getKey(self):
        return self.keyword
    
    def getName(self):
        return self.name
    
    def testKey(self, key):
        if self.keyword == key:
            return True
        else:
            return False

    def testName(self, name):
        if self.name == name:
            return True
        else:
            return False
    
    def setKey(self, key):
        self.keyword = key

    def remove(self):
        self.name = None
        self.keyword = None
    
    def setName(self, name):
        self.name = name

