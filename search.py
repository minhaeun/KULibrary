# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from search_detail import SearchDetailDialog
import math


class SearchDialog(object):
    page = 1
    maxPage = 1
    title = None

    def __init__(self, dbmanager):
        self.dbmanager = dbmanager

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(646, 348)
        self.Dialog = Dialog
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(30, 80, 601, 221))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(30, 30, 32, 32))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label_27.setFont(font)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("ui/image/open-book.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 58, 16))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.txtPage = QtWidgets.QLineEdit(Dialog)
        self.txtPage.setGeometry(QtCore.QRect(280, 308, 51, 21))
        self.txtPage.setObjectName("txtPage")
        self.lbPage = QtWidgets.QLabel(Dialog)
        self.lbPage.setGeometry(QtCore.QRect(340, 310, 58, 16))
        self.lbPage.setObjectName("lbPage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "KU Library"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "No"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "제목"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "저자"))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "출판사"))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "대출가능 수"))
        self.label.setText(_translate("Dialog", "서적이름"))
        self.txtPage.setText(_translate("Dialog", "1"))
        self.lbPage.setText(_translate("Dialog", "/ 10"))

        self.txtPage.returnPressed.connect(lambda: self.txtPageChanged())
        self.lineEdit.returnPressed.connect(
            lambda: self.btnSearchClicked())
        self.treeWidget.itemDoubleClicked.connect(lambda item: self.itemDoubleClicked(item))

    def itemDoubleClicked(self, item):
        book_no = item.text(0) # book_no
        
        dialog = QtWidgets.QDialog(self.Dialog)
        dialog_ui = SearchDetailDialog(self.dbmanager, book_no)
        dialog_ui.setupUi(dialog)
        dialog.setModal(True)
        dialog.show()

    def show_alert(self, title, message):
        msgbox = QtWidgets.QMessageBox(self.Dialog)
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setText(message)
        msgbox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return msgbox.exec()

    def btnSearchClicked(self):
        self.page = 1
        title = self.lineEdit.text()
        self.title = title
        self.search_book()

    def txtPageChanged(self):
        try:
            if(self.title is not None):
                self.page = int(self.txtPage.text())
                if(self.page > 0):
                    self.search_book()
        except:
            pass

    def search_book(self):
        self.treeWidget.clear()
        page = self.page
        title = self.title
        pagesize = 10

        result = self.dbmanager.search_book(title, pagesize, page)  # 한페이지에 10개씩
        if(len(result) == 0):
            self.show_alert("검색 결과", "검색 결과가 없습니다.")
        else:
            for row in result:
                item = QtWidgets.QTreeWidgetItem(self.treeWidget)
                total = row['total']
                book_no = str(row['book_no'])
                title = row['title']
                author = row['author']
                publisher = row['publisher']
                count = str(row['count'])
                item.setText(0, book_no)
                item.setText(1, title)
                item.setText(2, author)
                item.setText(3, publisher)
                item.setText(4, count)

                totalPage = math.ceil(total / pagesize)
                self.txtPage.setText(str(page))
                self.lbPage.setText("/ %s"%totalPage)