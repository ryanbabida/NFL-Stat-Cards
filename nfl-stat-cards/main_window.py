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

