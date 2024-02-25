# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(188, 255, 199, 255), stop:1 rgba(174, 231, 255, 255));")
        self.menu = QtWidgets.QPushButton(Dialog)
        self.menu.setGeometry(QtCore.QRect(40, 230, 81, 31))
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 203, 185);\n"
"    font: 9pt \"Montserrat Medium\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size:10.5pt;   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(229, 182, 166);       \n"
"}")
        self.menu.setObjectName("menu")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(280, 230, 81, 31))
        self.next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 170, 170);\n"
"    \n"
"    font: 9pt \"Montserrat Medium\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size:10.5pt;   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(229, 150, 150);       \n"
"}")
        self.next.setObjectName("next")
        self.restart = QtWidgets.QPushButton(Dialog)
        self.restart.setGeometry(QtCore.QRect(160, 232, 81, 31))
        self.restart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restart.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 203, 185);\n"
"    font: 9pt \"Montserrat Medium\";\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font-size:10.5pt;   \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(229, 182, 166);       \n"
"}")
        self.restart.setObjectName("pushButton_3")
        self.time_icon = QtWidgets.QPushButton(Dialog)
        self.time_icon.setGeometry(QtCore.QRect(50, 40, 61, 61))
        self.time_icon.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.time_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/clock_64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.time_icon.setIcon(icon)
        self.time_icon.setIconSize(QtCore.QSize(50, 50))
        self.time_icon.setObjectName("time_icon")
        self.key_icon = QtWidgets.QPushButton(Dialog)
        self.key_icon.setGeometry(QtCore.QRect(170, 40, 61, 61))
        self.key_icon.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.key_icon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/key_64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.key_icon.setIcon(icon1)
        self.key_icon.setIconSize(QtCore.QSize(50, 50))
        self.key_icon.setObjectName("key_icon")
        self.mist_icon = QtWidgets.QPushButton(Dialog)
        self.mist_icon.setGeometry(QtCore.QRect(290, 40, 61, 61))
        self.mist_icon.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.mist_icon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/mist_64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mist_icon.setIcon(icon2)
        self.mist_icon.setIconSize(QtCore.QSize(50, 50))
        self.mist_icon.setObjectName("mist_icon")
        self.time = QtWidgets.QLabel(Dialog)
        self.time.setGeometry(QtCore.QRect(50, 100, 61, 31))
        self.time.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Montserrat Medium\";")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.key = QtWidgets.QLabel(Dialog)
        self.key.setGeometry(QtCore.QRect(170, 100, 61, 31))
        self.key.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Montserrat Medium\";")
        self.key.setAlignment(QtCore.Qt.AlignCenter)
        self.key.setObjectName("key")
        self.mist = QtWidgets.QLabel(Dialog)
        self.mist.setGeometry(QtCore.QRect(290, 100, 61, 31))
        self.mist.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Montserrat Medium\";")
        self.mist.setAlignment(QtCore.Qt.AlignCenter)
        self.mist.setObjectName("mist")
        self.label_time = QtWidgets.QLabel(Dialog)
        self.label_time.setGeometry(QtCore.QRect(50, 150, 61, 41))
        self.label_time.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 13pt \"Montserrat Medium\";")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.label_key = QtWidgets.QLabel(Dialog)
        self.label_key.setGeometry(QtCore.QRect(176, 150, 51, 31))
        self.label_key.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 13pt \"Montserrat Medium\";")
        self.label_key.setAlignment(QtCore.Qt.AlignCenter)
        self.label_key.setObjectName("label_key")
        self.label_mist = QtWidgets.QLabel(Dialog)
        self.label_mist.setGeometry(QtCore.QRect(296, 150, 51, 31))
        self.label_mist.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 13pt \"Montserrat Medium\";")
        self.label_mist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mist.setObjectName("label_mist")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.menu.setText(_translate("Dialog", "Меню"))
        self.next.setText(_translate("Dialog", "Дальше"))
        self.restart.setText(_translate("Dialog", "Заново"))
        self.time.setText(_translate("Dialog", "Время:"))
        self.key.setText(_translate("Dialog", "Набрано:"))
        self.mist.setText(_translate("Dialog", "Ошибки:"))
        self.label_time.setText(_translate("Dialog", "00:00"))
        self.label_key.setText(_translate("Dialog", "0"))
        self.label_mist.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())