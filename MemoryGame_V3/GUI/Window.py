from GAME.Card import *


class Window:

    def __init__(self, game):
        self.game = game
        self.cards = 8
        root = tk.Tk()
        root.title("Memory game by Michel - V3")
        self.column = 0
        self.row = 0
        # het board wordt aangemaakt voor de memorygame (1 object)

        for i in range(self.cards * 2):
            Board(root, self.game, self.column, self.row, i)
            self.column = self.column + 1
            if self.column == 4:
                self.row = self.row + 1
                self.column = 0
        root.mainloop()
        # er worden met bovenstaande code 16 objecten aangemaakt

        # !-- er is 1 window object --!

class Board:

    def __init__(self, root, game, column, row, index):
        self.root = root
        self.game = game
        self.column = column
        self.row = row
        self.index = index
        #
        self.card = tk.Button(self.root,
                              text="?",
                              width=7,
                              height=5,
                              command=lambda: game.setStates(str("open"), self.index, self.card, self.game))
        self.card.grid(row=self.row, column=self.column, padx=20, pady=20)

        # in elk object wordt er een button aangemaakt, allemaal wordt dit aangemaakt in de root window.
        # Zodra er op 1 van de button objecten geklikt wordt, gaat de state op "open" (zie game.py)

        # !-- er zijn 16 kaart objecten binnen het window object --!