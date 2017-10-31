import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()

        self.inforUI()
        self.labelUI()
        self.inputUI()
        self.buttonUI()
        self.resultUI()
        self.sortUI()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Assignment6')
        self.show()

    def inforUI(self):

        titleLable = QLabel('ScoreBoard', self)
        titleLable.setGeometry(300, 0, 120, 80)
        inforLable = QLabel('20171678 이정훈\nSoftware Project II\nAssignment', self)
        inforLable.setGeometry(10, 0, 120, 80)

    def buttonUI(self):

        addBtn = QPushButton('Add', self)
        addBtn.setGeometry(50, 170, 120, 35)
        delBtn = QPushButton('Del', self)
        delBtn.setGeometry(180, 170, 120, 35)
        findBtn = QPushButton('Find', self)
        findBtn.setGeometry(310, 170, 120, 35)
        incBtn = QPushButton('Inc', self)
        incBtn.setGeometry(440, 170, 120, 35)
        showBtn = QPushButton('Show', self)
        showBtn.setGeometry(570, 170, 120, 35)

        addBtn.clicked.connect(self.addDB)
        delBtn.clicked.connect(self.delDB)
        findBtn.clicked.connect(self.findDB)
        incBtn.clicked.connect(self.incDB)
        showBtn.clicked.connect(self.showDB)

    def labelUI(self):

        nameLable = QLabel('Name: ', self)
        nameLable.setGeometry(90, 60, 50, 50)
        ageLable = QLabel('Age: ', self)
        ageLable.setGeometry(300, 60, 50, 50)
        scoreLable = QLabel('Score: ', self)
        scoreLable.setGeometry(500, 60, 50, 50)
        amountLable = QLabel('Amount: ', self)
        amountLable.setGeometry(360, 100, 50, 50)
        resultLable = QLabel('▼ Result ▼', self)
        resultLable.setGeometry(325, 200, 100 , 50)
        sortLable = QLabel('Key: ', self)
        sortLable.setGeometry(580, 100, 100, 50)

    def inputUI(self):

        self.nameInput = QLineEdit('', self)
        self.nameInput.setGeometry(130, 70, 150, 30)
        self.ageInput = QLineEdit('', self)
        self.ageInput.setGeometry(330, 70, 150, 30)
        self.scoreInput = QLineEdit('', self)
        self.scoreInput.setGeometry(540, 70, 150, 30)
        self.amountInput = QLineEdit('', self)
        self.amountInput.setGeometry(415, 110, 150, 30)


    def resultUI(self):

        self.result = QTextEdit(self)
        self.result.setGeometry(10, 250, 680, 220)
        self.result.setReadOnly(True)


    def sortUI(self):

        self.sort = QComboBox(self)
        self.sort.addItem('Name')
        self.sort.addItem('Age')
        self.sort.addItem('Score')
        self.sort.setGeometry(610, 110, 80, 30)

    def addDB(self):
        record = {'Name':self.nameInput.text(), 'Age':self.ageInput.text(), 'Score':self.scoreInput.text()}
        self.scoredb += [record]
        return self.scoredb

    def delDB(self):
        for i in range(len(self.scoredb)):
            for j in self.scoredb:
                if j['Name'] == self.nameInput.text():
                    self.scoredb.remove(j)
                    break

    def findDB(self):
        for p in self.scoredb:
            if p['Name'] == self.nameInput.text():
                print("Age:" + self.ageInput.text() + " Name:" + self.nameInput.text() + " Score:" + self.scoreInput.text())

    def incDB(self):
        for p in self.scoredb:
            if p['Name'] == self.nameInput.text():
                p['Score'] += self.scoreInput.text()

    def showDB(self):
        sortKey = 'Name' if len(parse) == 1 else parse[1]
        showScoreDB(self.scoredb, sortKey)



    def closeEvent(self, event):

        self.writeScoreDB()


    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
