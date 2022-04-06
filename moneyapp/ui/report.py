from ..app.helpers import Observer
from ..app.model import *
from typing import List
import asyncio

class IncomeReportUI(Observer):
    async def update(self, incomes: List[Income]):
        await asyncio.sleep(3)

        print("Incomes updated: Updating incomes' report")
        for income in incomes:
            print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")
        print("================")

class BudgetReportUI(Observer):
    async def update(self, budgets: List[Budget]):
        pass

class ExpenseReportUI(Observer):
    async def update(self, expenses: List[Expense]):
        pass