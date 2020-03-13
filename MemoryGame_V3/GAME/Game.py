from GAME.Card import *
from random import shuffle

class Game:

    def __init__(self):
        self.numbers = list("1122334455667788")
        shuffle(self.numbers)

    def setStates(self, state, index, button, game):
        self.game = game
        self.state = state
        self.index = index
        self.button = button
        #
        if self.state == str("open"):
            Card().turnCard(self.numbers[self.index], self.index, self.button, self.game)
        elif self.state == str("closed"):
            Card().topCard()
        elif self.state == str("guessed"):
            Card().matchCard()
