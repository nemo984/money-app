from ..app.helpers import Observer
from ..app.model import *
from typing import List

class BudgetUI(Observer):
    async def update(self, budgets: List[Budget]):
        pass