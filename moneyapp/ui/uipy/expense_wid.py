# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expense_wid.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from .resource_rc import *

class Ui_expense_form(object):
    def setupUi(self, expense_form):
        if not expense_form.objectName():
            expense_form.setObjectName(u"expense_form")
        expense_form.resize(840, 45)
        expense_form.setMinimumSize(QSize(840, 45))
        expense_form.setMaximumSize(QSize(840, 45))
        expense_form.setStyleSheet(u"#expense_form{\n"
"border: 1px solid black;\n"
"border-color: black white black white;\n"
"}")
        self.date_label = QLabel(expense_form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(10, 10, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.date_label.setFont(font)
        self.category_label = QLabel(expense_form)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(140, 10, 111, 31))
        self.category_label.setFont(font)
        self.amount_label = QLabel(expense_form)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(260, 10, 171, 31))
        self.amount_label.setFont(font)
        self.option_btn = QPushButton(expense_form)
        self.option_btn.setObjectName(u"option_btn")
        self.option_btn.setGeometry(QRect(790, 10, 31, 31))
        self.option_btn.setStyleSheet(u"border :1px solid black;\n"
"border-radius:15px;\n"
"background-color:#A7F0AE;")
        icon = QIcon()
        icon.addFile(u":/black/icon/White/more-vertical.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.option_btn.setIcon(icon)
        self.budget_label = QLabel(expense_form)
        self.budget_label.setObjectName(u"budget_label")
        self.budget_label.setGeometry(QRect(430, 15, 361, 21))
        self.budget_label.setFont(font)

        self.retranslateUi(expense_form)

        QMetaObject.connectSlotsByName(expense_form)
    # setupUi

    def retranslateUi(self, expense_form):
        expense_form.setWindowTitle(QCoreApplication.translate("expense_form", u"Form", None))
        self.date_label.setText(QCoreApplication.translate("expense_form", u"xx/xx/xxxx", None))
        self.category_label.setText(QCoreApplication.translate("expense_form", u"Part-Time", None))
        self.amount_label.setText(QCoreApplication.translate("expense_form", u"98765 THB", None))
        self.option_btn.setText("")
        self.budget_label.setText(QCoreApplication.translate("expense_form", u"TextLabel", None))
    # retranslateUi

