from PyQt4 import QtCore, QtGui

class Ui_Card(object):

    def __init__(self, Card, current_player): # current_player
        Card.resize(660, 650)
        Card.setWindowTitle(current_player[0])

        self.stat_table = QtGui.QTableWidget(Card)
        self.stat_table.setGeometry(QtCore.QRect(10, 210, 640, 400))
        self.stat_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.stat_table.setRowCount(len(current_player[5]) + 1)
        self.stat_table.setColumnCount(len(current_player[6]))

        for i in range(0, len(current_player[6])):
            self.stat_table.setItem(0, i, QtGui.QTableWidgetItem(current_player[6][i]))
        for i in range(1, len(current_player[5]) + 1):
            for j in range(0, len(current_player[5][0])):
                self.stat_table.setItem(i, j, QtGui.QTableWidgetItem(current_player[5][i - 1][j]))
        self.stat_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.name = QtGui.QLabel(Card)
        self.name.setGeometry(QtCore.QRect(150, 20, 200, 13))
        self.name.setText(current_player[0])
        
        self.num = QtGui.QLabel(Card)
        self.num.setGeometry(QtCore.QRect(300, 20, 56, 13))
        self.num.setText(current_player[1] + '-' + current_player[2])
       
        self.team = QtGui.QLabel(Card)
        self.team.setGeometry(QtCore.QRect(375, 20, 300, 13))
        self.team.setText(current_player[3])
        
        self.categories = QtGui.QComboBox(Card)
        self.categories.setGeometry(QtCore.QRect(500, 10, 104, 26))
        self.categories.addItem("")
        for cat in current_player[6]:
            self.categories.addItem(cat)
        #self.categories.highlighted['QString'].connect(self.catChanged)
        #self.categories.currentIndexChanged['QString'].connect(self.selectionchange)

        self.graphicsView_2 = QtGui.QGraphicsView(Card)
        self.graphicsView_2.setGeometry(QtCore.QRect(150, 40, 500, 161))

        self.photo = QtGui.QLabel(Card)
        self.photo.setGeometry(QtCore.QRect(10, 50, 130, 150))
        self.photo.setScaledContents(True)                  #current_player[3]
        self.photo.setPixmap(QtGui.QPixmap(current_player[4]))

        self.chart_button = QtGui.QPushButton(Card)
        self.chart_button.setGeometry(610, 12, 30, 20)
        self.chart_button.setText("Go")
        self.chart_button.clicked.connect(self.makeChart)

    def makeChart(self):
        print('here')
        print (self.categories.currentText())



