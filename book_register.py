# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_register.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dbmanager import DBManager
import datetime

class BookRegisterDialog(object):
    def __init__(self, dbmanager):
        self.dbmanager = dbmanager

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 521)
        self.Dialog = Dialog
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Title")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("메이플스토리")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 220, 64, 15))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(170, 100, 32, 32))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_27.setFont(font)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("ui/image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 260, 64, 15))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Publisher")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 300, 64, 15))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QDateEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 290, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 390, 93, 28))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 180, 64, 15))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(160, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 330, 191, 31))
        self.lineEdit_2.setPlaceholderText("Author")
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 340, 64, 15))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.initEdits()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "KU Library"))
        self.label.setText(_translate("Dialog", "서적등록"))
        self.label_2.setText(_translate("Dialog", "도서명"))
        self.label_4.setText(_translate("Dialog", "출판사"))
        self.label_5.setText(_translate("Dialog", "출간일자"))
        self.pushButton.setText(_translate("Dialog", "등록"))
        self.label_8.setText(_translate("Dialog", "도서구분"))
        self.label_3.setText(_translate("Dialog", "저자"))

        self.btnConnect()
        self.getCategories()

    def getCategories(self):
        rows = self.dbmanager.inquery_category()
        if(rows):
            for row in rows:
                area_no = row['area_no']
                category = row['category']

                self.comboBox.addItem(category,'adfs')
                self.comboBox.setItemData(self.comboBox.count()-1, QtCore.QVariant(area_no))

    def btnConnect(self):
        self.pushButton.clicked.connect(lambda:self.btnPushButtonClicked())

    def btnPushButtonClicked(self):
        area_no = self.comboBox.currentData()
        title = self.lineEdit.text()
        publisher = self.lineEdit_3.text()
        published_date = self.lineEdit_4.text()
        author = self.lineEdit_2.text()

        result = self.dbmanager.request_book(
            title, area_no, publisher, published_date, author)
            
        if(result == 1):
            self.show_info("서적등록", "서적 등록 완료")
            self.initEdits()
        else:
            self.show_alert("서적등록", "서적 등록 실패")

    def initEdits(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setDate(datetime.datetime.now())
    def show_alert(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()

    def show_info(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Information)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()
 