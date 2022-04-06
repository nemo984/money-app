from .helpers import Observable
from .model import *
from typing import Optional

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
    ):
        income = Income(owner=owner, category=category, 
                        amount=amount, note=note, 
                        frequency_day=frequency)
        income.save()
        self._incomes.append(income)
        print("Incomes updated: Notifying observers")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
        self.notify(self._incomes)


    def get():
        pass

    def update():
        pass

    def delete():
        pass
