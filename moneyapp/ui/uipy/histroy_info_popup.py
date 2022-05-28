# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'histroy_info_popup.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 170)
        self.date_label = QLabel(Form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(50, 10, 311, 20))
        self.brief = QLabel(Form)
        self.brief.setObjectName(u"brief")
        self.brief.setGeometry(QRect(117, 51, 271, 20))
        self.Action = QLabel(Form)
        self.Action.setObjectName(u"Action")
        self.Action.setGeometry(QRect(60, 31, 321, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Action.sizePolicy().hasHeightForWidth())
        self.Action.setSizePolicy(sizePolicy)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 31, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 31, 51, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 51, 101, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(11, 71, 111, 16))
        self.label_4.setFont(font)
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 90, 381, 71))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.date_label.setText("")
        self.brief.setText("")
        self.Action.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Action:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"brief_description:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Long description", None))
    # retranslateUi

