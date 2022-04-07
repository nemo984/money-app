from typing import List
from ..app.helpers import Observer
from ..app.model import *


class BudgetUI(Observer):
    async def update(self, budgets: List[Budget]):
        pass
