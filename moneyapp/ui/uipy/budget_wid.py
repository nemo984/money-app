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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QWidget)

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
        self.progressBar.setValue(24)
        self.hearde = QLabel(self.Budget_lay)
        self.hearde.setObjectName(u"hearde")
        self.hearde.setGeometry(QRect(20, 10, 71, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.hearde.setFont(font)
        self.amount = QLabel(self.Budget_lay)
        self.amount.setObjectName(u"amount")
        self.amount.setGeometry(QRect(20, 45, 101, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.amount.setFont(font1)
        self.label_9 = QLabel(self.Budget_lay)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 50, 221, 16))
        self.date = QLabel(self.Budget_lay)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(680, 110, 81, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.hearde.setText(QCoreApplication.translate("Form", u"Monthly", None))
        self.amount.setText(QCoreApplication.translate("Form", u"THB xx,xxx", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Until you reach THB xx,xxx", None))
        self.date.setText(QCoreApplication.translate("Form", u"Date", None))
    # retranslateUi

