import pickle


class ScoreDataBase:
    def __init__(self, dbFileName):
        self.dbFileName = dbFileName
        self.status = {'status': None, 'name': None}

    def read(self):
        try:
            fH = open(self.dbFileName, 'rb')
        except FileNotFoundError as e:
            #print("New DB: ", self.dbFileName)
            self.status['status'] = 'New'
            self.status['name'] = self.dbFileName
            return []

        scdb = []
        try:
            scdb = pickle.load(fH)
        except:
            #print("Empty DB: ", self.dbFileName)
            self.status['status'] = 'Empty'
            self.status['name'] = self.dbFileName
        else:
            #print("Open DB: ", self.dbFileName)
            self.status['status'] = 'Open'
            self.status['name'] = self.dbFileName
        fH.close()
        return scdb

    def write(self, scdb):
        fH = open(self.dbFileName, 'wb')
        pickle.dump(scdb, fH)
        fH.close()
