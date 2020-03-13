from Controller.Persoon import *
#
import tkinter as tk


class Window:
    def __init__(self, database):
        self.database = database
        self.gegevens = database.getDataSource("SELECT achternaam, voornaam FROM personen")
        self.personen = []
        voornaam = 1
        achternaam = 0
        #
        root = tk.Tk()
        root.geometry("800x500")
        root.title("Datebase gegevens")
        #
        self.text = tk.Text(root, width=90, height=100)
        #
        for columns in range(len(self.gegevens)):
            persoon = Persoon()
            persoon.setVoornaam(self.gegevens[columns][voornaam])
            persoon.setAchternaam(self.gegevens[columns][achternaam])
            self.personen.append(persoon)
        #
        self.reloadList()
        add = tk.Button(root, text="Toevoegen", bg="grey", command=self.secondWindow)
        refresh = tk.Button(root, text="refresh", command=self.reloadList)
        add.place(x=75, y=400)
        refresh.place(x=200, y=400)
        #
        root.mainloop()

    def secondWindow(self):
        second = tk.Tk()
        second.geometry("400x500")
        second.title("Update the records")
        #
        voornaam = tk.Label(second, text="Voornaam :")
        achternaam = tk.Label(second, text="Achternaam :")
        #
        voornaam.place(x=10, y=50)
        achternaam.place(x=10, y=100)
        #
        voornaamString = tk.StringVar()
        achternaamString = tk.StringVar()
        #
        voornaamEntry = tk.Entry(second, textvariable=voornaamString, width="20")
        achternaamEntry = tk.Entry(second, textvariable=achternaamString, width="20")
        #
        voornaamEntry.place(x=10, y=70)
        achternaamEntry.place(x=10, y=120)
        #
        register = tk.Button(second, text="Toevoegen", command=lambda: self.database.createDataSource(voornaamEntry.get(),
                                                                                                 achternaamEntry.get(),
                                                                                                 "INSERT INTO `personen`(`voornaam`, `achternaam`) VALUES (%s,%s)"))
        register.place(x=10, y=200)
        #
        second.mainloop()

    def reloadList(self):
        self.text.delete(1.0 , tk.END)
        self.text.insert(tk.INSERT, "\t\tVoornaam\t\t\tAchternaam\t\t\n\n\n")
        rijnummer = 1
        for persoon in self.personen:
            self.text.insert(tk.INSERT,
                        "\t{}\t{}\t\t\t{}\t\t\n\n".format(rijnummer, persoon.getVoornaam(), persoon.getAchternaam()))
            rijnummer += 1
        self.text.update_idletasks()
        self.text.pack()
