from typing import List
from ..app.helpers import Observer
from ..app.model import Income
from ..app.income_system import IncomeSystem
from .uipy.income_popup import Ui_Dialog
from .uipy.income_wid import Ui_income_form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

income_category_dropdown = {"Full-time": 0,
                            "Part-time": 1, "Passive": 2, "Other": 3}
income_recurrence_dropdown = {"one-time": 0,
                              "daily": 1, "weekly": 2, "monthly": 3, "yearly": 4}


class IncomeUI(Observer):

    def __init__(self, ui, income_system: IncomeSystem, parent):
        self.ui = ui
        self.parent = parent
        self.system = income_system
        self.pop = Ui_Dialog()
        self.ui.add_income_button.clicked.connect(self.add_income)
        self.parent = parent
        self.incomes = []
        self.incomes_layout = self.ui.verticalLayout_40
        self.ui.income_lineEdit.textEdited.connect(self.filter_incomes)

    def add_income(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.dialog.setWindowTitle("Add income")
        self.pop.date_entry.setDateTime(QDateTime.currentDateTime())
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.pop.cancel_btn.clicked.connect(self.close)

        self.dialog.show()

    def close_dia(self):
        date = self.pop.date_entry.text()

        if not self.pop.name_entry.text():
            self.pop.warning_label.setText("No input in name section")
            return

        name = self.pop.name_entry.text()
        category = str(self.pop.category_comboBox.currentText())

        if(self.isfloat(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "Input in amount section is not a number")
            return

        if(self.Stringlen(self.pop.name_entry.text()) == False):
            self.pop.warning_label.setText(
                "Name should be between 0-24 character")
            return

        if(self.Maximun(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "the Maximun of amount is 1 trillion")
            return

        if(self.isNegative(self.pop.amount_entry.text()) == True):
            self.pop.warning_label.setText(
                "amount cannot be negative")
            return
        amount = int(self.pop.amount_entry.text())
        recurrence = self.pop.recurence_comboBox.currentText()
        note = self.pop.note_entry.toPlainText()
        index_cat = self.pop.category_comboBox.currentIndex()
        index_rec = self.pop.recurence_comboBox.currentIndex()
        self.dialog.close()
        income = self.system.add(name=name, category=category, amount=amount,
                                 date=date, note=note, recurrence=recurrence)
        inc = IncomeItem(income_id=income.id, income_system=self.system, lay=self.incomes_layout, date=date,
                         name=name, category=category, amount=amount, recurrence=recurrence, note=note, index_cat=index_cat, index_rec=index_rec)

    def close(self):
        self.dialog.close()

    def Stringlen(self, string):
        l = len(string)
        if l > 24 or l < 0:
            return False
        else:
            return True

    def isNegative(self, num):
        if float(num) < 0:
            return True
        else:
            return False

    def Maximun(self, num):
        if float(num) > 1000000000000:
            return False
        else:
            return True

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

        # n = 28
        # total = 0
        # for income in incomes:
        #     total += (income.amount * n) / \
        #         income.frequency_day  # Total Income per N day

        #     print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")

        # # 1,.., 12
        # for month in range(1, 13):
        #     month_total = 0
        #     for income in incomes:
        #         if income.created_date.month > month:
        #             continue
        #         month_total += (income.amount * 28) / income.frequency_day

        #     print(f"Month {month} : {month_total}")

        # Month 1 : 32500
        # Month 2 : 52500

        self.clear_layout()
        for income in incomes:
            income = IncomeItem(income_id=income.id, income_system=self.system, lay=self.incomes_layout, date=income.date,
                                name=income.name, category=income.category, amount=income.amount, recurrence=income.recurrence, note=income.note,
                                index_cat=income_category_dropdown[income.category], index_rec=income_recurrence_dropdown[income.recurrence])
            income.add()
            self.incomes.append(income)

    def filter_incomes(self, text):
        self.system.filter(text)

    def clear_layout(self):
        for income in self.incomes:
            income.clear()
        self.incomes = []

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False


class IncomeItem(QWidget):
    def __init__(self, income_id, income_system, lay: QVBoxLayout, date, name, category, amount, recurrence, note, index_cat, index_rec):
        super(IncomeItem, self).__init__()
        self.id = income_id
        self.income_system = income_system
        self.layout = lay
        self.wid = Ui_income_form()
        self.pop = Ui_Dialog()
        self.index_cat = index_cat
        self.index_rec = index_rec
        self.name = name
        self.amount = amount
        self.note = note
        self.date = date
        self.recurrence = recurrence

        self.wid.setupUi(self)
        self.wid.date_label.setText(date)
        self.wid.name_label.setText(name)
        self.wid.category_label.setText(category)
        self.wid.amount_label.setText("฿{:,.2f}".format(amount))
        self.wid.recurrence_label.setText(recurrence)

        self.wid.option_btn.clicked.connect(self.option)

    def option(self):
        menu = QMenu()
        self.edit = QAction('Edit', self)
        self.edit.setData('Edit')
        self.edit.triggered.connect(self.edit_income)
        self.delete_b = QAction('Delete', self)
        self.delete_b.setData('Delete')
        self.delete_b.triggered.connect(self.delete)

        menu.addAction(self.edit)
        menu.addAction(self.delete_b)
        menu.exec(QCursor.pos())

    def edit_income(self):
        self.dialog = QDialog(self)
        self.pop.setupUi(self.dialog)
        self.dialog.setWindowTitle("Edit income")
        self.pop.name_entry.setText(self.name)
        self.pop.amount_entry.setText(str(self.amount))
        self.pop.category_comboBox.setCurrentIndex(self.index_cat)
        self.pop.recurence_comboBox.setCurrentIndex(self.index_rec)
        self.pop.note_entry.setPlainText(self.note)
        date = QDate.fromString(self.date, "dd/M/yyyy")
        self.pop.date_entry.setDate(date)
        self.date = self.pop.date_entry.text()
        self.pop.confirm_btn.clicked.connect(self.confirm_edit)
        self.pop.cancel_btn.clicked.connect(self.cancel)
        self.dialog.show()

    def confirm_edit(self):
        if not self.pop.name_entry.text():
            self.pop.warning_label.setText("No input in name section")
            return

        if(self.isfloat(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "Input in amount section is not a number")
            return

        if(self.Stringlen(self.pop.name_entry.text()) == False):
            self.pop.warning_label.setText(
                "Name should be between 0-24 character")
            return

        if(self.Maximun(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "the Maximun of amount is 1 trillion")
            return

        if(self.isNegative(self.pop.amount_entry.text()) == True):
            self.pop.warning_label.setText(
                "amount cannot be negative")
            return

        self.date = self.pop.date_entry.text()
        self.amount = self.pop.amount_entry.text()
        self.category = str(self.pop.category_comboBox.currentText())
        self.recurrence = str(self.pop.recurence_comboBox.currentText())
        self.wid.amount_label.setText("฿{:,.2f}".format(float(self.amount)))
        self.wid.date_label.setText(self.date)
        self.wid.category_label.setText(self.category)
        self.wid.recurrence_label.setText(self.recurrence)
        self.name = self.pop.name_entry.text()
        self.note = self.pop.note_entry.toPlainText()
        self.category = str(self.pop.category_comboBox.currentText())
        self.index_cat = self.pop.category_comboBox.currentIndex()
        self.index_rec = self.pop.recurence_comboBox.currentIndex()
        self.dialog.close()
        self.income_system.update(income_id=self.id, name=self.name, category=self.category, amount=float(
            self.amount), recurrence=self.recurrence, note=self.note)

    def cancel(self):
        self.dialog.close()

    def add(self):
        self.layout.insertWidget(0, self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()
        self.income_system.delete(self.id)

    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def Stringlen(self, string):
        l = len(string)
        if l > 24 or l < 0:
            return False
        else:
            return True

    def isNegative(self, num):
        if float(num) < 0:
            return True
        else:
            return False

    def Maximun(self, num):
        if float(num) > 1000000000000:
            return False
        else:
            return True
