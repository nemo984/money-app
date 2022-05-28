# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminder_info_popup.ui'
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
        Form.resize(400, 245)
        self.date_label = QLabel(Form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(10, 10, 101, 16))
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(10, 50, 371, 16))
        self.remaining_label = QLabel(Form)
        self.remaining_label.setObjectName(u"remaining_label")
        self.remaining_label.setGeometry(QRect(10, 110, 321, 31))
        self.title_label_2 = QLabel(Form)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setGeometry(QRect(10, 30, 55, 16))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 160, 381, 81))
        self.textEdit.setReadOnly(True)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 140, 71, 16))
        self.start_date_label = QLabel(Form)
        self.start_date_label.setObjectName(u"start_date_label")
        self.start_date_label.setGeometry(QRect(10, 70, 211, 16))
        self.end_date_label = QLabel(Form)
        self.end_date_label.setObjectName(u"end_date_label")
        self.end_date_label.setGeometry(QRect(10, 90, 171, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.date_label.setText(QCoreApplication.translate("Form", u"Date", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Budget Title", None))
        self.remaining_label.setText(QCoreApplication.translate("Form", u"Budget Remaining:", None))
        self.title_label_2.setText(QCoreApplication.translate("Form", u"Title", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Budget Note", None))
        self.start_date_label.setText(QCoreApplication.translate("Form", u"Budget Start Date", None))
        self.end_date_label.setText(QCoreApplication.translate("Form", u"Budget End Date", None))
    # retranslateUi

