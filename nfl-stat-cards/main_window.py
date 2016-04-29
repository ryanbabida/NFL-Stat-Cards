from PyQt4 import QtCore, QtGui
from parse_data import *
import sys

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



class Ui_Form(object):

    results = dict()
    current_player = list()
    cards = list()

    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("NFL Stat Cards"))
        Form.resize(455, 288)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.search_box = QtGui.QLineEdit(Form)
        self.search_box.setText(_fromUtf8(""))
        self.search_box.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.search_box, 0, 0, 1, 1)

        self.search_btn = QtGui.QPushButton(Form)
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.search_btn.clicked.connect(self.searchClicked)
        self.gridLayout.addWidget(self.search_btn, 0, 1, 1, 1)

        self.result_list = QtGui.QListWidget(Form)
        self.result_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.result_list.setObjectName(_fromUtf8("Results"))
        self.gridLayout.addWidget(self.result_list, 1, 0, 1, 1)

        self.save_btn = QtGui.QPushButton(Form)
        self.save_btn.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.save_btn, 1, 1, 1, 1)

        self.get_btn = QtGui.QPushButton(Form)
        self.get_btn.setObjectName(_fromUtf8("pushButton"))
        self.get_btn.clicked.connect(self.getClicked)
        self.gridLayout.addWidget(self.get_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "NFL Stat Cards", None))
        self.search_btn.setText(_translate("Form", "Search", None))
        self.save_btn.setText(_translate("Form", "Save Player", None))
        self.get_btn.setText(_translate("Form", "Get Player", None))


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
            img = QtGui.QImage()
            img.loadFromData(data)
            pos = getPos(log)
            team = getTeam(log)
            stats = getStats(log, pos[1])
            categories = getCategories(pos[1])

            self.current_player = (name, pos[0], pos[1], team, img, stats, categories)

            temp = QtGui.QWidget()
            self.cards.append(temp)
            ui = Ui_Card(self.cards[len(self.cards) - 1], self.current_player)
            temp.show()



if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

    

