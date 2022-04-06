from ..app.helpers import Observer
from ..app.model import *
from typing import List

class IncomeReportUI(Observer):
    def update(self, incomes: List[Income]):
        print("Incomes updated: Updating incomes' report")
        for income in incomes:
            print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")
        print("================")