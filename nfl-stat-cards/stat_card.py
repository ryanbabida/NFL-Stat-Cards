from PyQt4 import *
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from parse_data import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import numpy as np
import sys
import random

class StatCard(QWidget):
    def __init__(self, current_player):
        QWidget.__init__(self)
        self.current_player = current_player
        self.card = QWidget(self)

        self.card.resize(500, 400)
        self.card.setWindowTitle(current_player[0])

        self.stat_table = QTableWidget(self.card)
        self.stat_table.verticalHeader().setVisible(False)
        self.stat_table.horizontalHeader().setVisible(False)
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
        self.name.setText(current_player[0])

        self.num = QLabel(self.card)
        self.num.setText(current_player[1] + '-' + current_player[2])
       
        self.team = QLabel(self.card)
        self.team.setText(current_player[3])

        self.photo = QLabel(self.card)
        self.photo.setScaledContents(True)                  
        self.photo.setPixmap(QPixmap(current_player[4]))

        self.categories = QComboBox(self.card)
        self.categories.addItem("")
        for i in range(3, len(current_player[6])):
            self.categories.addItem(current_player[6][i])

        self.chart_button = QPushButton(self.card)
        self.chart_button.setText("Plot")
        self.chart_button.clicked.connect(self.makeChart)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        main_layout = QtGui.QVBoxLayout()
        grid1 = QtGui.QGridLayout()
        grid2 = QtGui.QGridLayout()
        
        grid1.addWidget(self.name, 0, 0)
        grid1.addWidget(self.num, 0, 1)
        grid1.addWidget(self.team, 0, 2)
        grid1.addWidget(self.categories, 0, 3)
        grid1.addWidget(self.chart_button, 0, 4)
        main_layout.addLayout(grid1)

        grid2.addWidget(self.photo, 0, 0)
        grid2.addWidget(self.stat_table, 0, 1, 2, 1)
        grid2.addWidget(self.canvas, 3, 0, 1, 2)
        main_layout.addLayout(grid2)
        
        self.setLayout(main_layout)

    def makeChart(self, current_player):
        data = [row[self.categories.currentIndex() + 2] for row in self.current_player[5]]
        data = data[5:len(data) - 1]
        for i in range(0, len(data)): 
            if data[i] == '--':
                data[i] = 0
        print(data)
        ax = self.figure.add_subplot(111)
        ax.hold(False)
        ax.plot(data)
        self.canvas.draw()


