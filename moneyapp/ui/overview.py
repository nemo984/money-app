from typing import List
from ..app.helpers import Observer
from ..app.model import *
from .uipy.overview_wid import Ui_Form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

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
    def __init__(self,ui,):
        self.ui = ui
        self.lay = self.ui.verticalLayout_18
        self.expenses = []

    async def update(self, expenses: List[Expense]):
        self.clear_layout()
        for expense in expenses:
            expense = ExpenseReport( expense_id=expense.id ,lay = self.lay , category = expense.category,
                                amount = expense.amount)
            expense.add()
            self.expenses.append(expense)

expense_category_dropdown = {"Food":0, "Entertainment":1, "Transport":2, "Education":3, "Healthcare":4, "Bill":5, "Saving":6, "Investment":7, "Shopping":8, "Utilities/Other":9}

class ExpenseReport(QWidget):
    def __init__(self,expense_id, lay: QVBoxLayout, category, amount):
        super(ExpenseReport, self).__init__()
        self.id = expense_id
        self.layout = lay
        self.wid = Ui_Form()
        self.amount = amount
        self.category = category

        self.wid.setupUi(self)
        self.wid.amount_label.setText(str(self.amount))
        self.wid.category_label.setText(category)



    def add(self):
        self.layout.insertWidget(0, self)

