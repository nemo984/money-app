# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Popup_Expense.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(423, 322)
        Dialog.setStyleSheet(u"#addExpense_btn{\n"
"background-color:#A7F0AE;\n"
"border-radius: 10px;\n"
"}\n"
"#cancel_btn{\n"
"background-color:#A7F0AE;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(20, 260, 101, 31))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 10, 131, 16))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_5.setFont(font)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 161, 231))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.category_comboBox = QComboBox(self.layoutWidget)
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.setObjectName(u"category_comboBox")

        self.verticalLayout.addWidget(self.category_comboBox)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.budget_comboBox = QComboBox(self.layoutWidget)
        self.budget_comboBox.addItem("")
        self.budget_comboBox.setObjectName(u"budget_comboBox")

        self.verticalLayout.addWidget(self.budget_comboBox)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.amount_entry = QLineEdit(self.layoutWidget)
        self.amount_entry.setObjectName(u"amount_entry")

        self.verticalLayout.addWidget(self.amount_entry)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.date_entry = QDateEdit(self.layoutWidget)
        self.date_entry.setObjectName(u"date_entry")

        self.verticalLayout.addWidget(self.date_entry)

        self.note_entry = QTextEdit(self.frame)
        self.note_entry.setObjectName(u"note_entry")
        self.note_entry.setGeometry(QRect(210, 40, 161, 101))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 160, 211, 21))
        self.confirm_btn = QPushButton(self.frame)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setGeometry(QRect(270, 260, 101, 31))

        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Note(Optional)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.category_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Food", None))
        self.category_comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.category_comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Transport", None))
        self.category_comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Education", None))
        self.category_comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Healthcare", None))
        self.category_comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Bill", None))
        self.category_comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Saving", None))
        self.category_comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"Investment", None))
        self.category_comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"Shopping", None))
        self.category_comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"Utilities/Other", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"Budget(Optional)", None))
        self.budget_comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.label_6.setText("")
        self.confirm_btn.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
    # retranslateUi

