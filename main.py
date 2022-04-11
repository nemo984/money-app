import moneyapp
from moneyapp.ui.Mono_ui import *

# app = moneyapp.MainApp()

import sys
import os


class MainWindow(QMainWindow):

    def init(self, parent=None):
        QMainWindow.init(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Overview_btn.clicked.connect(self.overview_click)
        self.ui.MenuButton.clicked.connect(self.Menuclick)
        self.Menu_Open = True

        self.show()

    def overview_click(self):
        print("Overview")
        self.ui.Overview_btn.setStyleSheet(
            "background-color : yellow;border-radius: 7px")
        self.ui.Overview_btn.setMinimumHeight(100)

    def Menuclick(self):
        self.Menu_Open = not self.Menu_Open
        if(self.MenuOpen):
            self.ui.leftMenu.setMinimumWidth(320)
            self.ui.leftMenu.setMaximumWidth(320)
        else:
            self.ui.leftMenu.setMinimumWidth(0)
            self.ui.leftMenu.setMaximumWidth(0)


if __name__ == "main":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
