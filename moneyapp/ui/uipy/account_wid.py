# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_wid.ui'
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

class Ui_account_form(object):
    def setupUi(self, account_form):
        if not account_form.objectName():
            account_form.setObjectName(u"account_form")
        account_form.resize(385, 140)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(account_form.sizePolicy().hasHeightForWidth())
        account_form.setSizePolicy(sizePolicy)
        account_form.setMinimumSize(QSize(300, 100))
        account_form.setMaximumSize(QSize(500, 140))
        account_form.setLayoutDirection(Qt.LeftToRight)
        account_form.setStyleSheet(u"#account_form {\n"
"border: 1px solid black;\n"
"border-color: black white black white;\n"
"}\n"
"")
        self.label_2 = QLabel(account_form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 62, 16))
        self.name_label = QLabel(account_form)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(30, 20, 201, 16))
        self.last_login_label = QLabel(account_form)
        self.last_login_label.setObjectName(u"last_login_label")
        self.last_login_label.setGeometry(QRect(30, 100, 141, 16))
        self.profile_label = QLabel(account_form)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setGeometry(QRect(240, 20, 100, 100))
        self.profile_label.setMinimumSize(QSize(100, 100))
        self.profile_label.setMaximumSize(QSize(100, 100))
        self.profile_label.setScaledContents(True)
        self.label = QLabel(account_form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 91, 16))
        self.created_date_label = QLabel(account_form)
        self.created_date_label.setObjectName(u"created_date_label")
        self.created_date_label.setGeometry(QRect(30, 60, 141, 16))

        self.retranslateUi(account_form)

        QMetaObject.connectSlotsByName(account_form)
    # setupUi

    def retranslateUi(self, account_form):
        account_form.setWindowTitle(QCoreApplication.translate("account_form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("account_form", u"Last Login:", None))
        self.name_label.setText(QCoreApplication.translate("account_form", u"Ruy Lopez", None))
        self.last_login_label.setText(QCoreApplication.translate("account_form", u"24/4/2022 19:35", None))
        self.profile_label.setText("")
        self.label.setText(QCoreApplication.translate("account_form", u"Created Date:", None))
        self.created_date_label.setText(QCoreApplication.translate("account_form", u"24/4/2022 19:35", None))
    # retranslateUi

