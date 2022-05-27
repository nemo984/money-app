from typing import List
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
        self.budgets = []
        self.budgets_layout = self.ui.verticalLayout_24

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
        name = self.pop.name_entry.text()
        amount = float(self.pop.amount_entry.text())
        index = self.pop.category_comboBox.currentIndex()
        c = self.pop.category_comboBox.currentText()
        note = self.pop.note_entry.toPlainText()
        self.dialog.close()
        budget = self.system.add(category=c, name=name, amount=amount, start_date=start_date, end_date=end_date)
        b = BudgetItem(budget_id=budget.id, budget_system=self.system, history_system=self.history_system, lay=self.budgets_layout, amount=amount, category=c,
                       end_date=end_date, index=index, note=note, name=name, start_date=start_date)
        self.history_system.add(action="Budget", action_type="Create", description="You created a budget")
        

    def close(self):
        self.dialog.close()

    async def update(self, budgets: List[Budget]):
        self.clear_layout()
        for budget in budgets:
            budget = BudgetItem(budget_id=budget.id, budget_system=self.system, history_system=self.history_system, lay=self.budgets_layout, name=budget.name, 
                                category=budget.category, index=budget_category_dropdown[budget.category], 
                                amount=budget.amount, start_date=budget.start_date, end_date=budget.end_date,
                                note=budget.note)
            budget.add()
            self.budgets.append(budget)

    def clear_layout(self):
        for budget in self.budgets:
            budget.clear()
        self.budgets = []


budget_category_dropdown = {"Food":0, "Entertainment":1, "Transport":2, "Education":3, "Healthcare":4, "Bill":5, "Saving":6, "Investment":7, "Shopping":8, "Utilities/Other":9}

class BudgetItem(QWidget):
    def __init__(self, budget_id, budget_system, history_system, lay: QVBoxLayout, category, name, amount, start_date, end_date, index, note):
        super(BudgetItem, self).__init__()
        self.id = budget_id
        self.budget_system = budget_system
        self.history_system = history_system
        self.layout = lay
        self.wid = Ui_Form()
        self.pop = Ui_Dialog()
        self.index = index
        self.amount = amount
        self.note = note
        self.s_date = start_date
        self.e_date = end_date
        self.category = category
        self.name = name

        self.wid.setupUi(self)
        self.wid.name_label.setText(self.name)
        self.wid.category_label.setText(self.category)
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
        

    def edit_budget(self):
        self.dialog = QDialog(self)
        self.pop.setupUi(self.dialog)
        self.pop.amount_entry.setText(str(self.amount))
        self.pop.name_entry.setText(self.wid.name_label.text())
        self.pop.category_comboBox.setCurrentIndex(self.index)
        self.pop.note_entry.setPlainText(self.note)   
        s_date = QDate.fromString(self.s_date,"dd/M/yyyy")
        e_date = QDate.fromString(self.e_date,"dd/M/yyyy")
        self.pop.startDate_entry.setDate(s_date)
        self.pop.endDate_entry.setDate(e_date)
        self.s_date = self.pop.startDate_entry.text()
        self.e_date = self.pop.endDate_entry.text()
        self.pop.confirm_btn.clicked.connect(self.confirm_edit)
        self.dialog.show()
        
    def confirm_edit(self):
        self.name = self.pop.name_entry.text()
        self.amount = self.pop.amount_entry.text()
        self.note = self.pop.note_entry.toPlainText()
        self.index = self.pop.category_comboBox.currentIndex()
        self.s_date = self.pop.startDate_entry.text()
        self.e_date = self.pop.endDate_entry.text()
        self.index = self.pop.category_comboBox.currentIndex()
        self.category = self.pop.category_comboBox.currentText()

        self.wid.name_label.setText(self.name)
        self.wid.category_label.setText(self.category)
        self.wid.amount.setText("฿{:,.2f}".format(float(self.amount)))
        self.wid.label_9.setText("Until you reach"+"฿{:,.2f}".format(float(self.amount)))
        self.wid.end_date.setText("End Date: "+ self.e_date)
        self.wid.start_date.setText("Start Date: "+ self.s_date)

        self.dialog.close()
        self.budget_system.update(budget_id=self.id, name=self.name, amount=float(self.amount), start_date=self.s_date, end_date=self.e_date, note=self.note, category=self.category)
        self.history_system.add(action="Budget", action_type="Update", description="You updated a budget")
        
    def add(self):
        self.layout.insertWidget(0, self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()
        self.budget_system.delete(self.id)
        self.history_system.add(action="Budget", action_type="Delete", description="You deleted a budget")

    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()
