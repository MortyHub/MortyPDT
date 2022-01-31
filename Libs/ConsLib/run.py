import os

class Command:
    def __init__(self, command):
        self.command = command

    def runCMD(self):
        os.system(self.command)