from typing import List
from ..app.helpers import Observer
from ..app.model import *
from .uipy.overview_wid import Ui_Form
from ..app.expense_system import ExpenseSystem
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
    def __init__(self,ui,s: ExpenseSystem):
        self.ui = ui
        self.lay = self.ui.verticalLayout_18
        self.expense_system = s
        self.expenses = []
        self.category = ["Food", "Entertainment", "Transport", "Education", "Healthcare", "Bill", "Saving", "Investment", "Shopping","Utilities/Other"]


    async def update(self, expenses: List[Expense]):
        self.clear_layout()
        b = self.expense_system.get_categories_total()
        for expense in expenses:
            amount = b[expense.category] if expense.category in b else 0
            expense = ExpenseReport( expense_id=expense.id ,lay = self.lay , category = expense.category,
                                amount=amount, expense_system = self.expense_system)
            expense.add() 
            self.expenses.append(expense)

    def clear_layout(self):
        for expense in self.expenses:
            expense.clear()
        self.expenses = []

class ExpenseReport(QWidget):
    def __init__(self,expense_id, lay: QVBoxLayout, category, amount, expense_system):
        super(ExpenseReport, self).__init__()
        self.id = expense_id
        self.layout = lay
        self.wid = Ui_Form()
        self.expense_system = expense_system
        self.amount = amount
        self.category = category
        self.wid.setupUi(self)
        self.wid.category_label.setText(category)
        self.wid.amount_label.setText("฿{:,.2f}".format(amount))          
        

    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()

    def add(self):
        self.layout.insertWidget(0,self)

