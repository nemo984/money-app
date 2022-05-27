import pickle
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ..app.budget_system import BudgetSystem
from ..app.income_system import IncomeSystem
from ..app.expense_system import ExpenseSystem
from ..app.account import AccountSystem
from ..app.history import HistorySystem
from ..app.reminder import ReminderSystem
from .budget import BudgetUI
from .income import IncomeUI
from .expense import ExpenseUI
from .history import HistoryUI
from .setting import SettingUI
from .overview import ExpenseReportUI
from .uipy.Mono import Ui_MainWindow
from PySide6.QtCore import *
import os
from datetime import datetime, timedelta

class MoneyAppUI(QMainWindow):
    def __init__(
        self,
        account,
        income_system: IncomeSystem,
        budget_system: BudgetSystem,
        expense_system: ExpenseSystem,
        history_system: HistorySystem,
        account_system: AccountSystem,
        reminder_system: ReminderSystem,
        parent = None
    ):
        super(MoneyAppUI, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Money App")
        self.account = account
        self.account_system = account_system

        self.ui.name_label.setText(account.name)
        qimg = QImage.fromData(account.profile_image)
        pixmap = QPixmap.fromImage(qimg)
        self.ui.profileImg_label.setPixmap(pixmap)

        budget_ui = BudgetUI(self.ui, account, budget_system, history_system,reminder_system, self)
        income_ui = IncomeUI(self.ui, income_system, history_system, self)
        expense_ui = ExpenseUI(self.ui,expense_system, budget_system, history_system, self)
        history_ui = HistoryUI(self.ui,history_system, self)
        setting_ui = SettingUI(self.ui, account_system, self)
        expense_report_ui = ExpenseReportUI(self.ui, expense_system)

        budget_system.add_observer(budget_ui)
        income_system.add_observer(income_ui)
        expense_system.add_observer(expense_ui)
        expense_system.add_observer(expense_report_ui)
        history_system.add_observer(history_ui)

        history_system.get()
        budget_system.get()
        expense_system.get()
        income_system.get()
        reminder_system.get()

        dic = expense_system.get_categories_total()
        print(dic)

        self.ui.Overview_btn.clicked.connect(self.switch_tab)
        self.ui.Overview_btn.setStyleSheet("""
        QPushButton {
            background-color: #2B5DD1;
            color: #FFFFFF;
            border-style: outset;
            padding: 2px;
            font: bold 20px;
            border-width: 6px;
            border-radius: 10px;
            border-color: #2752B8;
        }
        QPushButton:hover {
            background-color: lightgreen;
        }
        """)
        self.ui.Expense_btn.clicked.connect(self.switch_tab)
        self.ui.Income_btn.clicked.connect(self.switch_tab)
        self.ui.Analysis_btn.clicked.connect(self.switch_tab)
        self.ui.Budget_btn.clicked.connect(self.switch_tab)
        self.ui.logout_btn.clicked.connect(self.logout)
        self.ui.save_setting_btn.clicked.connect(self.save_setting)
        self.ui.delete_acc_btn.clicked.connect(self.delete_account)
        self.prev_tab = self.ui.Overview_btn

        self.ui.setting_btn.clicked.connect(self.setting)

    def logout(self):
        save_staySignIn()
        self.close()
        self.parent.show()

    def setting(self):
        self.prev_tab.setStyleSheet("background-color: transparent")
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.tab_level.setText("Setting")
        self.prev_tab = self.sender()

    def switch_tab(self):
        tabs = {"Overview": 0, "Budget": 1,
                "Income": 2, "Expense": 3, "Analysis": 4}
        self.prev_tab.setStyleSheet("background-color: transparent")
        text = self.sender().text()
        if text in tabs:
            self.ui.stackedWidget.setCurrentIndex(tabs[text])
        else:
            self.ui.stackedWidget.setCurrentIndex(5)

        self.ui.tab_level.setText(text)
        self.sender().setStyleSheet("""
        QPushButton {
            background-color: #2B5DD1;
            color: #FFFFFF;
            border-style: outset;
            padding: 2px;
            font: bold 20px;
            border-width: 6px;
            border-radius: 10px;
            border-color: #2752B8;
        }
        QPushButton:hover {
            background-color: lightgreen;
        }
        """)
        self.prev_tab = self.sender()

    def closeEvent(self, event):
        if self.parent:
            self.parent.close()
    
    def delete_account(self):
        self.account_system.delete(self.account)
        self.logout()

    def save_setting(self):
        print("saving")
        name = self.ui.lineedit_new_name.text()
        new_password = self.ui.new_pwd_lineEdit.text()
        new_password_confirm = self.ui.new_pwd_confirm_lineEdit.text()
        if (new_password != "" or new_password_confirm != "") and new_password != new_password_confirm:
            self.ui.setting_warning_label.setText("Password does not match")
            return

        self.account_system.update(account=self.account, name=name, password=new_password)
        self.ui.setting_warning_label.setText("")
        if name != "":
            self.ui.name_label.setText(name)
            self.ui.lineedit_new_name.setText("")
        if new_password != "":
            self.ui.new_pwd_lineEdit.setText("")
            self.ui.new_pwd_confirm_lineEdit.setText("")



_staySignInChecked = "staySignInChecked"
_account_id = "account_id"
_last_tab = "last_tab"

def load_id():
    try:
        with open('signin.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        save_staySignIn()
        return {_staySignInChecked:False, _account_id:-1, _last_tab: -1}

def save_staySignIn(staySignInChecked: bool = False, account_id: int = -1, last_tab: int = -1):
    staySignInChecked = load_id(
    )[0] if staySignInChecked is None else staySignInChecked
    with open('signin.pickle', 'wb') as fobj:
        d = {_staySignInChecked: staySignInChecked,
             _account_id: account_id, _last_tab: last_tab}
        pickle.dump(d, fobj)