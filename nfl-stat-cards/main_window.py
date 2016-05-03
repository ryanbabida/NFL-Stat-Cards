from PyQt4 import *
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from parse_data import *
from stat_card import *
import sys

class MainWindow(QMainWindow):

    results = dict()
    current_player = list()
    cards = list()

    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.main_window = QWidget(self)
        self.setCentralWidget(self.main_window)
        self.main_window.resize(455, 288)
        self.gridLayout = QGridLayout(self.main_window)

        self.search_box = QLineEdit(self.main_window)
        self.gridLayout.addWidget(self.search_box, 0, 0, 1, 1)

        self.search_btn = QPushButton(self.main_window)
        self.search_btn.setText("Search")
        self.gridLayout.addWidget(self.search_btn, 0, 1, 1, 1)
        self.search_btn.clicked.connect(self.searchClicked)
    
        self.result_list = QListWidget(self.main_window)
        self.result_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.gridLayout.addWidget(self.result_list, 1, 0, 1, 1)

        self.get_btn = QPushButton(self.main_window)
        self.get_btn.setText("Create Card")
        self.gridLayout.addWidget(self.get_btn, 1, 1, 1, 1)
        self.get_btn.clicked.connect(self.getClicked)

        self.save_btn = QPushButton(self.main_window)
        self.save_btn.setText("Save Player")
        self.gridLayout.addWidget(self.save_btn, 2, 0, 1, 1)
        self.save_btn.clicked.connect(self.saveClicked)

    def searchClicked(self):
        name = self.search_box.text()
        self.results.clear()
        self.results = search(name)
        self.result_list.clear()
        for name in self.results:
            self.result_list.addItem(name)
            
    def getClicked(self):
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
            ui = StatCard(current_player)
            self.cards.append(ui)
            ui.show()

    def saveClicked(self):
        print('saveClicked')
            
class App(QApplication):
    def __init__(self, *args):
        QApplication.__init__(self, *args)
        self.main = MainWindow()
        self.connect(self, SIGNAL("lastWindowClosed()"), self.byebye )
        self.main.show()

    def byebye( self ):
        self.exit(0)


