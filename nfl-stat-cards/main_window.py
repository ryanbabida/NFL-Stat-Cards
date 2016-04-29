from PyQt4 import *
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from parse_data import *
import sys
'''
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

    '''

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
        self.name.setGeometry(QRect(150, 20, 200, 13))
        self.name.setText(current_player[0])

        self.num = QLabel(self.card)
        self.num.setGeometry(QRect(300, 20, 56, 13))
        self.num.setText(current_player[1] + '-' + current_player[2])
       
        self.team = QLabel(self.card)
        self.team.setGeometry(QRect(375, 20, 300, 13))
        self.team.setText(current_player[3])

        self.photo = QLabel(self.card)
        self.photo.setGeometry(QRect(10, 50, 130, 150))
        self.photo.setScaledContents(True)                  #current_player[3]
        self.photo.setPixmap(QPixmap(current_player[4]))

        self.categories = QComboBox(self.card)
        self.categories.setGeometry(QRect(500, 10, 104, 26))
        self.categories.addItem("")
        for cat in current_player[6]:
            self.categories.addItem(cat)
        #self.categories.highlighted['QString'].connect(self.catChanged)
        #self.categories.currentIndexChanged['QString'].connect(self.selectionchange)

        self.chart_button = QPushButton(self.card)
        self.chart_button.setGeometry(610, 12, 30, 20)
        self.chart_button.setText("Go")
        self.chart_button.clicked.connect(self.makeChart)

    def makeChart(self):
        print('here')
        print (self.categories.currentText())




class MainWindow(QMainWindow):
    
    results = dict()
    current_player = list()
    cards = list()

    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.cw = QWidget(self)
        self.setCentralWidget(self.cw)
        self.cw.resize(455, 288)
        self.gridLayout = QGridLayout(self.cw)

        self.search_box = QLineEdit(self.cw)
        self.gridLayout.addWidget(self.search_box, 0, 0, 1, 1)

        self.search_btn = QPushButton(self.cw)
        self.search_btn.setText("Search")
        self.gridLayout.addWidget(self.search_btn, 0, 1, 1, 1)
        self.search_btn.clicked.connect(self.searchClicked)
    
        self.result_list = QListWidget(self.cw)
        self.result_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.gridLayout.addWidget(self.result_list, 1, 0, 1, 1)

        self.get_btn = QPushButton(self.cw)
        self.get_btn.setText("Create Card")
        self.gridLayout.addWidget(self.get_btn, 1, 1, 1, 1)
        self.get_btn.clicked.connect(self.getClicked)

    def searchClicked(self):
        name = self.search_box.text()
        self.results.clear()
        self.results = search(name)
        self.result_list.clear()
        for name in self.results:
            self.result_list.addItem(name)
            
    def getClicked(self):
        # creates the player object
        if self.result_list.currentItem() == None: 
            print("Not valid")
        else:
            name = self.result_list.currentItem().text()
            log = getLog(self.results[name])
            img_url = getImg(log)
            data = urllib.request.urlopen(img_url).read()
            img = QImage()
            img.loadFromData(data)
            pos = getPos(log)
            team = getTeam(log)
            stats = getStats(log, pos[1])
            categories = getCategories(pos[1])

            current_player = (name, pos[0], pos[1], team, img, stats, categories)
            #print(current_player)
            

            
            ui = StatCard(current_player)
            self.cards.append(ui)
            ui.show()
            
    

class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
        self.main.show()

    def byebye( self ):
        self.exit(0)


def main(args):
    global app
    app = App(args)
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)

