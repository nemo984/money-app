from typing import Optional, List
from .helpers import Observable
from .model import Income, Account 

class IncomeSystem(Observable):
    def __init__(self, owner):
        super().__init__()
        self.owner = owner
        self._incomes = []

    def add(
        self,
        name: str,
        category: str,
        amount: float,
        date,
        note: Optional[str] = None,
        frequency: Optional[int] = None,
    ) -> Income:
        income = Income(owner=self.owner, name=name, category=category, date=date,
                        amount=amount, note=note,
                        frequency_day=frequency)
        income.save()
        self._incomes.append(income)
        self.notify(self._incomes)
        return income

    def get(self) -> List[Income]:
        self._incomes = list(self.owner.incomes_ordered)
        self.notify(self._incomes)
        return self._incomes
        
    def getByID(self, income_id) -> Income:
        income = Income.get_or_none(Income.id == income_id)
        return income


    def update(
        self,
        income_id: int,
        name: Optional[str] = None,
        category: Optional[str] = None,
        amount: Optional[float] = None,
        frequency: Optional[int] = None,
        note: Optional[str] = None,
    ) -> Income:
        income = self.getByID(income_id)
        if income is None:
            return
        if name:
            income.name = name
        if category:
            income.category = category
        if amount:
            income.amount = amount
        if frequency:
            income.frequency_day = frequency
        if note:
            income.note = note

        income.save()
        self.get()
        return income

    def delete(self, income_id):
        income = self.getByID(income_id)
        if income is None:
            return
        income.delete_instance()
        self.get()
