from ..app.account import AccountSystem
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class SettingUI:
    def __init__(self, ui, s: AccountSystem, parent):
        self.ui = ui
        self.parent = parent
        self.account_system = s
        #self.ui.logout_btn.clicked.connect(self.close)
        #print(self.ui.logout_btn)
        self.ui.logout_btn.clicked.connect(self.close1)
        self.ui.delete_acc_btn.clicked.connect(self.delete_account)
        self.ui.save_setting_btn.clicked.connect(self.save_setting)

    def delete_account(self):
        print("delte")

    def save_setting(self):
        print("save setting")

    def close1(self):
        print("Plz close")
        self.parent.logout()



