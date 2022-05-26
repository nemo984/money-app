from typing import List
from ..app.helpers import Observer
from ..app.model import Budget
from ..app.budget_system import BudgetSystem
from .uipy.budget_popup import Ui_Dialog
from .uipy.budget_wid import Ui_Form
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class BudgetUI(Observer):
    
    def __init__(self, ui, s: BudgetSystem, parent):
        self.ui = ui
        self.parent = parent
        self.system = s
        self.pop = Ui_Dialog()
        self.ui.add_Budget.clicked.connect(self.add_budget)


    def add_budget(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.dialog.show()

    def close_dia(self):
        start_date =self.pop.startDate_entry.text()
        end_date = self.pop.endDate_entry.text()
        head = self.pop.name_entry.text()
        amount = int(self.pop.amount_entry.text())
        b = BudgetItem(self.ui.verticalLayout_24, head, amount, start_date,end_date)
        b.add()
        self.dialog.close()

    #def delete_bud(self):
    
    
        
    async def update(self, budgets: List[Budget]):
        pass


class BudgetItem(QWidget):
    def __init__(self, lay: QVBoxLayout, head, amount, start_date,end_date):
        super(BudgetItem, self).__init__()
        self.layout = lay
        self.wid = Ui_Form()
        self.wid.setupUi(self)
        self.wid.hearde.setText(head)
        self.wid.amount.setText("฿{:,.2f}".format(amount))
        self.wid.end_date.setText("End Date:"+end_date)
        self.wid.start_date.setText("Start Date:"+start_date)
        self.wid.progressBar.setValue(0)
        self.wid.progressBar.setMaximum(amount)
        self.wid.more_btn.clicked.connect(self.option)

    def option(self):
        menu = QMenu()
        #self.Edit = menu.addAction('Edit')
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
        print("test")

    def add(self):
        self.layout.insertWidget(0,self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()