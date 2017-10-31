import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout,
                             QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)


class ScoreDBForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        self.mainVBox = QVBoxLayout()

        self.dataHLayout0 = QHBoxLayout()
        self.dataHLayout1 = QHBoxLayout()
        self.buttonHLayout = QHBoxLayout()
        self.resultHLayout = QHBoxLayout()

        self.nameHBox = LabelHBoxLayout('Name: ', QLineEdit)
        self.ageHBox = LabelHBoxLayout('Age: ', QLineEdit)
        self.scoreHBox = LabelHBoxLayout('Score: ', QLineEdit)

        self.amountHBox = LabelHBoxLayout('Amount: ', QLineEdit)
        self.keyHBox = LabelHBoxLayout('Key: ', QComboBox)

        self.addButton = QPushButton('Add')
        self.delButton = QPushButton('Del')
        self.findButton = QPushButton('Find')
        self.incButton = QPushButton('Inc')
        self.showButton = QPushButton('Show')

        self.resultVBox = LabelVBoxLayout('Result: ', QTextEdit)

        self.layoutSetup()

    def layoutSetup(self):
        self.mainVBox.addLayout(self.dataHLayout0)
        self.mainVBox.addLayout(self.dataHLayout1)
        self.mainVBox.addLayout(self.buttonHLayout)
        self.mainVBox.addLayout(self.resultHLayout)

        self.dataHLayout0.addLayout(self.nameHBox)
        self.dataHLayout0.addLayout(self.ageHBox)
        self.dataHLayout0.addLayout(self.scoreHBox)

        self.dataHLayout1.addStretch(1)
        self.dataHLayout1.addLayout(self.amountHBox)
        self.dataHLayout1.addLayout(self.keyHBox)

        self.buttonHLayout.addStretch(1)
        self.buttonHLayout.addWidget(self.addButton)
        self.buttonHLayout.addWidget(self.delButton)
        self.buttonHLayout.addWidget(self.findButton)
        self.buttonHLayout.addWidget(self.incButton)
        self.buttonHLayout.addWidget(self.showButton)

        self.resultHLayout.addLayout(self.resultVBox)

        keys = ['Name', 'Age', 'Score']
        for keyName in keys:
            self.keyHBox.widget.addItem(keyName)

        self.setLayout(self.mainVBox)


class LabelHBoxLayout(QHBoxLayout):
    def __init__(self, label, widget):
        super().__init__()
        self.label = QLabel(label)
        self.widget = widget()
        self.setup()

    def setup(self):
        self.addWidget(self.label)
        self.addWidget(self.widget)


class LabelVBoxLayout(QVBoxLayout):
    def __init__(self, label, widget):
        super().__init__()
        self.label = QLabel(label)
        self.widget = widget()
        self.setup()

    def setup(self):
        self.addWidget(self.label)
        self.addWidget(self.widget)


class Test(ScoreDBForm):
    def __init__(self):
        super().__init__()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())
