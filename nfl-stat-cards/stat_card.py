from PyQt4 import *
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from parse_data import *
import sys

        #self.graphicsView_2 = QtGui.QGraphicsView(Card)
        #self.graphicsView_2.setGeometry(QtCore.QRect(150, 40, 500, 161))

class StatCard(QWidget):
    def __init__(self, current_player):
        QWidget.__init__(self)
        self.card = QWidget(self)

        self.card.resize(660, 650)
        self.card.setWindowTitle(current_player[0])

        self.stat_table = QTableWidget(self.card)
        self.stat_table.setGeometry(QRect(10, 210, 640, 400))
        self.stat_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.stat_table.setRowCount(len(current_player[5]) + 1)
        self.stat_table.setColumnCount(len(current_player[6]))

        for i in range(0, len(current_player[6])):
            self.stat_table.setItem(0, i, QTableWidgetItem(current_player[6][i]))
        for i in range(1, len(current_player[5]) + 1):
            for j in range(0, len(current_player[5][0])):
              self.stat_table.setItem(i, j, QTableWidgetItem(current_player[5][i - 1][j]))
        self.stat_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.name = QLabel(self.card)
        self.name.setGeometry(QRect(10, 20, 200, 13))
        self.name.setText(current_player[0])

        self.num = QLabel(self.card)
        self.num.setGeometry(QRect(250, 20, 56, 13))
        self.num.setText(current_player[1] + '-' + current_player[2])
       
        self.team = QLabel(self.card)
        self.team.setGeometry(QRect(375, 20, 300, 13))
        self.team.setText(current_player[3])

        self.photo = QLabel(self.card)
        self.photo.setGeometry(QRect(10, 50, 150, 150))
        self.photo.setScaledContents(True)                  
        self.photo.setPixmap(QPixmap(current_player[4]))

        self.categories = QComboBox(self.card)
        self.categories.setGeometry(QRect(500, 10, 104, 26))
        self.categories.addItem("")
        for cat in current_player[6]:
            self.categories.addItem(cat)

        self.chart_button = QPushButton(self.card)
        self.chart_button.setGeometry(610, 12, 30, 20)
        self.chart_button.setText("Go")
        self.chart_button.clicked.connect(self.makeChart)

    def makeChart(self):
        print('here')
        print (self.categories.currentText())


