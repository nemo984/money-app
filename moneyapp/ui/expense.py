from typing import List
from ..app.helpers import Observer
from ..app.model import Expense
from ..app.expense_system import ExpenseSystem


class ExpenseUI(Observer):

    def __init__(self, s: ExpenseSystem):
        self.ui = 0 
        self.system = s

    async def update(self, incomes: List[Expense]):
        pass
