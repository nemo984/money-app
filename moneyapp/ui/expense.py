from typing import List
from ..app.helpers import Observer
from ..app.model import Expense
from ..app.expense_system import ExpenseSystem
from .uipy.expense_popup import Ui_Dialog
from .uipy.expense_wid import Ui_expense_form
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class ExpenseUI(Observer):

    def __init__(self, ui, s: ExpenseSystem, parent):
        self.ui = ui
        self.parent = parent
        self.system = s
        self.pop = Ui_Dialog()
        self.ui.add_expense_button.clicked.connect(self.add_expense)

    def add_expense(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.dialog.show()

    def close_dia(self):
        date =self.pop.date_entry.text()
        category = str(self.pop.category_comboBox.currentText())
        #str(combobox1.currentText())
        amount = int(self.pop.amount_entry.text())
        ex = ExpenseItem(self.ui.verticalLayout_38, date,category,amount)
        ex.add()
        self.dialog.close()


    async def update(self, incomes: List[Expense]):
        pass

class ExpenseItem(QWidget):
    def __init__(self, lay: QVBoxLayout, date,category,amount):
        super(ExpenseItem, self).__init__()
        self.layout = lay
        self.wid = Ui_expense_form()
        self.wid.setupUi(self)
        self.wid.date_label.setText(date)
        self.wid.category_label.setText(category)
        self.wid.amount_label.setText("฿{:,.2f}".format(amount))
        
        self.wid.option_btn.clicked.connect(self.option)

    def option(self):
        menu = QMenu()
        Edit = menu.addAction('Edit')
        delete = menu.addAction('Delete')
        menu.exec(QCursor.pos())

    def hi(self):
        print("hi")

    def add(self):
        self.layout.insertWidget(0,self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()