# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sun Mar 31 22:26:44 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 555)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 30, 271, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(40)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(500, 30, 71, 21))
        self.comboBox_2.setMaxVisibleItems(40)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("#label {\n"
"\n"
"color:#0094ff;\n"
"\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 101, 41))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("#label_2{\n"
"color:#0094ff;\n"
"\n"
"\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"\n"
"color:#0094ff;\n"
"background:#e0e0e0;\n"
"border-radius:60px;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 140, 281, 321))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"\n"
"color:#0094ff;\n"
"background:#e0e0e0;\n"
"border-radius:60px;\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(500, 140, 104, 321))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 100, 141, 41))
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3{\n"
"\n"
"color:#0094ff;\n"
"\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 100, 141, 41))
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("#label_4{\n"
"\n"
"color:#0094ff;\n"
"\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Movies", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Ratings", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Recommend", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Submit", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Movie names", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Ratings", None, -1))

