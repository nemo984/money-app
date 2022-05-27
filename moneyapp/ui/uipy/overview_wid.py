# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'overview_wid.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
from .resource_rc import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(110, 110)
        Form.setMinimumSize(QSize(110, 110))
        Form.setMaximumSize(QSize(110, 110))
        self.category_label = QLabel(Form)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(10, 10, 91, 20))
        self.category_label.setAlignment(Qt.AlignCenter)
        self.icon_label = QLabel(Form)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setGeometry(QRect(30, 30, 51, 51))
        self.icon_label.setPixmap(
            QPixmap(u":/black/icon/White/alert-octagon.svg"))
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.amount_label = QLabel(Form)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(10, 80, 91, 21))
        self.amount_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.category_label.setText(
            QCoreApplication.translate("Form", u"category", None))
        self.icon_label.setText("")
        self.amount_label.setText(
            QCoreApplication.translate("Form", u"amount", None))
    # retranslateUi
