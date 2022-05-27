# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'budget_wid.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QWidget)
from .resource_rc import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 140)
        Form.setMinimumSize(QSize(800, 140))
        Form.setMaximumSize(QSize(800, 140))
        Form.setStyleSheet(u"#Budget_lay{\n"
" border: 1px solid black;\n"
" border-radius: 30px;\n"
"}\n"
"#progressBar{\n"
"background-color:#C4C4C4;\n"
"border-radius: 10px;\n"
"}\n"
"#more_btn{\n"
"background-color:transparent;\n"
"}")
        self.Budget_lay = QWidget(Form)
        self.Budget_lay.setObjectName(u"Budget_lay")
        self.Budget_lay.setGeometry(QRect(0, 0, 800, 140))
        self.Budget_lay.setMinimumSize(QSize(800, 140))
        self.Budget_lay.setMaximumSize(QSize(800, 140))
        self.Budget_lay.setStyleSheet(u"")
        self.progressBar = QProgressBar(self.Budget_lay)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 80, 761, 31))
        self.progressBar.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.category_label = QLabel(self.Budget_lay)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(630, 20, 91, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.category_label.setFont(font)
        self.amount = QLabel(self.Budget_lay)
        self.amount.setObjectName(u"amount")
        self.amount.setGeometry(QRect(20, 45, 281, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.amount.setFont(font1)
        self.label_9 = QLabel(self.Budget_lay)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(330, 50, 421, 20))
        self.end_date = QLabel(self.Budget_lay)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(640, 110, 131, 20))
        self.more_btn = QPushButton(self.Budget_lay)
        self.more_btn.setObjectName(u"more_btn")
        self.more_btn.setGeometry(QRect(740, 10, 51, 31))
        icon = QIcon()
        icon.addFile(u":/black/icon/White/more-vertical.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.more_btn.setIcon(icon)
        self.more_btn.setIconSize(QSize(24, 24))
        self.start_date = QLabel(self.Budget_lay)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(20, 110, 121, 20))
        self.name_label = QLabel(self.Budget_lay)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(20, 20, 491, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.category_label.setText(QCoreApplication.translate("Form", u"Bus", None))
        self.amount.setText(QCoreApplication.translate("Form", u"THB xx,xxx", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Until you reach THB xx,xxx", None))
        self.end_date.setText(QCoreApplication.translate("Form", u"Date", None))
        self.more_btn.setText("")
        self.start_date.setText(QCoreApplication.translate("Form", u"Date", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"Name", None))
    # retranslateUi

