from typing import List
from ..app.helpers import Observer
from ..app.model import Income
from ..app.income_system import IncomeSystem
from .uipy.income_popup import Ui_Dialog
from .uipy.income_wid import Ui_income_form
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class IncomeUI(Observer):

    def __init__(self, ui, s: IncomeSystem, parent):
        self.ui = ui
        self.parent = parent
        self.system = s
        self.pop = Ui_Dialog()
        self.ui.add_income_button.clicked.connect(self.add_income)

    def add_income(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.dialog.show()

    def close_dia(self):
        date = self.pop.date_entry.text()
        name = self.pop.name_entry.text()
        category = str(self.pop.category_comboBox.currentText())
        # str(combobox1.currentText())
        amount = int(self.pop.amount_entry.text())
        recurrence = str(self.pop.recurence_comboBox.currentText())
        inc = IncomeItem(self.ui.verticalLayout_39, date,
                         name, category, amount, recurrence)
        inc.add()
        self.dialog.close()

    # Income: 100 / frequency_day
    # Every 10 day -> (100 * 10) / frequency_day

    # Problem: Show income history every month
    # 1. User add the first income with amount = 20000, frequency = 28 - January
    # 2. User add the second income with amount = 1500, frequency = 7 - January
    # 3. User edited the first income to amount = 36000 - March

    # Problem: Show income history every month
    # 1. User add the first income with amount = 20000, frequency = 28 - January
    # 2. User add the second income with amount = 1500, frequency = 7 - Feb
    # 3. User edited the first income to amount = 36000 - March

    # Problem: Show income history every month
    # 1. User add the first income with amount = 20000, frequency = 28 - Feb
    # 2. User add the second income with amount = 1500, frequency = 7 - Feb
    # 3. User edited the first income to amount = 36000 - March

    # January, 26000
    # Feb, 26000
    # March, 42000

    #            create_date, amount
    # Add Income 1: January, 30000
    # Add Income 2: January, 2500
    # Add Income 3: Feb, 20000
    # incomes = [[January, 30000], [January, 2500], [Feb, 20000]]

    async def update(self, incomes: List[Income]):
        print("Incomes updated: Updating income page UI")

        n = 28
        total = 0
        for income in incomes:
            total += (income.amount * n) / \
                income.frequency_day  # Total Income per N day

            print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")

        # 1,.., 12
        for month in range(1, 13):
            month_total = 0
            for income in incomes:
                if income.created_date.month > month:
                    continue
                month_total += (income.amount * 28) / income.frequency_day

            print(f"Month {month} : {month_total}")

        # Month 1 : 32500
        # Month 2 : 52500

        print("================")


class IncomeItem(QWidget):
    def __init__(self, lay: QVBoxLayout, date, name, category, amount, recurrence):
        super(IncomeItem, self).__init__()
        self.layout = lay
        self.wid = Ui_income_form()
        self.wid.setupUi(self)
        self.wid.date_label.setText(date)
        self.wid.name_label.setText(name)
        self.wid.category_label.setText(category)
        self.wid.amount_label.setText("฿{:,.2f}".format(amount))
        self.wid.recurrence_label.setText(recurrence)

        self.wid.option_btn.clicked.connect(self.option)

    def option(self):
        menu = QMenu()
        #self.Edit = menu.addAction('Edit')
        self.edit = QAction('Edit', self)
        self.edit.setData('Edit')
        self.edit.triggered.connect(self.edit_income)
        self.delete_b = QAction('Delete', self)
        self.delete_b.setData('Delete')
        self.delete_b.triggered.connect(self.delete)
        menu.addAction(self.edit)
        menu.addAction(self.delete_b)
        menu.exec(QCursor.pos())

    def hi(self):
        print("hi")

    def edit_income(self):

    def add(self):
        self.layout.insertWidget(0, self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()
