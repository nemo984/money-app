# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_Ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import .resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
" color:#000;\n"
" border:none;\n"
"}\n"
"#centralwidget{\n"
" background-color:#FFFFFF;\n"
"}\n"
"#leftMenu{\n"
" background-color:#D5E6F6;\n"
"}\n"
"QPushButton{\n"
" background-color:transparent;\n"
"}\n"
"#label{\n"
" color:#D5E6F6;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(320, 720))
        self.leftMenu.setMaximumSize(QSize(320, 720))
        self.verticalLayout_6 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.leftMenu_2 = QFrame(self.leftMenu)
        self.leftMenu_2.setObjectName(u"leftMenu_2")
        self.leftMenu_2.setFrameShape(QFrame.StyledPanel)
        self.leftMenu_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.leftMenu_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Profile = QFrame(self.leftMenu_2)
        self.Profile.setObjectName(u"Profile")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Profile.sizePolicy().hasHeightForWidth())
        self.Profile.setSizePolicy(sizePolicy)
        self.Profile.setFrameShape(QFrame.StyledPanel)
        self.Profile.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Profile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.Profile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/black/icon/White/image.svg"))

        self.gridLayout.addWidget(self.label_3, 0, 0, 2, 1)

        self.label_2 = QLabel(self.Profile)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.Profile)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/black/icon/White/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(23, 23))

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.Profile, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_5 = QFrame(self.leftMenu_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Overview_btn = QPushButton(self.frame_5)
        self.Overview_btn.setObjectName(u"Overview_btn")
        self.Overview_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/black/icon/White/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Overview_btn.setIcon(icon1)
        self.Overview_btn.setIconSize(QSize(23, 23))

        self.verticalLayout_7.addWidget(self.Overview_btn)

        self.Budget_btn = QPushButton(self.frame_5)
        self.Budget_btn.setObjectName(u"Budget_btn")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.Budget_btn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/black/icon/White/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Budget_btn.setIcon(icon2)
        self.Budget_btn.setIconSize(QSize(23, 23))

        self.verticalLayout_7.addWidget(self.Budget_btn)

        self.Income_btn = QPushButton(self.frame_5)
        self.Income_btn.setObjectName(u"Income_btn")
        self.Income_btn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/black/icon/White/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Income_btn.setIcon(icon3)
        self.Income_btn.setIconSize(QSize(23, 23))

        self.verticalLayout_7.addWidget(self.Income_btn)

        self.Expense_btn = QPushButton(self.frame_5)
        self.Expense_btn.setObjectName(u"Expense_btn")
        self.Expense_btn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/black/icon/White/minus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Expense_btn.setIcon(icon4)
        self.Expense_btn.setIconSize(QSize(23, 23))

        self.verticalLayout_7.addWidget(self.Expense_btn)

        self.Analysis_btn = QPushButton(self.frame_5)
        self.Analysis_btn.setObjectName(u"Analysis_btn")
        self.Analysis_btn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/black/icon/White/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Analysis_btn.setIcon(icon5)
        self.Analysis_btn.setIconSize(QSize(23, 23))

        self.verticalLayout_7.addWidget(self.Analysis_btn)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.leftMenu_2)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        self.mainbody.setMaximumSize(QSize(16777215, 720))
        self.verticalLayout = QVBoxLayout(self.mainbody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.mainbody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.MenuButton = QPushButton(self.widget)
        self.MenuButton.setObjectName(u"MenuButton")
        self.MenuButton.setMaximumSize(QSize(34, 34))
        icon6 = QIcon()
        icon6.addFile(u":/Blue/icon/Blue/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MenuButton.setIcon(icon6)
        self.MenuButton.setIconSize(QSize(53, 53))

        self.horizontalLayout_3.addWidget(self.MenuButton)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.headerFrame)

        self.stackedWidget = QStackedWidget(self.mainbody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 140, 49, 16))

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 140, 49, 16))

        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 140, 49, 16))

        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 140, 49, 16))

        self.gridLayout_2.addWidget(self.frame_4, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText("")
        self.Overview_btn.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.Budget_btn.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.Income_btn.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.Expense_btn.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.Analysis_btn.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.MenuButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"box 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"box 2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"box 3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"box 4", None))
    # retranslateUi

