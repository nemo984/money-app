from typing import Optional, List
from .helpers import Observable
from .model import Income, Account
from datetime import datetime, timedelta

class IncomeSystem(Observable):
    def __init__(self, owner, history_system):
        super().__init__()
        self.owner = owner
        self._incomes = []
        self.history_system = history_system

    def add(
        self,
        name: str,
        category: str,
        amount: float,
        date,
        note: Optional[str] = None,
        recurrence: Optional[str] = None,
    ) -> Income:
        income = Income(owner=self.owner, name=name, category=category, date=date,
                        amount=amount, note=note,
                        recurrence=recurrence)
        income.save()
        self._incomes.append(income)
        self.notify(self._incomes)
        self.history_system.add_create("Income", f"You created an income named '{name}'", 
        f"You created an income named '{name}', category = {category}, amount= {amount}, recurrence = {recurrence}")
        return income

    def get(self) -> List[Income]:
        self._incomes = list(self.owner.incomes_ordered)
        self.notify(self._incomes)
        return self._incomes

    def getByID(self, income_id) -> Income:
        income = Income.get_or_none(Income.id == income_id)
        return income

    def filter(self, query: str):
        if query == "":
            return self.get()

        filtered_incomes = []
        for income in self._incomes:
            currency = "฿{:,.2f}".format(income.amount)
            s = f"{income.date}{income.name}{income.category}{currency}{income.recurrence}"
            if query in s:
                filtered_incomes.append(income)
        self.notify(filtered_incomes)
        return filtered_incomes

    def get_incomes_total(self) -> dict:
        results = {"daily": 0, "weekly": 0, "monthly": 0, "yearly": 0}
        multiplier = {"daily": (1, 7, 30, 365), "weekly": (1/7, 1, 30/7, 365/7), "monthly": (1/30, 7/30, 1, 365/30 ), 
                      "yearly": (1/365, 7/365, 30/365, 1)}
        for income in self._incomes:
            recurrence = income.recurrence
            if recurrence in results:
                times = multiplier[recurrence]
                for i, recc in enumerate(multiplier.keys()):
                    results[recc] += float(income.amount) * times[i] 
        return results

    def get_categories_total(self):
        categories = {"Full-time": 0, "Part-time": 0, "Passive": 0, "Other": 0}
        recurrence_multiplier = {"daily": 30, "weekly": 4, "monthly": 1, "yearly": 30/365}
        for income in self._incomes:
            amount = 0 
            if income.recurrence in recurrence_multiplier:
                categories[income.category] += float(income.amount) * recurrence_multiplier[income.recurrence]
        return categories

    def update(
        self,
        income_id: int,
        name: Optional[str] = None,
        category: Optional[str] = None,
        amount: Optional[float] = None,
        recurrence: Optional[str] = None,
        note: Optional[str] = None,
    ) -> Income:
        income = self.getByID(income_id)
        change_str = ""
        if income is None:
            return
        if name:
            change_str += f"You change the name from '{income.name}' to '{name}'. "
            income.name = name
        if category:
            change_str += f"You change the category from '{income.category}' to '{category}'. "
            income.category = category
        if amount:
            change_str += f"You change the amount from '{income.amount}' to '{amount}'. "
            income.amount = amount
        if recurrence:
            change_str += f"You change the recurrence from '{income.recurrence}' to '{recurrence}'. "
            income.recurrence = recurrence
        if note:
            change_str += f"You change the note from '{income.note}' to '{note}'. "
            income.note = note
        income.save()
        self.get()
        self.history_system.add_update("Income", f"You updated the income named '{income.name}'", 
        f"You updated the income named '{income.name}'. " + change_str)
        return income

    def delete(self, income_id):
        income = self.getByID(income_id)
        if income is None:
            return
        self.history_system.add_delete("Income",  f"You deleted the income named '{income.name}'", 
        f"You deleted the income named '{income.name}' that have category={income.category}, amount={income.amount}, recurrence={income.recurrence}")
        income.delete_instance()
        self.get()
