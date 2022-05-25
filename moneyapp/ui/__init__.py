from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from ..app.budget_system import BudgetSystem
from ..app.income_system import IncomeSystem
from ..app.expense_system import ExpenseSystem
from ..app.account import AccountSystem
from .budget import BudgetUI
from .income import IncomeUI
from .expense import ExpenseUI
from .uipy.Mono import Ui_MainWindow
import os

class MoneyAppUI(QMainWindow):
    def __init__(
        self,
        account_id: int,
        income_system: IncomeSystem,
        budget_system: BudgetSystem,
        expense_system: ExpenseSystem,
        parent = None
    ):
        super(MoneyAppUI, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        budget_ui = BudgetUI(self.ui, budget_system, self)
        income_ui = IncomeUI(1, income_system)
        expense_ui = ExpenseUI(expense_system)
        
        budget_system.add_observer(budget_ui)
        income_system.add_observer(income_ui)
        expense_system.add_observer(expense_ui)

        account = AccountSystem().getByID(account_id)
        self.ui.name_label.setText(account.name)
        qimg = QImage.fromData(account.profile_image)
        pixmap = QPixmap.fromImage(qimg)
        self.ui.profileImg_label.setPixmap(pixmap)

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


    def switch_tab(self):
        tabs = {"Overview":0, "Budget":1, "Income":2, "Expense":3, "Analysis":4}
        self.prev_tab.setStyleSheet("background-color: transparent")
        text = self.sender().text()
        self.ui.stackedWidget.setCurrentIndex(tabs[text])
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


