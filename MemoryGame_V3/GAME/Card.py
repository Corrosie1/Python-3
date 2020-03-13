import tkinter as tk

button_number = []


class Card:

    def turnCard(self, number, index, button, game):
        self.number = number
        self.index = index
        self.button = button
        self.game = game
        #
        self.button.config(text=self.number, state=tk.DISABLED)
        #
        button_number.append(self.button)
        button_number.append(self.number)
        button_number.append(self.index)
        #
        if len(button_number) >= 6:
            self.checkCard()

    def checkCard(self):
        if button_number[1] == button_number[4]:
            self.game.setStates(str("guessed"), None, None, None)
        if len(button_number) == 9:
            self.game.setStates(str("closed"), None, None, None)

            # Ik liep zelf tegen het probleem aan dat ik de tekst niet kon wijzigen door gebruik te maken van een getter in het window object (onder het kopje text).
            # uiteindelijk heb ik het opgelost door alsnog gebruik te maken van .config(text="<NUMMER>") ipv door het eenmalig in het board object onder het attribuut text te doen met een getter
            # als voorbeeld: .config(text=getNumber())

    def topCard(self):
        button_number[0].config(text="?", state=tk.NORMAL)
        button_number[3].config(text="?", state=tk.NORMAL)
        button_number[6].config(text="?", state=tk.NORMAL)
        #
        for i in range(len(button_number)):
            button_number.pop()

    def matchCard(self):
        button_number[0].config(text="Match! - {}".format(button_number[1]))
        button_number[3].config(text="Match! - {}".format(button_number[4]))
        #
        for i in range(len(button_number)):
            button_number.pop()
