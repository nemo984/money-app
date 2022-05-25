# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_wid.ui'
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
import resource_rc

class Ui_history_form(object):
    def setupUi(self, history_form):
        if not history_form.objectName():
            history_form.setObjectName(u"history_form")
        history_form.resize(885, 45)
        history_form.setMinimumSize(QSize(885, 45))
        history_form.setMaximumSize(QSize(885, 45))
        history_form.setStyleSheet(u"#history_form{\n"
"border: 1px solid black;\n"
"border-color: black white black white;\n"
"}")
        self.date_label = QLabel(history_form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(10, 10, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.date_label.setFont(font)
        self.type_label = QLabel(history_form)
        self.type_label.setObjectName(u"type_label")
        self.type_label.setGeometry(QRect(160, 10, 121, 31))
        self.type_label.setFont(font)
        self.action_label = QLabel(history_form)
        self.action_label.setObjectName(u"action_label")
        self.action_label.setGeometry(QRect(310, 10, 121, 31))
        self.action_label.setFont(font)
        self.description_label = QLabel(history_form)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setGeometry(QRect(460, 10, 351, 31))
        self.description_label.setFont(font)
        self.option_btn = QPushButton(history_form)
        self.option_btn.setObjectName(u"option_btn")
        self.option_btn.setGeometry(QRect(840, 10, 31, 31))
        self.option_btn.setStyleSheet(u"border :1px solid black;\n"
"border-radius:15px;\n"
"background-color:#A7F0AE;")
        icon = QIcon()
        icon.addFile(u":/black/icon/White/more-vertical.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.option_btn.setIcon(icon)

        self.retranslateUi(history_form)

        QMetaObject.connectSlotsByName(history_form)
    # setupUi

    def retranslateUi(self, history_form):
        history_form.setWindowTitle(QCoreApplication.translate("history_form", u"Form", None))
        self.date_label.setText(QCoreApplication.translate("history_form", u"xx/xx/xxxx", None))
        self.type_label.setText(QCoreApplication.translate("history_form", u"Income", None))
        self.action_label.setText(QCoreApplication.translate("history_form", u"Update", None))
        self.description_label.setText(QCoreApplication.translate("history_form", u"description", None))
        self.option_btn.setText("")
    # retranslateUi

