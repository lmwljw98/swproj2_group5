from database import ScoreDataBase


class ScoreAPI:
    def __init__(self, dbName):
        self.db = ScoreDataBase(dbName)
        self.scdb = self.db.read()

    def save(self):
        self.db.write(self.scdb)

    def searchRecord(self, name):
        indexList = []
        for index in range(len(self.scdb)):
            if self.scdb[index]['Name'] == name:
                indexList.append(index)
        return indexList

    def getAllRecord(self, keyName):
        return sorted(self.scdb, key=lambda person: person[keyName])

    def findRecord(self, name):
        return [self.scdb[index] for index in self.searchRecord(name)]

    def addRecord(self, **kwargs):
        self.scdb.append(kwargs)

    def deleteRecord(self, name):
        reversedIndexList = self.searchRecord(name)[-1::-1]
        for index in reversedIndexList:
            self.scdb.pop(index)

    def increaseRecord(self, name, amount):
        for index in self.searchRecord(name):
            self.scdb[index]['Score'] += amount
