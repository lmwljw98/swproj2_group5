
import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()

        self.lineedit_name = QLineEdit(self)
        self.lineedit_name.move(40, 10)
        self.lineedit_age = QLineEdit(self)
        self.lineedit_age.move(200, 10)
        self.lineedit_score = QLineEdit(self)
        self.lineedit_score.move(370, 10)
        self.lineedit_amount = QLineEdit(self)
        self.lineedit_amount.move(230, 50)

        self.result = QTextEdit()
        self.result.move(20,120)

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        label_name = QLabel("Name:", self)
        label_age = QLabel("Age:", self)
        label_score = QLabel("Score:", self)
        label_amount = QLabel("Amount:", self)
        label_key = QLabel("Key:", self)
        label_result = QLabel("Result:", self)
        label_name.move(0,10)
        label_age.move(170,10)
        label_score.move(330,10)
        label_amount.move(170, 50)
        label_key.move(380, 50)
        label_result.move(0,110)

        btn_add = QPushButton("Add", self)
        btn_add.move(50,75)
        btn_del = QPushButton("Del", self)
        btn_del.move(135,75)
        btn_find = QPushButton("Find", self)
        btn_find.move(220,75)
        btn_inc = QPushButton("Inc", self)
        btn_inc.move(305,75)
        btn_show = QPushButton("Show", self)
        btn_show.move(390,75)


        btn_add.clicked.connect(self.addDB)
        btn_show.clicked.connect(self.showScoreDB)
        btn_del.clicked.connect(self.delDB)
        btn_find.clicked.connect(self.findDB)
        btn_inc.clicked.connect(self.incDB)

        combobox_key = QComboBox(self)
        combobox_key.move(415,50)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6_20171680')
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
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

    def addDB(self):
        record = {'Name': self.lineedit_name.text(), 'Age': self.lineedit_age.text(), 'Score': self.lineedit_score.text()}
        self.scoredb += [record]

    def delDB(self):
        for i in range(len(self.scoredb)):
            for j in self.scoredb:
                if j['Name'] == self.lineedit_name.text():
                    self.scoredb.remove(j)
                    break
        self.showScoreDB()

    def findDB(self):
        pass

    def incDB(self):
        lineedit_amount = int(self.lineedit_amount.text())
        for i in self.scoredb:
            i['Score'] = int(i["Score"])
            if i['Name'] == self.lineedit_name.text():
                i['Score'] += lineedit_amount
            self.showScoreDB()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())