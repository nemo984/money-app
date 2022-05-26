from typing import List
from unicodedata import category
from ..app.helpers import Observer
from ..app.model import Budget
from ..app.budget_system import BudgetSystem
from .uipy.budget_popup import Ui_Dialog
from .uipy.budget_wid import Ui_Form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class BudgetUI(Observer):
    def __init__(self, ui, account, budget_system: BudgetSystem, history_system, parent):
        self.ui = ui
        self.account = account
        self.system = budget_system
        self.history_system = history_system
        self.parent = parent
        self.pop = Ui_Dialog()
        self.ui.add_Budget.clicked.connect(self.add_budget)
        self.parent = parent

    def add_budget(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.pop.startDate_entry.setDateTime(QDateTime.currentDateTime())
        self.pop.endDate_entry.setDateTime(QDateTime.currentDateTime())
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.pop.cancel_btn.clicked.connect(self.close)
        self.dialog.show()

    def close_dia(self):
        start_date = self.pop.startDate_entry.text()
        end_date = self.pop.endDate_entry.text()
        head = self.pop.name_entry.text()
        amount = float(self.pop.amount_entry.text())
        index = self.pop.category_comboBox.currentIndex()
        c = self.pop.category_comboBox.currentText()
        note = self.pop.note_entry.toPlainText()
        b = BudgetItem(self.ui.verticalLayout_24, head, amount,
                       start_date, end_date, index, note)
        b.add()
        self.dialog.close()
        self.history_system.add(action="Budget", action_type="Create", description="You created a budget")
        self.system.add(c,amount,end_date,note)
        

    def close(self):
        self.dialog.close()

    async def update(self, budgets: List[Budget]):
        pass


class BudgetItem(QWidget):
    def __init__(self, lay: QVBoxLayout, head, amount, start_date, end_date, index, note):
        super(BudgetItem, self).__init__()
        self.layout = lay
        self.wid = Ui_Form()
        self.pop = Ui_Dialog()
        self.index = index
        self.amount = amount
        self.note = note
        self.s_date = start_date
        self.e_date = end_date

        self.wid.setupUi(self)
        self.wid.hearde.setText(head)
        self.wid.amount.setText("฿{:,.2f}".format(amount))
        self.wid.end_date.setText("End Date:"+end_date)
        self.wid.start_date.setText("Start Date:"+start_date)
        self.wid.progressBar.setValue(0)
        self.wid.progressBar.setMaximum(amount)
        self.wid.label_9.setText("Until you reach"+"฿{:,.2f}".format(amount))
        self.wid.more_btn.clicked.connect(self.option)

    def option(self):
        menu = QMenu()
        self.edit = QAction('Edit', self)
        self.edit.setData('Edit')
        self.edit.triggered.connect(self.edit_budget)
        self.delete_b = QAction('Delete', self)
        self.delete_b.setData('Delete')
        self.delete_b.triggered.connect(self.delete)

        menu.addAction(self.edit)
        menu.addAction(self.delete_b)
        menu.exec(QCursor.pos())

    def hi(self):
        print("hi")

    def edit_budget(self):
        self.dialog = QDialog(self)
        self.pop.setupUi(self.dialog)
        self.pop.amount_entry.setText(str(self.amount))
        self.pop.name_entry.setText(self.wid.hearde.text())
        self.pop.category_comboBox.setCurrentIndex(self.index)
        self.pop.note_entry.setPlainText(self.note)
        self.pop.confirm_btn.clicked.connect(self.confirm_edit)
        s_date = QDate.fromString(self.s_date,"dd/M/yyyy")
        e_date = QDate.fromString(self.e_date,"dd/M/yyyy")
        self.pop.startDate_entry.setDate(s_date)
        self.pop.endDate_entry.setDate(e_date)
        s_date = self.pop.startDate_entry.text()
        e_date = self.pop.endDate_entry.text()
        self.dialog.show()

    def confirm_edit(self):
        start_date = self.pop.startDate_entry.text()
        end_date = self.pop.endDate_entry.text()
        head = self.pop.name_entry.text()
        amount = self.pop.amount_entry.text()
        self.wid.hearde.setText(head)
        self.wid.amount.setText("฿{:,.2f}".format(float(amount)))
        self.wid.label_9.setText("Until you reach"+"฿{:,.2f}".format(float(amount)))
        self.wid.end_date.setText("End Date:"+end_date)
        self.wid.start_date.setText("Start Date:"+start_date)
        self.amount = self.pop.amount_entry.text()
        self.note = self.pop.note_entry.toPlainText()
        self.index = self.pop.category_comboBox.currentIndex()
        self.dialog.close()

    def add(self):
        self.layout.insertWidget(0, self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()
