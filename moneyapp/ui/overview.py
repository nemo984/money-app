from typing import List
from ..app.helpers import Observer
from ..app.model import *


class ReminderUI(Observer):
    async def update(self, reminders: List[Reminder]):
        pass


class IncomeReportUI(Observer):
    async def update(self, incomes: List[Income]):
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
