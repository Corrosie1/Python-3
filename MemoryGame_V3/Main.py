from GAME.Game import *
from GUI.Window import *


class Main:

    def __init__(self):
        self.game = Game()
        self.window = Window(self.game)

Main()
