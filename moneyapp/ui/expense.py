from ..app.helpers import Observer
from ..app.model import *
from typing import List

class ExpenseUI(Observer):
    async def update(self, incomes: List[Expense]):
        pass