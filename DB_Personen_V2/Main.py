from Gui.Window import *
from Database.DataObject import *


class Main:

    def __init__(self):
        self.dataObject = DataObject()
        Window(self.dataObject)


Main()
