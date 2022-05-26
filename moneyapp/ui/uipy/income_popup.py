# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Popup_Income.ui'
##
# Created by: Qt User Interface Compiler version 6.2.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
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
        Dialog.resize(433, 386)
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
        self.cancel_btn.setGeometry(QRect(20, 330, 101, 31))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 10, 131, 16))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_5.setFont(font)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(210, 40, 161, 101))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 160, 211, 21))
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 11, 161, 291))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.name_entry = QLineEdit(self.layoutWidget)
        self.name_entry.setObjectName(u"name_entry")

        self.verticalLayout.addWidget(self.name_entry)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.category_comboBox = QComboBox(self.layoutWidget)
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.setObjectName(u"category_comboBox")

        self.verticalLayout.addWidget(self.category_comboBox)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.amount_entry = QLineEdit(self.layoutWidget)
        self.amount_entry.setObjectName(u"amount_entry")

        self.verticalLayout.addWidget(self.amount_entry)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout.addWidget(self.label_7)

        self.recurence_comboBox = QComboBox(self.layoutWidget)
        self.recurence_comboBox.addItem("")
        self.recurence_comboBox.addItem("")
        self.recurence_comboBox.addItem("")
        self.recurence_comboBox.addItem("")
        self.recurence_comboBox.addItem("")
        self.recurence_comboBox.setObjectName(u"recurence_comboBox")

        self.verticalLayout.addWidget(self.recurence_comboBox)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.date_entry = QDateEdit(self.layoutWidget)
        self.date_entry.setObjectName(u"date_entry")

        self.verticalLayout.addWidget(self.date_entry)

        self.confirm_btn = QPushButton(self.frame)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setGeometry(QRect(290, 330, 101, 31))

        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancel_btn.setText(
            QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_5.setText(QCoreApplication.translate(
            "Dialog", u"Note(Optional)", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate(
            "Dialog", u"Category", None))
        self.category_comboBox.setItemText(
            0, QCoreApplication.translate("Dialog", u"Full-time", None))
        self.category_comboBox.setItemText(
            1, QCoreApplication.translate("Dialog", u"Part-time", None))
        self.category_comboBox.setItemText(
            2, QCoreApplication.translate("Dialog", u"Passive", None))
        self.category_comboBox.setItemText(
            3, QCoreApplication.translate("Dialog", u"Other", None))

        self.label_3.setText(
            QCoreApplication.translate("Dialog", u"Amount", None))
        self.label_7.setText(QCoreApplication.translate(
            "Dialog", u"Recurrence", None))
        self.recurence_comboBox.setItemText(
            0, QCoreApplication.translate("Dialog", u"one-time", None))
        self.recurence_comboBox.setItemText(
            1, QCoreApplication.translate("Dialog", u"daily", None))
        self.recurence_comboBox.setItemText(
            2, QCoreApplication.translate("Dialog", u"weekly", None))
        self.recurence_comboBox.setItemText(
            3, QCoreApplication.translate("Dialog", u"monthly", None))
        self.recurence_comboBox.setItemText(
            4, QCoreApplication.translate("Dialog", u"yearly", None))

        self.label_4.setText(
            QCoreApplication.translate("Dialog", u"Date", None))
        self.confirm_btn.setText(
            QCoreApplication.translate("Dialog", u"Confirm", None))
    # retranslateUi
