from PyQt4 import QtCore, QtGui
from parse_data import *
from stat_card import *
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
        name = self.result_list.currentItem().text()
        log = getLog(self.results[name])
        img_url = getImg(log)
        data = urllib.request.urlopen(img_url).read()
        img = QtGui.QImage()
        img.loadFromData(data)
        pos = getPos(log)
        team = getTeam(log)
        stats = getStats(log, pos[1])


        self.current_player = [name, self.results[name], log, pos[0], pos[1], team, img, stats]
        #print(self.current_player)
        #print("here main")
        
        for x in stats:
            print(x)

        '''
        TODO: Use current player to get    
         - stats for each game
         - stats for total
         - dropdown for each cat
         - graph based on cat
         Don't really need player.py...
        '''

        temp = QtGui.QWidget()
        self.cards.append(temp)
        ui = Ui_Card()
        ui.setupUi(self.cards[len(self.cards) - 1], self.current_player[0], 
            self.current_player[3] + "-" + self.current_player[4], 
            self.current_player[5], self.current_player[6])
        self.cards[len(self.cards) - 1].show()
        

