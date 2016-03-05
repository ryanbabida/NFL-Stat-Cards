from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Card(object):
    def setupUi(self, Card, name, num, team, photo):
        Card.setObjectName(_fromUtf8("Card"))
        Card.resize(660, 325)
        self.tableView = QtGui.QTableView(Card)
        self.tableView.setGeometry(QtCore.QRect(10, 210, 640, 101))
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setObjectName(_fromUtf8("tableView"))

        self.name = QtGui.QLabel(Card)
        self.name.setGeometry(QtCore.QRect(150, 20, 200, 13))
        self.name.setObjectName(_fromUtf8("name"))
        

        self.num = QtGui.QLabel(Card)
        self.num.setGeometry(QtCore.QRect(350, 20, 56, 13))
        self.num.setObjectName(_fromUtf8("num"))
       

        self.team = QtGui.QLabel(Card)
        self.team.setGeometry(QtCore.QRect(425, 20, 300, 13))
        self.team.setObjectName(_fromUtf8("team"))
        

        self.comboBox = QtGui.QComboBox(Card)
        self.comboBox.setGeometry(QtCore.QRect(550, 10, 104, 26))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.graphicsView_2 = QtGui.QGraphicsView(Card)
        self.graphicsView_2.setGeometry(QtCore.QRect(150, 40, 500, 161))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))

        self.photo = QtGui.QLabel(Card)
        self.photo.setGeometry(QtCore.QRect(10, 50, 130, 150))
        self.photo.setObjectName(_fromUtf8("photo"))


        self.retranslateUi(Card, name, num, team, photo)
        QtCore.QMetaObject.connectSlotsByName(Card)

    def retranslateUi(self, Card, name, num, team, photo):
        Card.setWindowTitle(_translate("Card", name, None))
        self.name.setText(_translate("Card", name, None))
        self.num.setText(_translate("Card", num, None))
        self.team.setText(_translate("Card", team, None))
        self.photo.setScaledContents(True)
        #myScaledPixmap = myPixmap.scaled(self.label.size(), QtGui.KeepAspectRatio)
        self.photo.setPixmap(QtGui.QPixmap(photo))


