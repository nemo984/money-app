from typing import List
from ..app.helpers import Observer
from ..app.model import *


class IncomeUI(Observer):
    async def update(self, incomes: List[Income]):
        print("Incomes updated: Updating income page UI")
        for income in incomes:
            print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")
        print("================")
