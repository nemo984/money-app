from typing import List
from ..app.helpers import Observer
from ..app.model import Budget
from ..app.budget_system import BudgetSystem


class BudgetUI(Observer):
    
    def __init__(self, s: BudgetSystem):
        self.ui = 0 
        self.system = s

    async def update(self, budgets: List[Budget]):
        pass
