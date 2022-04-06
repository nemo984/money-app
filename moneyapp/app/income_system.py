from .helpers import Observable
from .model import *

class IncomeSystem(Observable):
    def __init__(self):
        super().__init__()
        self._incomes = []

    def add(self, income : Income):
        income.save()
        self._incomes.append(income)
        self.notify()
