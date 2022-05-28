# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_info_popup.ui'
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
        Form.resize(400, 228)
        self.date_label = QLabel(Form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(60, 0, 291, 31))
        self.brief_description_label = QLabel(Form)
        self.brief_description_label.setObjectName(u"brief_description_label")
        self.brief_description_label.setGeometry(QRect(60, 70, 331, 20))
        self.type_label = QLabel(Form)
        self.type_label.setObjectName(u"type_label")
        self.type_label.setGeometry(QRect(60, 30, 311, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type_label.sizePolicy().hasHeightForWidth())
        self.type_label.setSizePolicy(sizePolicy)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 5, 41, 21))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 31, 41, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 71, 41, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 90, 111, 16))
        self.label_4.setFont(font)
        self.long_description_textEdit = QTextEdit(Form)
        self.long_description_textEdit.setObjectName(u"long_description_textEdit")
        self.long_description_textEdit.setGeometry(QRect(10, 110, 381, 111))
        self.long_description_textEdit.setStyleSheet(u"border: 1px solid black;")
        self.long_description_textEdit.setReadOnly(True)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(11, 51, 51, 16))
        self.label_5.setFont(font)
        self.action_label = QLabel(Form)
        self.action_label.setObjectName(u"action_label")
        self.action_label.setGeometry(QRect(70, 50, 301, 20))
        sizePolicy.setHeightForWidth(self.action_label.sizePolicy().hasHeightForWidth())
        self.action_label.setSizePolicy(sizePolicy)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.date_label.setText(QCoreApplication.translate("Form", u"sfsf", None))
        self.brief_description_label.setText(QCoreApplication.translate("Form", u"fdffa", None))
        self.type_label.setText(QCoreApplication.translate("Form", u"dfdf", None))
        self.label.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Type:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Brief:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Long description:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Action:", None))
        self.action_label.setText(QCoreApplication.translate("Form", u"dffd", None))
    # retranslateUi

