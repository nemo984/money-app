# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'notification_wid.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 40)
        Form.setMinimumSize(QSize(400, 0))
        Form.setMaximumSize(QSize(400, 40))
        self.date_label = QLabel(Form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(10, 10, 71, 21))
        self.action_label = QLabel(Form)
        self.action_label.setObjectName(u"action_label")
        self.action_label.setGeometry(QRect(90, 10, 61, 21))
        self.description_label = QLabel(Form)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setGeometry(QRect(160, 10, 191, 21))
        self.option_btn = QPushButton(Form)
        self.option_btn.setObjectName(u"option_btn")
        self.option_btn.setGeometry(QRect(370, 10, 21, 21))
        self.option_btn.setStyleSheet(u"background-color:transparent;")
        icon = QIcon()
        icon.addFile(u":/black/icon/White/more-vertical.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.option_btn.setIcon(icon)
        self.option_btn.setIconSize(QSize(20, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.date_label.setText(
            QCoreApplication.translate("Form", u"22/2/2222", None))
        self.action_label.setText(
            QCoreApplication.translate("Form", u"Budget", None))
        self.description_label.setText(QCoreApplication.translate(
            "Form", u"Expense exceed budget", None))
        self.option_btn.setText("")
    # retranslateUi
