from PySide6 import QtWidgets
from .app.budget_system import BudgetSystem
from .app.income_system import IncomeSystem
from .app.expense_system import ExpenseSystem
from .ui import MoneyAppUI


class MainApp:
    def __init__(self):
        self.income_system = IncomeSystem()
        self.budget_system = BudgetSystem()
        self.expense_system = ExpenseSystem()
        self.ui = MoneyAppUI(self.income_system, self.budget_system, self.expense_system)
        
    def show(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui.setupUi(self.window)
        self.window.show()