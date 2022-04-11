from typing import List
from ..app.helpers import Observer
from ..app.model import Income
from ..app.income_system import IncomeSystem


class IncomeUI(Observer):
    
    def __init__(self, s: IncomeSystem):
        self.ui = 0
        self.system = s

    async def update(self, incomes: List[Income]):
        print("Incomes updated: Updating income page UI")
        for income in incomes:
            print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")
        print("================")
