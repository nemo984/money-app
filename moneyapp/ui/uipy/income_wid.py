# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'income_wid.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QWidget)
from .resource_rc import *


class Ui_income_form(object):
    def setupUi(self, income_form):
        if not income_form.objectName():
            income_form.setObjectName(u"income_form")
        income_form.resize(840, 45)
        income_form.setMinimumSize(QSize(840, 45))
        income_form.setMaximumSize(QSize(840, 45))
        font = QFont()
        font.setPointSize(12)
        income_form.setFont(font)
        income_form.setStyleSheet(u"#income_form{\n"
                                  "border: 1px solid black;\n"
                                  "border-color: black white black white;\n"
                                  "}")
        self.date_label = QLabel(income_form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(10, 10, 121, 31))
        self.date_label.setFont(font)
        self.name_label = QLabel(income_form)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(160, 10, 171, 31))
        self.name_label.setFont(font)
        self.category_label = QLabel(income_form)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(360, 10, 111, 31))
        self.category_label.setFont(font)
        self.amount_label = QLabel(income_form)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(500, 10, 141, 31))
        self.amount_label.setFont(font)
        self.recurrence_label = QLabel(income_form)
        self.recurrence_label.setObjectName(u"recurrence_label")
        self.recurrence_label.setGeometry(QRect(670, 10, 101, 31))
        self.recurrence_label.setFont(font)
        self.option_btn = QPushButton(income_form)
        self.option_btn.setObjectName(u"option_btn")
        self.option_btn.setGeometry(QRect(790, 10, 31, 31))
        self.option_btn.setStyleSheet(u"border :1px solid black;\n"
                                      "border-radius:15px;\n"
                                      "background-color:#A7F0AE;")
        icon = QIcon()
        icon.addFile(u":/black/icon/White/more-vertical.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.option_btn.setIcon(icon)

        self.retranslateUi(income_form)

        QMetaObject.connectSlotsByName(income_form)
    # setupUi

    def retranslateUi(self, income_form):
        income_form.setWindowTitle(
            QCoreApplication.translate("income_form", u"Form", None))
        self.date_label.setText(QCoreApplication.translate(
            "income_form", u"xx/xx/xxxx", None))
        self.name_label.setText(QCoreApplication.translate(
            "income_form", u"allowance", None))
        self.category_label.setText(QCoreApplication.translate(
            "income_form", u"Full-Time", None))
        self.amount_label.setText(QCoreApplication.translate(
            "income_form", u"12345 THB", None))
        self.recurrence_label.setText(
            QCoreApplication.translate("income_form", u"Yearly", None))
        self.option_btn.setText("")
    # retranslateUi
