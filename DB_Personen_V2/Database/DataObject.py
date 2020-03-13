from Database.Credentials.Credentials import *
import mysql.connector

class DataObject:
    def __init__(self):
        self.mydb = mysql.connector.connect(host=host,
                                            user=user,
                                            password=password,
                                            database=database)
        self.mycursor = self.mydb.cursor()

    def getDataSource(self, query):
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def createDataSource(self, voornaam, achternaam, query):
        gegevens = (voornaam, achternaam)
        self.mycursor.execute(query, gegevens)
        self.mydb.commit()