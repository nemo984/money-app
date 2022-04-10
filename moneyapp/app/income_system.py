from typing import Optional, List
from .helpers import Observable
from .model import *


class IncomeSystem(Observable):
    def __init__(self):
        super().__init__()
        self._incomes = []

    def add(
        self,
        owner: Account,
        category: IncomeCategory,
        amount: float,
        note: Optional[str] = None,
        frequency: Optional[int] = None,
    ) -> Income:
        income = Income(owner=owner, category=category,
                        amount=amount, note=note,
                        frequency_day=frequency)
        income.save()
        self._incomes.append(income)
        print("Incomes updated: Notifying observers")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
        self.notify(self._incomes)
        return income

    def get(self, account: Account) -> List[Income]:
        self._incomes = list(account.incomes_ordered)
        self.notify(self._incomes)
        return self._incomes

    def update(
        self,
        income: Income,
        category: Optional[IncomeCategory] = None,
        amount: Optional[float] = None,
        frequency: Optional[int] = None,
        note: Optional[str] = None,
    ) -> Income:

        if category:
            income.category = category
        if amount:
            income.amount = amount
        if frequency:
            income.frequency_day = frequency
        if note:
            income.note = note

        income.save()
        self.get(income.owner)
        return income

    def delete(self, income: Income):
        owner = income.owner
        income.delete_instance()
        self.get(owner)
