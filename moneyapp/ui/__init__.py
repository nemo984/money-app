import pickle
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ..app.budget_system import BudgetSystem
from ..app.income_system import IncomeSystem
from ..app.expense_system import ExpenseSystem
from ..app.account import AccountSystem
from ..app.history import HistorySystem
from .budget import BudgetUI
from .income import IncomeUI
from .expense import ExpenseUI
from .history import HistoryUI
from .setting import SettingUI
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
        parent = None
    ):
        super(MoneyAppUI, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.name_label.setText(account.name)
        qimg = QImage.fromData(account.profile_image)
        pixmap = QPixmap.fromImage(qimg)
        self.ui.profileImg_label.setPixmap(pixmap)

        budget_ui = BudgetUI(self.ui, account, budget_system, history_system, self)
        income_ui = IncomeUI(self.ui, income_system, history_system, self)
        expense_ui = ExpenseUI(self.ui,expense_system, budget_system, history_system, self)
        history_ui = HistoryUI(self.ui,history_system, self)
        setting_ui = SettingUI(self.ui, account_system, self)
        
        budget_system.add_observer(budget_ui)
        income_system.add_observer(income_ui)
        expense_system.add_observer(expense_ui)
        history_system.add_observer(history_ui)

        history_system.get()
        budget_system.get()
        expense_system.get()
        income_system.get()

        now = datetime.today()
        print( now+ timedelta(days=20))
        dic = expense_system.get_categories_total(now - timedelta(days=20), now+ timedelta(days=20))
        for d in dic:
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