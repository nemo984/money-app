# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mono.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
from .resource_rc import *

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
"}\n"
"#Budget_widdget{\n"
"border: 1px solid black;\n"
" border-radius: 35px;\n"
"}\n"
"#Expanse_widdget{\n"
"border: 1px solid black;\n"
" border-radius: 35px;\n"
"}\n"
"#Notification_widdget{\n"
" border: 1px solid black;\n"
" border-radius: 35px;\n"
"}\n"
"#pie_widdget{\n"
" border-radius: 35px;\n"
" border: 1px solid black;\n"
"}\n"
"#add_Budget{\n"
"background-color:#A7F0AE;\n"
"border-radius: 25px;\n"
"}\n"
"#scrollArea{\n"
"background-color:transparent;\n"
"}\n"
"#Budget_lay{\n"
" border: 1px solid black;\n"
" border-radius: 30px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(320, 720))
        self.leftMenu.setMaximumSize(QSize(0, 720))
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
        self.name_label = QLabel(self.Profile)
        self.name_label.setObjectName(u"name_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)

        self.gridLayout.addWidget(self.name_label, 0, 1, 1, 1)

        self.setting_btn = QPushButton(self.Profile)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy1.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/black/icon/White/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon)
        self.setting_btn.setIconSize(QSize(23, 23))

        self.gridLayout.addWidget(self.setting_btn, 1, 1, 1, 1)

        self.profileImg_label = QLabel(self.Profile)
        self.profileImg_label.setObjectName(u"profileImg_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(70)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profileImg_label.sizePolicy().hasHeightForWidth())
        self.profileImg_label.setSizePolicy(sizePolicy2)
        self.profileImg_label.setMinimumSize(QSize(70, 70))
        self.profileImg_label.setMaximumSize(QSize(70, 70))
        self.profileImg_label.setPixmap(QPixmap(u":/black/icon/White/alert-octagon.svg"))
        self.profileImg_label.setScaledContents(True)

        self.gridLayout.addWidget(self.profileImg_label, 0, 0, 2, 1)


        self.verticalLayout_5.addWidget(self.Profile, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_5 = QFrame(self.leftMenu_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
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

        self.tab_level = QLabel(self.widget)
        self.tab_level.setObjectName(u"tab_level")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.tab_level.setFont(font2)

        self.horizontalLayout_3.addWidget(self.tab_level)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.headerFrame)

        self.stackedWidget = QStackedWidget(self.mainbody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(3, 0, 481, 405))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.widget_8 = QWidget(self.frame)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.widget_8.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.widget_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.comboBox = QComboBox(self.widget_8)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))
        self.comboBox.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_11.addWidget(self.comboBox, 0, Qt.AlignLeft)

        self.pie_widdget = QWidget(self.widget_8)
        self.pie_widdget.setObjectName(u"pie_widdget")
        self.pie_widdget.setMinimumSize(QSize(445, 369))
        self.pie_widdget.setMaximumSize(QSize(369, 16777215))

        self.verticalLayout_11.addWidget(self.pie_widdget)


        self.verticalLayout_19.addWidget(self.widget_8)

        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(3, 409, 465, 231))
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 0, 0, 0)
        self.widget_5 = QWidget(self.frame_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_9 = QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_8.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.Notification_widdget = QWidget(self.frame_4)
        self.Notification_widdget.setObjectName(u"Notification_widdget")
        self.Notification_widdget.setMinimumSize(QSize(445, 207))
        self.Notification_widdget.setMaximumSize(QSize(445, 207))
        self.verticalLayout_41 = QVBoxLayout(self.Notification_widdget)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_8 = QFrame(self.Notification_widdget)
        self.frame_8.setObjectName(u"frame_8")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.frame_8.setFont(font3)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout_20.addWidget(self.label_6)


        self.verticalLayout_41.addWidget(self.frame_8)

        self.scrollArea_7 = QScrollArea(self.Notification_widdget)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u"background-color:transparent;")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 423, 132))
        self.notification_list = QWidget(self.scrollAreaWidgetContents_7)
        self.notification_list.setObjectName(u"notification_list")
        self.notification_list.setGeometry(QRect(0, 0, 421, 131))
        self.notification_list.setStyleSheet(u"")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_41.addWidget(self.scrollArea_7)


        self.verticalLayout_8.addWidget(self.Notification_widdget)

        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(490, 214, 441, 431))
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_4 = QWidget(self.frame_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Expanse_widdget = QWidget(self.widget_4)
        self.Expanse_widdget.setObjectName(u"Expanse_widdget")
        self.Expanse_widdget.setMinimumSize(QSize(405, 395))
        self.Expanse_widdget.setMaximumSize(QSize(405, 395))
        self.verticalLayout_18 = QVBoxLayout(self.Expanse_widdget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_7 = QFrame(self.Expanse_widdget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_4)


        self.verticalLayout_18.addWidget(self.frame_7)

        self.scrollArea_6 = QScrollArea(self.Expanse_widdget)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u"background-color:transparent;")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 383, 320))
        self.verticalLayout_42 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.widget_7 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_42.addWidget(self.widget_7)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_18.addWidget(self.scrollArea_6)


        self.verticalLayout_4.addWidget(self.Expanse_widdget, 0, Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(490, 0, 455, 208))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(420, 190))
        self.widget_2.setMaximumSize(QSize(411, 173))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Budget_widdget = QWidget(self.widget_2)
        self.Budget_widdget.setObjectName(u"Budget_widdget")
        self.Budget_widdget.setMinimumSize(QSize(405, 167))
        self.frame_6 = QFrame(self.Budget_widdget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 111, 51))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.Budget_widdget)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")
        self.frame_9 = QFrame(self.page_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 942, 650))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_3 = QWidget(self.frame_9)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_23 = QVBoxLayout(self.widget_3)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 898, 522))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.budget_list = QWidget(self.scrollAreaWidgetContents)
        self.budget_list.setObjectName(u"budget_list")

        self.verticalLayout_24.addWidget(self.budget_list)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_23.addWidget(self.scrollArea)


        self.verticalLayout_22.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.frame_9)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_31 = QVBoxLayout(self.widget_6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.add_Budget = QPushButton(self.widget_6)
        self.add_Budget.setObjectName(u"add_Budget")
        self.add_Budget.setMinimumSize(QSize(272, 55))
        self.add_Budget.setMaximumSize(QSize(272, 55))
        self.add_Budget.setFont(font3)

        self.verticalLayout_31.addWidget(self.add_Budget)


        self.verticalLayout_22.addWidget(self.widget_6, 0, Qt.AlignRight|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"#incomeList_frame,#income_report_graph,#income_daily_frame,#income_weekly_frame,#income_monthly_frame,#income_yearly_frame {\n"
"border :1px solid black;\n"
"border-radius:20px\n"
"}\n"
"\n"
"#income_daily,#income_weekly,#income_monthly,#income_yearly,#frame_21 {\n"
"border-width:1px;\n"
"border-style: solid;\n"
" border-color: white white black white;\n"
"}\n"
"\n"
"#income_daily_value ,#income_weekly_value ,#income_monthly_value ,#income_yearly_value {\n"
"border-width: 1px; \n"
"border-style: solid;\n"
"border-color: black white white white;\n"
"}\n"
"\n"
"#add_income_button{\n"
"border :2px solid black;\n"
"border-radius:15px;\n"
"background-color:#A7F0AE;\n"
"}")
        self.income_report_graph = QFrame(self.page_3)
        self.income_report_graph.setObjectName(u"income_report_graph")
        self.income_report_graph.setGeometry(QRect(10, 10, 942, 322))
        self.income_report_graph.setStyleSheet(u"")
        self.income_report_graph.setFrameShape(QFrame.StyledPanel)
        self.income_report_graph.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.income_report_graph)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.totalIncome_frame = QFrame(self.income_report_graph)
        self.totalIncome_frame.setObjectName(u"totalIncome_frame")
        self.totalIncome_frame.setStyleSheet(u"")
        self.totalIncome_frame.setFrameShape(QFrame.StyledPanel)
        self.totalIncome_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.totalIncome_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.income_yearly_frame = QFrame(self.totalIncome_frame)
        self.income_yearly_frame.setObjectName(u"income_yearly_frame")
        self.income_yearly_frame.setFrameShape(QFrame.StyledPanel)
        self.income_yearly_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.income_yearly_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.income_yearly = QLabel(self.income_yearly_frame)
        self.income_yearly.setObjectName(u"income_yearly")
        font4 = QFont()
        font4.setBold(True)
        self.income_yearly.setFont(font4)

        self.verticalLayout_32.addWidget(self.income_yearly)

        self.income_yearly_value = QLabel(self.income_yearly_frame)
        self.income_yearly_value.setObjectName(u"income_yearly_value")

        self.verticalLayout_32.addWidget(self.income_yearly_value)


        self.gridLayout_8.addWidget(self.income_yearly_frame, 1, 1, 1, 1)

        self.income_monthly_frame = QFrame(self.totalIncome_frame)
        self.income_monthly_frame.setObjectName(u"income_monthly_frame")
        self.income_monthly_frame.setStyleSheet(u"")
        self.income_monthly_frame.setFrameShape(QFrame.StyledPanel)
        self.income_monthly_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.income_monthly_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.income_monthly = QLabel(self.income_monthly_frame)
        self.income_monthly.setObjectName(u"income_monthly")
        self.income_monthly.setFont(font4)

        self.verticalLayout_33.addWidget(self.income_monthly)

        self.income_monthly_value = QLabel(self.income_monthly_frame)
        self.income_monthly_value.setObjectName(u"income_monthly_value")

        self.verticalLayout_33.addWidget(self.income_monthly_value)


        self.gridLayout_8.addWidget(self.income_monthly_frame, 1, 0, 1, 1)

        self.income_daily_frame = QFrame(self.totalIncome_frame)
        self.income_daily_frame.setObjectName(u"income_daily_frame")
        self.income_daily_frame.setFrameShape(QFrame.StyledPanel)
        self.income_daily_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.income_daily_frame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.income_daily = QLabel(self.income_daily_frame)
        self.income_daily.setObjectName(u"income_daily")
        self.income_daily.setFont(font4)

        self.verticalLayout_34.addWidget(self.income_daily)

        self.income_daily_value = QLabel(self.income_daily_frame)
        self.income_daily_value.setObjectName(u"income_daily_value")

        self.verticalLayout_34.addWidget(self.income_daily_value)


        self.gridLayout_8.addWidget(self.income_daily_frame, 0, 0, 1, 1)

        self.income_weekly_frame = QFrame(self.totalIncome_frame)
        self.income_weekly_frame.setObjectName(u"income_weekly_frame")
        self.income_weekly_frame.setFrameShape(QFrame.StyledPanel)
        self.income_weekly_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.income_weekly_frame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.income_weekly = QLabel(self.income_weekly_frame)
        self.income_weekly.setObjectName(u"income_weekly")
        self.income_weekly.setFont(font4)

        self.verticalLayout_35.addWidget(self.income_weekly)

        self.income_weekly_value = QLabel(self.income_weekly_frame)
        self.income_weekly_value.setObjectName(u"income_weekly_value")

        self.verticalLayout_35.addWidget(self.income_weekly_value)


        self.gridLayout_8.addWidget(self.income_weekly_frame, 0, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.totalIncome_frame)

        self.frame_16 = QFrame(self.income_report_graph)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.income_pie = QWidget(self.frame_16)
        self.income_pie.setObjectName(u"income_pie")
        self.income_pie.setGeometry(QRect(10, 9, 441, 281))

        self.horizontalLayout_9.addWidget(self.frame_16)

        self.incomeList_frame = QFrame(self.page_3)
        self.incomeList_frame.setObjectName(u"incomeList_frame")
        self.incomeList_frame.setGeometry(QRect(10, 340, 942, 321))
        self.incomeList_frame.setStyleSheet(u"")
        self.incomeList_frame.setFrameShape(QFrame.StyledPanel)
        self.incomeList_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.incomeList_frame)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_21 = QFrame(self.incomeList_frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_21)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.income_lineEdit = QLineEdit(self.frame_21)
        self.income_lineEdit.setObjectName(u"income_lineEdit")
        self.income_lineEdit.setStyleSheet(u"border: 1px solid black;")

        self.verticalLayout_37.addWidget(self.income_lineEdit)

        self.income_list_header = QLabel(self.frame_21)
        self.income_list_header.setObjectName(u"income_list_header")
        self.income_list_header.setFont(font4)

        self.verticalLayout_37.addWidget(self.income_list_header)


        self.verticalLayout_36.addWidget(self.frame_21, 0, Qt.AlignTop)

        self.frame_22 = QFrame(self.incomeList_frame)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy4)
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.add_income_button = QPushButton(self.frame_22)
        self.add_income_button.setObjectName(u"add_income_button")
        self.add_income_button.setGeometry(QRect(880, 180, 31, 31))
        self.add_income_button.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/black/icon/White/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_income_button.setIcon(icon7)
        self.scrollArea_5 = QScrollArea(self.frame_22)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(0, 0, 871, 231))
        self.scrollArea_5.setStyleSheet(u"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 871, 231))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"background-color:#FFFFFF;")
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.income_list = QWidget(self.scrollAreaWidgetContents_4)
        self.income_list.setObjectName(u"income_list")

        self.verticalLayout_40.addWidget(self.income_list)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_36.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"#expenseList_frame,#expense_report_graph,#expense_daily_frame,#expense_weekly_frame,#expense_monthly_frame,#expense_yearly_frame {\n"
"border :1px solid black;\n"
"border-radius:20px\n"
"}\n"
"\n"
"#expense_daily,#expense_weekly,#expense_monthly,#expense_yearly,#frame_19 {\n"
"border-width:1px;\n"
"border-style: solid; \n"
"border-color: white white black white;\n"
"}\n"
"\n"
"#expense_daily_value ,#expense_monthly_value ,#expense_yearly_value {\n"
"border-width: 1px;\n"
" border-style: solid;\n"
"border-color: black white white white;\n"
"}\n"
"\n"
"#expense_weekly_value {\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: black white white white;\n"
"}\n"
"\n"
"#add_expense_button{\n"
"border :2px solid black;\n"
"border-radius:15px;\n"
"background-color:#A7F0AE;\n"
"}\n"
"")
        self.expenseList_frame = QFrame(self.page_4)
        self.expenseList_frame.setObjectName(u"expenseList_frame")
        self.expenseList_frame.setGeometry(QRect(10, 340, 942, 321))
        self.expenseList_frame.setStyleSheet(u"")
        self.expenseList_frame.setFrameShape(QFrame.StyledPanel)
        self.expenseList_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.expenseList_frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_19 = QFrame(self.expenseList_frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_19)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.expense_lineEdit = QLineEdit(self.frame_19)
        self.expense_lineEdit.setObjectName(u"expense_lineEdit")
        self.expense_lineEdit.setStyleSheet(u"border: 1px solid black;")

        self.verticalLayout_26.addWidget(self.expense_lineEdit)

        self.expense_list_header = QLabel(self.frame_19)
        self.expense_list_header.setObjectName(u"expense_list_header")
        self.expense_list_header.setFont(font4)

        self.verticalLayout_26.addWidget(self.expense_list_header)


        self.verticalLayout_25.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.frame_20 = QFrame(self.expenseList_frame)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy4.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy4)
        self.frame_20.setMaximumSize(QSize(16777215, 16777215))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.add_expense_button = QPushButton(self.frame_20)
        self.add_expense_button.setObjectName(u"add_expense_button")
        self.add_expense_button.setGeometry(QRect(880, 180, 31, 31))
        self.add_expense_button.setStyleSheet(u"")
        self.add_expense_button.setIcon(icon7)
        self.scrollArea_3 = QScrollArea(self.frame_20)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(0, 0, 871, 231))
        self.scrollArea_3.setStyleSheet(u"background-color:transparent;")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 871, 231))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"background-color:#FFFFFF;")
        self.verticalLayout_38 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.expense_list = QWidget(self.scrollAreaWidgetContents_3)
        self.expense_list.setObjectName(u"expense_list")

        self.verticalLayout_38.addWidget(self.expense_list)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_25.addWidget(self.frame_20)

        self.expense_report_graph = QFrame(self.page_4)
        self.expense_report_graph.setObjectName(u"expense_report_graph")
        self.expense_report_graph.setGeometry(QRect(10, 10, 942, 322))
        self.expense_report_graph.setStyleSheet(u"")
        self.expense_report_graph.setFrameShape(QFrame.StyledPanel)
        self.expense_report_graph.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.expense_report_graph)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.totalExpense_frame = QFrame(self.expense_report_graph)
        self.totalExpense_frame.setObjectName(u"totalExpense_frame")
        self.totalExpense_frame.setStyleSheet(u"")
        self.totalExpense_frame.setFrameShape(QFrame.StyledPanel)
        self.totalExpense_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.totalExpense_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.expense_yearly_frame = QFrame(self.totalExpense_frame)
        self.expense_yearly_frame.setObjectName(u"expense_yearly_frame")
        self.expense_yearly_frame.setFrameShape(QFrame.StyledPanel)
        self.expense_yearly_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.expense_yearly_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.expense_yearly = QLabel(self.expense_yearly_frame)
        self.expense_yearly.setObjectName(u"expense_yearly")
        self.expense_yearly.setFont(font4)

        self.verticalLayout_27.addWidget(self.expense_yearly)

        self.expense_yearly_value = QLabel(self.expense_yearly_frame)
        self.expense_yearly_value.setObjectName(u"expense_yearly_value")

        self.verticalLayout_27.addWidget(self.expense_yearly_value)


        self.gridLayout_7.addWidget(self.expense_yearly_frame, 1, 1, 1, 1)

        self.expense_monthly_frame = QFrame(self.totalExpense_frame)
        self.expense_monthly_frame.setObjectName(u"expense_monthly_frame")
        self.expense_monthly_frame.setStyleSheet(u"")
        self.expense_monthly_frame.setFrameShape(QFrame.StyledPanel)
        self.expense_monthly_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.expense_monthly_frame)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.expense_monthly = QLabel(self.expense_monthly_frame)
        self.expense_monthly.setObjectName(u"expense_monthly")
        self.expense_monthly.setFont(font4)

        self.verticalLayout_28.addWidget(self.expense_monthly)

        self.expense_monthly_value = QLabel(self.expense_monthly_frame)
        self.expense_monthly_value.setObjectName(u"expense_monthly_value")

        self.verticalLayout_28.addWidget(self.expense_monthly_value)


        self.gridLayout_7.addWidget(self.expense_monthly_frame, 1, 0, 1, 1)

        self.expense_daily_frame = QFrame(self.totalExpense_frame)
        self.expense_daily_frame.setObjectName(u"expense_daily_frame")
        self.expense_daily_frame.setFrameShape(QFrame.StyledPanel)
        self.expense_daily_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.expense_daily_frame)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.expense_daily = QLabel(self.expense_daily_frame)
        self.expense_daily.setObjectName(u"expense_daily")
        self.expense_daily.setFont(font4)

        self.verticalLayout_29.addWidget(self.expense_daily)

        self.expense_daily_value = QLabel(self.expense_daily_frame)
        self.expense_daily_value.setObjectName(u"expense_daily_value")

        self.verticalLayout_29.addWidget(self.expense_daily_value)


        self.gridLayout_7.addWidget(self.expense_daily_frame, 0, 0, 1, 1)

        self.expense_weekly_frame = QFrame(self.totalExpense_frame)
        self.expense_weekly_frame.setObjectName(u"expense_weekly_frame")
        self.expense_weekly_frame.setFrameShape(QFrame.StyledPanel)
        self.expense_weekly_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.expense_weekly_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.expense_weekly = QLabel(self.expense_weekly_frame)
        self.expense_weekly.setObjectName(u"expense_weekly")
        self.expense_weekly.setFont(font4)

        self.verticalLayout_30.addWidget(self.expense_weekly)

        self.expense_weekly_value = QLabel(self.expense_weekly_frame)
        self.expense_weekly_value.setObjectName(u"expense_weekly_value")

        self.verticalLayout_30.addWidget(self.expense_weekly_value)


        self.gridLayout_7.addWidget(self.expense_weekly_frame, 0, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.totalExpense_frame)

        self.frame_10 = QFrame(self.expense_report_graph)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.expense_line = QWidget(self.frame_10)
        self.expense_line.setObjectName(u"expense_line")
        self.expense_line.setGeometry(QRect(10, 10, 441, 281))

        self.horizontalLayout_8.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"#incomeDownBtn,#expenseDownBtn,#budgetDownBtn {border :1px solid black;border-radius:10px}\n"
