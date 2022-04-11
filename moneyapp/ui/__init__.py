from ..app.budget_system import BudgetSystem
from ..app.income_system import IncomeSystem
from ..app.expense_system import ExpenseSystem
from .budget import BudgetUI
from .income import IncomeUI
from .expense import ExpenseUI

class MoneyAppUI:
    def __init__(
        self,
        income_system: IncomeSystem,
        budget_system: BudgetSystem,
        expense_system: ExpenseSystem,
    ):
        budget_ui = BudgetUI(budget_system)
        income_ui = IncomeUI(income_system)
        expense_ui = ExpenseUI(expense_system)
        
        budget_system.add_observer(budget_ui)
        income_system.add_observer(income_ui)
        expense_system.add_observer(expense_ui)
