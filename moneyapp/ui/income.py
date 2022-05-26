from typing import List
from ..app.helpers import Observer
from ..app.model import Income
from ..app.income_system import IncomeSystem
from .uipy.income_popup import Ui_Dialog
from .uipy.income_wid import Ui_income_form
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class IncomeUI(Observer):

    def __init__(self, ui, s: IncomeSystem, history_system, parent):
        self.ui = ui
        self.parent = parent
        self.system = s
        self.history_system = history_system
        self.pop = Ui_Dialog()
        self.ui.add_income_button.clicked.connect(self.add_income)

    def add_income(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.pop.cancel_btn.clicked.connect(self.close)

        self.dialog.show()

    def close_dia(self):
        date = self.pop.date_entry.text()
        name = self.pop.name_entry.text()
        category = str(self.pop.category_comboBox.currentText())
        amount = int(self.pop.amount_entry.text())
        recurrence = str(self.pop.recurence_comboBox.currentText())
        note = self.pop.note_entry.toPlainText()
        index_cat = self.pop.category_comboBox.currentIndex()
        index_rec = self.pop.recurence_comboBox.currentIndex()
        inc = IncomeItem(self.ui.verticalLayout_39, date,
                         name, category, amount, recurrence, note, index_cat, index_rec)
        inc.add()
        self.dialog.close()
        change.recToInt(recurrence)

    def close(self):
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
    def __init__(self, lay: QVBoxLayout, date, name, category, amount, recurrence, note, index_cat, index_rec):
        super(IncomeItem, self).__init__()
        self.layout = lay
        self.wid = Ui_income_form()
        self.pop = Ui_Dialog()
        self.index_cat = index_cat
        self.index_rec = index_rec
        self.name = name
        self.amount = amount
        self.note = note

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
        self.pop.name_entry.setText(self.name)
        self.pop.amount_entry.setText(str(self.amount))
        self.pop.category_comboBox.setCurrentIndex(self.index_cat)
        self.pop.recurence_comboBox.setCurrentIndex(self.index_rec)
        self.pop.note_entry.setPlainText(self.note)
        #date = QDate.fromString(self.sdate,"dd/M/yyyy")
        # self.pop.startDate_entry.setDate(date)
        #date = self.pop.date_entry.text()
        self.pop.confirm_btn.clicked.connect(self.confirm_edit)
        self.pop.cancel_btn.clicked.connect(self.cancel)
        self.dialog.show()

    def confirm_edit(self):
        date = self.pop.date_entry.text()
        amount = self.pop.amount_entry.text()
        category = str(self.pop.category_comboBox.currentText())
        recurrence = str(self.pop.recurence_comboBox.currentText())
        self.wid.amount_label.setText("฿{:,.2f}".format(float(amount)))
        self.wid.date_label.setText(date)
        self.wid.category_label.setText(category)
        self.wid.recurrence_label.setText(recurrence)
        self.name = self.pop.name_entry.text()
        self.amount = self.pop.amount_entry.text()
        self.note = self.pop.note_entry.toPlainText()
        self.category = str(self.pop.category_comboBox.currentText())
        self.index_cat = self.pop.category_comboBox.currentIndex()
        self.index_rec = self.pop.recurence_comboBox.currentIndex()
        self.dialog.close()

    def cancel(self):
        self.dialog.close()

    def add(self):
        self.layout.insertWidget(0, self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()


class change():
    # recurrence->one-time=None,daily=1,weekly=7,monthly=30,yearly=365
    def recToInt(recurrence):
        if(recurrence == "one-time"):
            return None
        elif(recurrence == "Daily"):
            return 1
        elif(recurrence == "Weekly"):
            return 7
        elif(recurrence == "Monthly"):
            return 30
        elif(recurrence == "Yearly"):
            return 365

    def intTorec(number):
        if(number == None):
            return "one-time"
        elif(number == 1):
            return "Daily"
        elif(number == 7):
            return "Weekly"
        elif(number == 30):
            return "Monthly"
        elif(number == 365):
            return "Yearly"
