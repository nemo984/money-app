import re
from typing import List
from ..app.helpers import Observer
from ..app.model import *
from .uipy.overview_wid import Ui_Form
from .uipy.notification_wid import Ui_Form as Ui_Reminder
from ..app.expense_system import ExpenseSystem
from ..app.reminder import ReminderSystem
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtCharts import *


class ReminderUI(Observer):
    def __init__(self, ui, r: ReminderSystem):
        self.ui = ui
        self.lay = self.ui.verticalLayout_43
        self.reminder_system = r
        self.reminders = []

    async def update(self, reminders: List[Reminder]):
        self.clear_layout()
        for reminder in reminders:
            reminder = ReminderReport(reminder_id=reminder.id, lay=self.lay,reminder_system=self.reminder_system, date=reminder.created_date, 
                                    heading=reminder.heading, description=reminder.message)
            reminder.add()
            self.reminders.append(reminder)

    def clear_layout(self):
        for reminder in self.reminders:
            reminder.clear()
        self.reminders = []

class ReminderReport(QWidget):
    def __init__(self, reminder_id, lay: QVBoxLayout, reminder_system, date, heading, description):
        super(ReminderReport, self).__init__()
        self.id = reminder_id
        self.layout = lay
        self.date = date
        self.heading = heading
        self.description = description
        self.wid = Ui_Reminder()
        self.reminder_system = reminder_system
        self.wid.setupUi(self)
        self.wid.date_label.setText(str(date))
        self.wid.action_label.setText(heading)
        self.wid.description_label.setText(description)
        self.wid.option_btn.clicked.connect(self.option)

    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()

    def add(self):
        self.layout.insertWidget(0, self)

    def option(self):
        menu = QMenu()
        self.delete_action = QAction('Delete', self)
        self.delete_action.setData('Delete')
        self.delete_action.triggered.connect(self.delete)
        menu.addAction(self.delete_action)
        menu.exec(QCursor.pos())

    def delete(self):
        self.reminder_system.delete(self.id)
        self.clear()

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
    def __init__(self, ui, s: ExpenseSystem):
        self.ui = ui
        self.lay = self.ui.verticalLayout_42
        self.expense_system = s
        self.expenses = []
        self.category = [("Food", ":/category/icon/category/Food.svg"),
                         ("Entertainment", ":/category/icon/category/Entertainment.svg"),
                         ("Transport", ":/category/icon/category/Transport.svg"),
                         ("Education", ":/category/icon/category/Education.svg"),
                         ("Healthcare", ":/category/icon/category/healthcare.svg"),
                         ("Bill", ":/category/icon/category/bill.svg"),
                         ("Saving", ":/category/icon/category/Saving.svg"),
                         ("Investment", ":/category/icon/category/Investment.svg"),
                         ("Shopping", ":/category/icon/category/shopping-.svg"),
                         ("Utilities/Other", ":/category/icon/category/other.svg")]


    async def update(self, expenses: List[Expense]):
        self.clear_layout()
        b = self.expense_system.get_categories_total()
        i = 0
        while i < len(self.category):
            expenses_categories = []
            for j in range(3):
                if i >= len(self.category):
                    break
                category = self.category[i][0]
                amount = b[category] if category in b else 0
                expenses_categories.append((category, self.category[i][1], amount))
                i += 1
            
            expense = ExpenseReport(lay=self.lay, expense_system=self.expense_system, expense_categories=expenses_categories)
            expense.add()
            self.expenses.append(expense)

    def clear_layout(self):
        for expense in self.expenses:
            expense.clear()
        self.expenses = []

class DonutChartUI(Observer):
    def __init__(self, ui, expense_system, income_system):
        self.ui = ui
        self.expense_system = expense_system
        self.income_system = income_system
        self.ui.categories_total_comboBox.currentTextChanged.connect(self.change_chart)
        self.currentText = "Expense"
        self.series = QPieSeries()
        self.series.setHoleSize(0.35)

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
 
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Expense Example")
 
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
 
        self.ui.pie_widdget.setContentsMargins(0, 0, 0, 0)
        lay = QHBoxLayout(self.ui.pie_widdget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.chartview)

    async def update(self, _):
        self.change_chart(self.currentText)

    def change_chart(self, text):
        self.currentText = text
        if self.currentText == "Expense":
            expenses_categories = self.expense_system.get_categories_total()
            self.expenses_donut_chart(expenses_categories)
        else:
            incomes_categories = self.income_system.get_incomes_total()
            self.incomes_donut_chart(incomes_categories)

    def expenses_donut_chart(self, expenses):
        self.series.clear()
        for category, value in expenses.items():
            self.series.append(category, value)

    def incomes_donut_chart(self, incomes):
        self.series.clear()
        for category, value in incomes.items():
            self.series.append(category, value)
 

class ExpenseReport(QWidget):
    # (category, amount, icon_path)
    def __init__(self, lay: QVBoxLayout, expense_system, expense_categories):
        super(ExpenseReport, self).__init__()
        self.layout = lay
        self.wid = Ui_Form()
        self.expense_system = expense_system
        self.wid.setupUi(self)
        self.wid.category_label.setText(expense_categories[0][0])
        self.wid.icon_label.setPixmap(QPixmap(expense_categories[0][1]))
        self.wid.amount_label.setText(
            "฿{:,.2f}".format(expense_categories[0][2]))

        if len(expense_categories) < 2:
            return
        self.wid.category_label_2.setText(expense_categories[1][0])
        self.wid.icon_label_2.setPixmap(QPixmap(expense_categories[1][1]))
        self.wid.amount_label_2.setText(
            "฿{:,.2f}".format(expense_categories[1][2]))

        if len(expense_categories) < 3:
            return
        self.wid.category_label_3.setText(expense_categories[2][0])
        self.wid.icon_label_3.setPixmap(QPixmap(expense_categories[2][1]))
        self.wid.amount_label_3.setText(
            "฿{:,.2f}".format(expense_categories[2][2]))

    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()

    def add(self):
        self.layout.insertWidget(-1, self)

