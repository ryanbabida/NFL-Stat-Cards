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

    def setupUi(self, Card, current_player): # current_player
        Card.setObjectName(_fromUtf8("Card"))
        Card.resize(660, 650)
        Card.setWindowTitle(current_player[0])

        self.stat_table = QtGui.QTableWidget(Card)
        self.stat_table.setGeometry(QtCore.QRect(10, 210, 640, 400))
        self.stat_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.stat_table.setObjectName(_fromUtf8("stat_table"))
        self.stat_table.setRowCount(len(current_player[5]) + 1)
        self.stat_table.setColumnCount(len(current_player[6]))

        self.stat_table.setItem(0, 0, QtGui.QTableWidgetItem("Week"))
        for i in range(0, len(current_player[6])):
            self.stat_table.setItem(0, i, QtGui.QTableWidgetItem(current_player[6][i]))
        for i in range(1, len(current_player[5]) + 1):
            for j in range(0, len(current_player[5][0])):
                self.stat_table.setItem(i, j, QtGui.QTableWidgetItem(current_player[5][i - 1][j]))

        self.name = QtGui.QLabel(Card)
        self.name.setGeometry(QtCore.QRect(150, 20, 200, 13))
        self.name.setObjectName(_fromUtf8("name"))
        self.name.setText(current_player[0])
        
        self.num = QtGui.QLabel(Card)
        self.num.setGeometry(QtCore.QRect(350, 20, 56, 13))
        self.num.setObjectName(_fromUtf8("num"))
        self.num.setText(current_player[1] + '-' + current_player[2])
       
        self.team = QtGui.QLabel(Card)
        self.team.setGeometry(QtCore.QRect(425, 20, 300, 13))
        self.team.setObjectName(_fromUtf8("team"))
        self.team.setText(current_player[3])
        
        self.categories = QtGui.QComboBox(Card)
        self.categories.setGeometry(QtCore.QRect(550, 10, 104, 26))
        self.categories.setObjectName(_fromUtf8("comboBox"))
        for cat in current_player[6]:
            self.categories.addItem(cat)
        #self.categories.highlighted['QString'].connect(self.catChanged)
        self.categories.currentIndexChanged['QString'].connect(self.selectionchange)

        self.graphicsView_2 = QtGui.QGraphicsView(Card)
        self.graphicsView_2.setGeometry(QtCore.QRect(150, 40, 500, 161))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))

        self.photo = QtGui.QLabel(Card)
        self.photo.setGeometry(QtCore.QRect(10, 50, 130, 150))
        self.photo.setObjectName(_fromUtf8("photo"))
        self.photo.setScaledContents(True)                  #current_player[3]
        self.photo.setPixmap(QtGui.QPixmap(current_player[4]))

        QtCore.QMetaObject.connectSlotsByName(Card)


    def selectionchange(self,i):
        print ("Items in the list are :")
        
        for count in range(self.cb.count()):
            print (self.cb.itemText(count))
        print ("Current index",i,"selection changed ",self.cb.currentText())