"#searchHistory_lineEdit,#historyList {border :1px solid black}\n"
"#incomeDownBtn{\n"
"background-color:#A7F0AE;\n"
"}\n"
"#expenseDownBtn{\n"
"background-color:#A7F0AE;\n"
"}\n"
"#budgetDownBtn{\n"
"background-color:#A7F0AE;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.page_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_13 = QFrame(self.page_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.searchHistory_lineEdit = QLineEdit(self.frame_15)
        self.searchHistory_lineEdit.setObjectName(u"searchHistory_lineEdit")
        self.searchHistory_lineEdit.setGeometry(QRect(20, 20, 221, 21))
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.searchHistory_lineEdit.sizePolicy().hasHeightForWidth())
        self.searchHistory_lineEdit.setSizePolicy(sizePolicy5)
        self.scrollArea_4 = QScrollArea(self.frame_15)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(0, 50, 921, 251))
        self.scrollArea_4.setStyleSheet(u"background-color:transparent;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 921, 251))
        self.scrollAreaWidgetContents_5.setStyleSheet(u"")
        self.verticalLayout_39 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.history_list = QWidget(self.scrollAreaWidgetContents_5)
        self.history_list.setObjectName(u"history_list")

        self.verticalLayout_39.addWidget(self.history_list)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_2.addWidget(self.frame_15, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.page_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.incomeDownBtn = QPushButton(self.frame_18)
        self.incomeDownBtn.setObjectName(u"incomeDownBtn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.incomeDownBtn.sizePolicy().hasHeightForWidth())
        self.incomeDownBtn.setSizePolicy(sizePolicy6)

        self.verticalLayout_15.addWidget(self.incomeDownBtn)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.frame_24 = QFrame(self.frame_17)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_24)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.expenseDownBtn = QPushButton(self.frame_24)
        self.expenseDownBtn.setObjectName(u"expenseDownBtn")
        sizePolicy6.setHeightForWidth(self.expenseDownBtn.sizePolicy().hasHeightForWidth())
        self.expenseDownBtn.setSizePolicy(sizePolicy6)

        self.verticalLayout_16.addWidget(self.expenseDownBtn)


        self.verticalLayout_14.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_17)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.budgetDownBtn = QPushButton(self.frame_23)
        self.budgetDownBtn.setObjectName(u"budgetDownBtn")
        sizePolicy6.setHeightForWidth(self.budgetDownBtn.sizePolicy().hasHeightForWidth())
        self.budgetDownBtn.setSizePolicy(sizePolicy6)

        self.verticalLayout_17.addWidget(self.budgetDownBtn)


        self.verticalLayout_14.addWidget(self.frame_23)


        self.verticalLayout_13.addWidget(self.frame_17)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"#upload_pic_btn {border :1px solid black;border-radius:10px}\n"
"#delete_acc_btn,#logout_btn,#save_setting_btn {border :1px solid black;}\n"
"#lineedit_confirm_new_password,#lineedit_current_password,#lineedit_new_password,#lineedit_new_name {border :1px solid black;}\n"
"#logout_btn{\n"
"background-color:#A7F0AE;\n"
"border-radius: 10px;\n"
"}\n"
"#save_setting_btn{\n"
"background-color:#68FF77;\n"
"border-radius: 10px;\n"
"}\n"
"#upload_pic_btn{\n"
"background-color:#A7F0AE;\n"
"border-radius:10px;\n"
"}\n"
"#delete_acc_btn{\n"
"background-color:#FF7C7C;\n"
"border-radius: 10px;\n"
"}")
        self.scrollArea_2 = QScrollArea(self.page_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 951, 661))
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 951, 661))
        self.new_pwd_lineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.new_pwd_lineEdit.setObjectName(u"new_pwd_lineEdit")
        self.new_pwd_lineEdit.setGeometry(QRect(50, 250, 271, 31))
        self.new_pwd_lineEdit.setStyleSheet(u"border: 1px solid black;")
        self.new_pwd_lineEdit.setInputMethodHints(Qt.ImhNone)
        self.new_pwd_confirm_lineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.new_pwd_confirm_lineEdit.setObjectName(u"new_pwd_confirm_lineEdit")
        self.new_pwd_confirm_lineEdit.setGeometry(QRect(50, 320, 271, 31))
        self.new_pwd_confirm_lineEdit.setStyleSheet(u"border: 1px solid black;")
        self.save_setting_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.save_setting_btn.setObjectName(u"save_setting_btn")
        self.save_setting_btn.setGeometry(QRect(420, 600, 101, 41))
        self.save_setting_btn.setAutoFillBackground(False)
        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 70, 191, 31))
        self.label_7.setFont(font3)
        self.logout_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(820, 600, 101, 41))
        self.delete_acc_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.delete_acc_btn.setObjectName(u"delete_acc_btn")
        self.delete_acc_btn.setGeometry(QRect(30, 600, 101, 41))
        self.new_pic_label = QLabel(self.scrollAreaWidgetContents_2)
        self.new_pic_label.setObjectName(u"new_pic_label")
        self.new_pic_label.setGeometry(QRect(590, 110, 200, 200))
        self.new_pic_label.setMinimumSize(QSize(200, 200))
        self.new_pic_label.setMaximumSize(QSize(200, 200))
        self.new_pic_label.setStyleSheet(u"border: 1px solid black;")
        self.new_pic_label.setScaledContents(True)
        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(580, 60, 231, 41))
        self.label_9.setFont(font3)
        self.upload_pic_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.upload_pic_btn.setObjectName(u"upload_pic_btn")
        self.upload_pic_btn.setGeometry(QRect(630, 320, 111, 41))
        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 190, 181, 31))
        self.label_8.setFont(font3)
        self.lineedit_new_name = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineedit_new_name.setObjectName(u"lineedit_new_name")
        self.lineedit_new_name.setGeometry(QRect(50, 130, 271, 31))
        self.setting_warning_label = QLabel(self.scrollAreaWidgetContents_2)
        self.setting_warning_label.setObjectName(u"setting_warning_label")
        self.setting_warning_label.setGeometry(QRect(330, 330, 241, 16))
        self.setting_warning_label.setStyleSheet(u"color: red;")
        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 110, 111, 16))
        self.label.setStyleSheet(u"color: black;")
        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 230, 111, 16))
        self.label_2.setStyleSheet(u"color: black;")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 300, 141, 16))
        self.label_3.setStyleSheet(u"color: black;")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.setting_btn.setText("")
        self.profileImg_label.setText("")
        self.Overview_btn.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.Budget_btn.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.Income_btn.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.Expense_btn.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.Analysis_btn.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.MenuButton.setText("")
        self.tab_level.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All-Time", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Daily", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Weekly", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.comboBox.setItemText(5, "")

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  Budget", None))
        self.add_Budget.setText(QCoreApplication.translate("MainWindow", u"Create a new Budget", None))
        self.income_yearly.setText(QCoreApplication.translate("MainWindow", u"Total income yearly:", None))
        self.income_yearly_value.setText(QCoreApplication.translate("MainWindow", u"416541343", None))
        self.income_monthly.setText(QCoreApplication.translate("MainWindow", u"Total income monthly:", None))
        self.income_monthly_value.setText(QCoreApplication.translate("MainWindow", u"6545473654", None))
        self.income_daily.setText(QCoreApplication.translate("MainWindow", u"Total income daily:", None))
        self.income_daily_value.setText(QCoreApplication.translate("MainWindow", u"13212312313", None))
        self.income_weekly.setText(QCoreApplication.translate("MainWindow", u"Total income weekly:", None))
        self.income_weekly_value.setText(QCoreApplication.translate("MainWindow", u"13215431", None))
        self.income_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter income", None))
        self.income_list_header.setText(QCoreApplication.translate("MainWindow", u"income list", None))
        self.add_income_button.setText("")
        self.expense_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter expense", None))
        self.expense_list_header.setText(QCoreApplication.translate("MainWindow", u"expense list", None))
        self.add_expense_button.setText("")
        self.expense_yearly.setText(QCoreApplication.translate("MainWindow", u"Total expense yearly:", None))
        self.expense_yearly_value.setText(QCoreApplication.translate("MainWindow", u"416541343", None))
        self.expense_monthly.setText(QCoreApplication.translate("MainWindow", u"Total expense monthly:", None))
        self.expense_monthly_value.setText(QCoreApplication.translate("MainWindow", u"6545473654", None))
        self.expense_daily.setText(QCoreApplication.translate("MainWindow", u"Total expense daily:", None))
        self.expense_daily_value.setText(QCoreApplication.translate("MainWindow", u"13212312313", None))
        self.expense_weekly.setText(QCoreApplication.translate("MainWindow", u"Total expense weekly:", None))
        self.expense_weekly_value.setText(QCoreApplication.translate("MainWindow", u"13215431", None))
        self.searchHistory_lineEdit.setInputMask("")
        self.searchHistory_lineEdit.setText("")
        self.searchHistory_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter history", None))
        self.incomeDownBtn.setText(QCoreApplication.translate("MainWindow", u"Download Income History", None))
        self.expenseDownBtn.setText(QCoreApplication.translate("MainWindow", u"Download Expense History", None))
        self.budgetDownBtn.setText(QCoreApplication.translate("MainWindow", u"Download Budget History", None))
        self.new_pwd_lineEdit.setText("")
        self.new_pwd_lineEdit.setPlaceholderText("")
        self.new_pwd_confirm_lineEdit.setText("")
        self.new_pwd_confirm_lineEdit.setPlaceholderText("")
        self.save_setting_btn.setText(QCoreApplication.translate("MainWindow", u"Save setting", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Change Username", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.delete_acc_btn.setText(QCoreApplication.translate("MainWindow", u"Delete account", None))
        self.new_pic_label.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Change profile picture", None))
        self.upload_pic_btn.setText(QCoreApplication.translate("MainWindow", u"Upload picture", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Change password", None))
        self.lineedit_new_name.setInputMask("")
        self.lineedit_new_name.setPlaceholderText("")
        self.setting_warning_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"New Username", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
    # retranslateUi

