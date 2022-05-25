# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(647, 495)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#account_listWidget{\n"
"border:1px solid black;\n"
"}\n"
"\n"
"#login_btn,#create_btn{\n"
"background-color:#EDE6DB;\n"
"border:1px solid black;\n"
"}\n"
"\n"
"#create_btn_2{\n"
"background-color:#1A3C40;\n"
"border:1px solid black;\n"
"color: #FFFFFF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#back_btn{\n"
"background-color:#1D5C63;\n"
"border:1px solid black;\n"
"color: #FFFFFF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#upload_btn{\n"
"background-color:#EDE6DB;\n"
"border:1px solid black;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#login_page,#create_page{\n"
"background-image :url(:/background/login_background.jpg);\n"
"}\n"
"\n"
"#profile_label{\n"
"background-color: #FFFFFF;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_page.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.login_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.login_page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.account_listWidget = QListWidget(self.frame)
        self.account_listWidget.setObjectName(u"account_listWidget")
        self.account_listWidget.setMinimumSize(QSize(400, 0))
        self.account_listWidget.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout.addWidget(self.account_listWidget)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.login_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.staySignIn_checkBox = QCheckBox(self.frame_2)
        self.staySignIn_checkBox.setObjectName(u"staySignIn_checkBox")

        self.verticalLayout_2.addWidget(self.staySignIn_checkBox)

        self.login_btn = QPushButton(self.frame_2)
        self.login_btn.setObjectName(u"login_btn")
        font = QFont()
        font.setPointSize(12)
        self.login_btn.setFont(font)

        self.verticalLayout_2.addWidget(self.login_btn)

        self.create_btn = QPushButton(self.frame_2)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setFont(font)

        self.verticalLayout_2.addWidget(self.create_btn)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.login_page)
        self.create_page = QWidget()
        self.create_page.setObjectName(u"create_page")
        self.create_page.setStyleSheet(u"")
        self.label = QLabel(self.create_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 151, 16))
        self.label.setFont(font)
        self.name_lineEdit = QLineEdit(self.create_page)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setGeometry(QRect(60, 90, 191, 22))
        self.label_2 = QLabel(self.create_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 140, 151, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.create_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 230, 171, 16))
        self.label_3.setFont(font)
        self.password_lineEdit = QLineEdit(self.create_page)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(60, 180, 191, 22))
        self.passwordConfirm_lineEdit = QLineEdit(self.create_page)
        self.passwordConfirm_lineEdit.setObjectName(u"passwordConfirm_lineEdit")
        self.passwordConfirm_lineEdit.setGeometry(QRect(60, 270, 191, 21))
        self.profile_label = QLabel(self.create_page)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setGeometry(QRect(450, 70, 110, 110))
        self.profile_label.setMinimumSize(QSize(110, 110))
        self.profile_label.setMaximumSize(QSize(110, 110))
        self.profile_label.setStyleSheet(u"border: 1px solid black;\n"
"")
        self.profile_label.setScaledContents(True)
        self.upload_btn = QPushButton(self.create_page)
        self.upload_btn.setObjectName(u"upload_btn")
        self.upload_btn.setGeometry(QRect(450, 210, 111, 41))
        self.create_btn_2 = QPushButton(self.create_page)
        self.create_btn_2.setObjectName(u"create_btn_2")
        self.create_btn_2.setGeometry(QRect(450, 390, 111, 41))
        self.create_btn_2.setFont(font)
        self.back_btn = QPushButton(self.create_page)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(60, 390, 111, 41))
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"")
        self.warning_label = QLabel(self.create_page)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(200, 200, 181, 21))
        self.stackedWidget.addWidget(self.create_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.staySignIn_checkBox.setText(QCoreApplication.translate("MainWindow", u"Stayed logged in", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"Create New Account", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.profile_label.setText("")
        self.upload_btn.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.create_btn_2.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.warning_label.setText("")
    # retranslateUi

