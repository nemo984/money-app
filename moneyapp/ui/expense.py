from typing import List
from ..app.helpers import Observer
from ..app.model import Expense
from ..app.expense_system import ExpenseSystem
from .uipy.expense_popup import Ui_Dialog
from .uipy.expense_wid import Ui_expense_form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class ExpenseUI(Observer):

    def __init__(self, ui, s: ExpenseSystem, history_system, parent):
        self.ui = ui
        self.parent = parent
        self.system = s
        self.history_system = history_system
        self.expenses = []
        self.pop = Ui_Dialog()
        self.lay = self.ui.verticalLayout_38
        self.ui.add_expense_button.clicked.connect(self.add_expense)
        self.parent = parent

    def add_expense(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.pop.date_entry.setDateTime(QDateTime.currentDateTime())
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.pop.cancel_btn.clicked.connect(self.close)
        self.dialog.show()

    def close_dia(self):
        date = self.pop.date_entry.text()
        category = str(self.pop.category_comboBox.currentText())
        amount = int(self.pop.amount_entry.text())
        note = self.pop.note_entry.toPlainText()
        index_cat = self.pop.category_comboBox.currentIndex()
        index_bud = self.pop.budget_comboBox.currentIndex()              
        self.dialog.close()
        expense = self.system.add(
            category, amount, date,note
        )
        ex = ExpenseItem(expense.id ,self.ui.verticalLayout_38,
                         date, category, amount, note, index_cat, index_bud, self.history_system,self.system)
        self.history_system.add(
            action="Expense", action_type="Create", description="You created a new expense")

    def close(self):
        self.dialog.close()

    async def update(self, expenses: List[Expense]):
        print(expenses)
        self.clear_layout()
        for expense in expenses:
            expense = ExpenseItem( expense_id=expense.id ,lay = self.lay , date = expense.date, category = expense.category,
                                amount = expense.amount, note = expense.note, index_cat = expense_category_dropdown[expense.category],
                                index_bud = 0, history_system=self.history_system, expense_system=self.system)
            expense.add()
            self.expenses.append(expense)

    def clear_layout(self):
        for expense in self.expenses:
            expense.clear()
        self.expense = []

expense_category_dropdown = {"Food":0, "Entertainment":1, "Transport":2, "Education":3, "Healthcare":4, "Bill":5, "Saving":6, "Investment":7, "Shopping":8, "Utilities/Other":9}

class ExpenseItem(QWidget):
    def __init__(self,expense_id, lay: QVBoxLayout, date, category, amount, note, index_cat, index_bud, history_system, expense_system):
        super(ExpenseItem, self).__init__()
        self.id = expense_id
        self.layout = lay
        self.wid = Ui_expense_form()
        self.pop = Ui_Dialog()
        self.index_cat = index_cat
        self.index_bud = index_bud
        self.amount = amount
        self.note = note
        self.date = date
        self.history_system = history_system
        self.expense_system = expense_system

        self.wid.setupUi(self)
        self.wid.date_label.setText(date)
        self.wid.category_label.setText(category)
        self.wid.amount_label.setText("฿{:,.2f}".format(amount))
        self.wid.option_btn.clicked.connect(self.option)

    def option(self):
        menu = QMenu()
        self.edit = QAction('Edit', self)
        self.edit.setData('Edit')
        self.edit.triggered.connect(self.edit_expense)
        self.delete_b = QAction('Delete', self)
        self.delete_b.setData('Delete')
        self.delete_b.triggered.connect(self.delete)

        menu.addAction(self.edit)
        menu.addAction(self.delete_b)
        menu.exec(QCursor.pos())

    def edit_expense(self):
        self.dialog = QDialog(self)
        self.pop.setupUi(self.dialog)
        self.pop.amount_entry.setText(str(self.amount))
        self.pop.category_comboBox.setCurrentIndex(self.index_cat)
        self.pop.budget_comboBox.setCurrentIndex(self.index_bud)
        self.pop.note_entry.setPlainText(self.note)
        date = QDate.fromString(self.date, "dd/M/yyyy")
        self.pop.date_entry.setDate(date)
        self.date = self.pop.date_entry.text()
        self.pop.confirm_btn.clicked.connect(self.confirm_edit)
        self.pop.cancel_btn.clicked.connect(self.cancel)
        self.dialog.show()

    def confirm_edit(self):
        date = self.pop.date_entry.text()
        amount = self.pop.amount_entry.text()
        category = str(self.pop.category_comboBox.currentText())
        self.wid.amount_label.setText("฿{:,.2f}".format(float(amount)))
        self.wid.date_label.setText(date)
        self.wid.category_label.setText(category)
        self.amount = self.pop.amount_entry.text()
        self.note = self.pop.note_entry.toPlainText()
        self.category = str(self.pop.category_comboBox.currentText())
        self.index_cat = self.pop.category_comboBox.currentIndex()
        self.index_bud = self.pop.budget_comboBox.currentIndex()
        self.date = self.pop.date_entry.text()

        self.dialog.close()
        self.history_system.add(
            action="Expense", action_type="Update", description="You updated your expense")
        self.expense_system.update(
            expense_id = self.id ,date = self.date,category=self.category,amount=float(self.amount),note=self.note)

    def cancel(self):
        self.dialog.close()

    def add(self):
        self.layout.insertWidget(0, self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()
        self.expense_system.delete(self.id)
        self.history_system.add(
            action="Expense", action_type="Delete", description="You deleted your expense")

    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()
