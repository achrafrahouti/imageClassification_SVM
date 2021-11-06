from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(457, 358)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(140, 50, 181, 31))
        self.btn.setObjectName("btn")
        
        
        self.dialog = QtWidgets.QFileDialog(self.centralwidget)
        self.dialog.setWindowTitle('Open wav File')
        self.dialog.setNameFilter('image files (*.png *.jpg)')
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(146, 100, 171, 121))
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(76, 242, 351, 31))
        self.resultat.setObjectName("resultat")
        font=QtGui.QFont()
        font.setPointSize(12)
        self.resultat.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Choisir image"))
        self.label.setText(_translate("MainWindow", "MACHINE A VECTEUR DE SUPPORTS"))
        self.img.setText(_translate("MainWindow", " "))
        self.resultat.setText(_translate("MainWindow", ""))

