import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox
from form import ScoreDBForm
from api import ScoreAPI


class ScoreDBApplication(ScoreDBForm):
    def __init__(self):
        super().__init__()
        self.api = ScoreAPI('assignment6.dat')
        self.initUI()
        self.setWindowTitle(self.api.db.status['status'] + ' ' + self.api.db.status['name'])
        self.show()
        self.showAllRecord()

    def initUI(self):
        self.addButton.clicked.connect(self.addRecord)
        self.delButton.clicked.connect(self.delRecord)
        self.findButton.clicked.connect(self.findRecord)
        self.incButton.clicked.connect(self.incRecord)
        self.showButton.clicked.connect(self.showAllRecord)
        self.keyHBox.widget.currentTextChanged.connect(self.showAllRecord)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.api.save()

    def showRecord(self, recordList):
        result = ""
        for i in recordList:
            result += "%s=%s\t%s=%d\t%s=%d\n" % ('Name', i['Name'], 'Age', i['Age'], 'Score', i['Score'])
        self.resultVBox.widget.setText(result)

    def addRecord(self):
        name = self.nameHBox.widget.text()
        try:
            age = int(self.ageHBox.widget.text())
        except ValueError as e:
            errorWindow = QMessageBox.warning(self, 'Error', 'Age field must be numeric', QMessageBox.Ok, QMessageBox.Ok)
            return
        try:
            score = int(self.scoreHBox.widget.text())
        except ValueError as e:
            errorWindow = QMessageBox.warning(self, 'Error', 'Score field must be numeric', QMessageBox.Ok, QMessageBox.Ok)
            return
        self.api.addRecord(Name=name, Age=age, Score=score)
        self.showAllRecord()

    def delRecord(self):
        name = self.nameHBox.widget.text()
        self.api.deleteRecord(name)
        self.showAllRecord()

    def findRecord(self):
        name = self.nameHBox.widget.text()
        self.showRecord(self.api.findRecord(name))

    def incRecord(self):
        name = self.nameHBox.widget.text()
        try:
            amount = int(self.amountHBox.widget.text())
        except ValueError as e:
            errorWindow = QMessageBox.warning(self, 'Error', 'Amount field must be numeric', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.api.increaseRecord(name, amount)
            self.showAllRecord()

    def showAllRecord(self):
        self.showRecord(self.api.getAllRecord(self.keyHBox.widget.currentText()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ScoreDBApplication()
    sys.exit(app.exec_())
    