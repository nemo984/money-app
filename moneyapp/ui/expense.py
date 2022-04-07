from typing import List
from ..app.helpers import Observer
from ..app.model import *


class ExpenseUI(Observer):
    async def update(self, incomes: List[Expense]):
        pass
