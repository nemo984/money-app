from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from ..app.budget_system import BudgetSystem
from ..app.income_system import IncomeSystem
from ..app.expense_system import ExpenseSystem
from .budget import BudgetUI
from .income import IncomeUI
from .expense import ExpenseUI
from .uipy.Mono import Ui_MainWindow

class MoneyAppUI:
    def __init__(
        self,
        main_window,
        income_system: IncomeSystem,
        budget_system: BudgetSystem,
        expense_system: ExpenseSystem,
    ):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(main_window)
        budget_ui = BudgetUI(budget_system)
        income_ui = IncomeUI(1, income_system)
        expense_ui = ExpenseUI(expense_system)
        
        budget_system.add_observer(budget_ui)
        income_system.add_observer(income_ui)
        expense_system.add_observer(expense_ui)



