from typing import List
from ..app.helpers import Observer
from ..app.model import *
from .uipy.overview_wid import Ui_Form
from ..app.expense_system import ExpenseSystem
from ..app.reminder import ReminderSystem
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class ReminderUI(Observer):
    def __init__(self,ui,r: ReminderSystem):
        self.ui = ui
        self.lay = self.ui.verticalLayout_42
        self.riminder_system = r
        self.reminders = []
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
        self.lay = self.ui.verticalLayout_42
        self.expense_system = s
        self.expenses = []
        self.category = {"Food":u":/category/icon/category/Food.svg", 
                        "Entertainment":u":/category/icon/category/Entertainment.svg", 
                        "Transport":u":/category/icon/category/Transport.svg", 
                        "Education":u":/category/icon/category/Education.svg", 
                        "Healthcare":u":/category/icon/category/healthcare.svg", 
                        "Bill":u":/category/icon/category/bill.svg",
                        "Saving":u":/category/icon/category/Saving.svg", 
                        "Investment":u":/category/icon/category/Investment.svg", 
                        "Shopping":u":/category/icon/category/shopping-.svg",
                        "Utilities/Other":u":/category/icon/category/other.svg"}
        
    async def update(self, expenses: List[Expense]):
        self.clear_layout()
        b = self.expense_system.get_categories_total()
        for category, icon_path in self.category.items():
            amount = b[category] if category in b else 0
            expense = ExpenseReport(lay = self.lay , category = category, icon_path=icon_path,
                                amount=amount, expense_system = self.expense_system)
            expense.add() 
            self.expenses.append(expense)

    def clear_layout(self):
        for expense in self.expenses:
            expense.clear()
        self.expenses = []

class ExpenseReport(QWidget):
    def __init__(self, lay: QVBoxLayout, icon_path, category, amount, expense_system):
        super(ExpenseReport, self).__init__()
        self.layout = lay
        self.wid = Ui_Form()
        self.expense_system = expense_system
        self.amount = amount
        self.category = category
        self.wid.setupUi(self)
        self.wid.category_label.setText(category)
        self.wid.icon_label.setPixmap(QPixmap(icon_path))
        self.wid.amount_label.setText("฿{:,.2f}".format(amount))          
        

    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()

    def add(self):
        self.layout.insertWidget(0,self)

