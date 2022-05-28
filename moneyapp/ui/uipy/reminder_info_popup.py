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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 172)
        self.date_label = QLabel(Form)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(60, 10, 301, 20))
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(107, 51, 281, 20))
        self.remaining_label = QLabel(Form)
        self.remaining_label.setObjectName(u"remaining_label")
        self.remaining_label.setGeometry(QRect(140, 150, 241, 20))
        self.title_label_2 = QLabel(Form)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setGeometry(QRect(50, 31, 331, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label_2.sizePolicy().hasHeightForWidth())
        self.title_label_2.setSizePolicy(sizePolicy)
        self.start_date_label = QLabel(Form)
        self.start_date_label.setObjectName(u"start_date_label")
        self.start_date_label.setGeometry(QRect(141, 71, 251, 20))
        self.end_date_label = QLabel(Form)
        self.end_date_label.setObjectName(u"end_date_label")
        self.end_date_label.setGeometry(QRect(137, 91, 251, 20))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 41, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 31, 31, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 51, 81, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(11, 71, 131, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(11, 91, 111, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 150, 131, 16))
        self.label_6.setFont(font)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 110, 91, 16))
        self.label_7.setFont(font)
        self.total_budget = QLabel(Form)
        self.total_budget.setObjectName(u"total_budget")
        self.total_budget.setGeometry(QRect(140, 110, 231, 20))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 130, 91, 16))
        self.label_8.setFont(font)
        self.used_label = QLabel(Form)
        self.used_label.setObjectName(u"used_label")
        self.used_label.setGeometry(QRect(140, 130, 251, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.date_label.setText("")
        self.title_label.setText(QCoreApplication.translate("Form", u"T", None))
        self.remaining_label.setText(QCoreApplication.translate("Form", u"T", None))
        self.title_label_2.setText(QCoreApplication.translate("Form", u"T", None))
        self.start_date_label.setText(QCoreApplication.translate("Form", u"T", None))
        self.end_date_label.setText(QCoreApplication.translate("Form", u"T", None))
        self.label.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Title:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Budget Title:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Budget Start Date:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Budget End Date:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Budget Remaining:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Budget Total:", None))
        self.total_budget.setText(QCoreApplication.translate("Form", u"T", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Budget Used:", None))
        self.used_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

