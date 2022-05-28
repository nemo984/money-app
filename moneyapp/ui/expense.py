from typing import List
from ..app.helpers import Observer
from ..app.model import Expense
from ..app.expense_system import ExpenseSystem
from .uipy.expense_popup import Ui_Dialog
from .uipy.expense_wid import Ui_expense_form
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtCharts import *

class ExpenseUI(Observer):

    def __init__(self, ui, s: ExpenseSystem, budget_system, parent):
        self.ui = ui
        self.parent = parent
        self.system = s
        self.budget_system = budget_system
        self.expenses = []
        self.pop = Ui_Dialog()
        self.lay = self.ui.verticalLayout_38
        self.ui.add_expense_button.clicked.connect(self.add_expense)
        self.parent = parent
        self.budgets = {}
        self.ui.expense_lineEdit.textEdited.connect(self.filter_expenses)

        self.currentText = "Expense"
        self.series = QPieSeries()
        self.series.setHoleSize(0.35)
        self.series.setLabelsVisible(True)
        self.series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignRight)
 
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.ui.pie_widdget.setContentsMargins(0, 0, 0, 0)
        lay = QHBoxLayout(self.ui.expense_graph_container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.chartview)

    def change_graph(self, expenses_catagories):
        self.series.clear()
        for category, amount in expenses_catagories.items():
            if amount != 0: 
                self.series.append(category, amount)

        for slice in self.series.slices():
            slice.setLabel(f"{slice.label()} {100 * slice.percentage():.2f}%")

    def add_expense(self):
        self.dialog = QDialog(self.parent)
        self.pop.setupUi(self.dialog)
        self.dialog.setWindowTitle("Add expense")
        self.pop.date_entry.setDateTime(QDateTime.currentDateTime())
        self.pop.confirm_btn.clicked.connect(self.close_dia)
        self.pop.cancel_btn.clicked.connect(self.close_popup)
        self.pop.category_comboBox.currentTextChanged.connect(
            self.category_change)

        self.category_change("Food")
        self.dialog.show()

    def category_change(self, value):
        self.pop.budget_comboBox.clear()
        budgets = self.budget_system.getByCategory(value)
        self.budgets = {f"{b.start_date} {b.name}": b for b in budgets}
        self.pop.budget_comboBox.addItem("None")
        self.pop.budget_comboBox.addItems(self.budgets.keys())

    def close_dia(self):
        date = self.pop.date_entry.text()
        category = str(self.pop.category_comboBox.currentText())
        budget = str(self.pop.budget_comboBox.currentText())

        if(self.isfloat(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "Input in amount section is not a number")
            return
        
        if(self.Maximun(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "the Maximun of amount is 1 trillion")
            return

        if(self.isNegative(self.pop.amount_entry.text()) == True):
            self.pop.warning_label.setText(
                "amount cannot be negative")
            return

        amount = float(self.pop.amount_entry.text())
        note = self.pop.note_entry.toPlainText()
        index_cat = self.pop.category_comboBox.currentIndex()
        index_bud = self.pop.budget_comboBox.currentIndex()
        budget = self.budgets[budget] if budget in self.budgets else None
        self.dialog.close()
        expense = self.system.add(
            category=category, amount=amount, date=date, note=note, budget=budget
        )
        ex = ExpenseItem(expense.id, self.lay,
                         date, category, amount, note, index_cat, self.system, budget, budget_system=self.budget_system)


    def close_popup(self):
        self.dialog.close()

    async def update(self, expenses: List[Expense]):
        self.clear_layout()
        for expense in expenses:
            expense = ExpenseItem(expense_id=expense.id, lay=self.lay, date=expense.date, category=expense.category,
                                  amount=expense.amount, note=expense.note, index_cat=expense_category_dropdown[
                                      expense.category],
                                  expense_system=self.system, budget=expense.budget, budget_system=self.budget_system)
            expense.add()
            self.expenses.append(expense)
        
        data = self.system.get_expenses_total()
        self.change_total_expenses(data)
        self.change_graph(data)

    def change_total_expenses(self, data):
        self.ui.expense_daily_value.setText("฿{:,.2f}".format(data["daily"]))
        self.ui.expense_weekly_value.setText("฿{:,.2f}".format(data["weekly"]))
        self.ui.expense_monthly_value.setText("฿{:,.2f}".format(data["monthly"]))
        self.ui.expense_yearly_value.setText("฿{:,.2f}".format(data["yearly"]))

    def clear_layout(self):
        for expense in self.expenses:
            expense.clear()
        self.expenses = []

    def filter_expenses(self, text):
        self.system.filter(text)

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def isNegative(self,num):
        if float(num) < 0:
            return True
        else:
            return False
    
    def Maximun(self,num):
        if float(num) > 1000000000000:
            return False
        else:
            return True



expense_category_dropdown = {"Food": 0, "Entertainment": 1, "Transport": 2, "Education": 3,
                             "Healthcare": 4, "Bill": 5, "Saving": 6, "Investment": 7, "Shopping": 8, "Utilities/Other": 9}


class ExpenseItem(QWidget):
    def __init__(self, expense_id, lay: QVBoxLayout, date, category, amount, note, index_cat, expense_system, budget, budget_system):
        super(ExpenseItem, self).__init__()
        self.id = expense_id
        self.layout = lay
        self.wid = Ui_expense_form()
        self.pop = Ui_Dialog()
        self.budget_system = budget_system
        self.index_cat = index_cat
        self.amount = amount
        self.note = note
        self.date = date
        self.expense_system = expense_system
        self.budget = budget
        self.category = category
        self.budget_category = budget.name if budget is not None else None
        
        self.wid.setupUi(self)
        self.wid.date_label.setText(date)
        self.wid.category_label.setText(category)
        self.wid.amount_label.setText("฿{:,.2f}".format(amount))
        if budget is not None:
            self.wid.budget_label.setText(budget.name)
        if budget is None:
            self.wid.budget_label.setText("")
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
        self.dialog.setWindowTitle("Edit expense")
        self.pop.amount_entry.setText(str(self.amount))
        self.pop.category_comboBox.setCurrentIndex(self.index_cat)
        self.pop.note_entry.setPlainText(self.note)
        date = QDate.fromString(self.date, "dd/M/yyyy")
        self.pop.date_entry.setDate(date)
        self.date = self.pop.date_entry.text()
        self.pop.confirm_btn.clicked.connect(self.confirm_edit)
        self.pop.cancel_btn.clicked.connect(self.cancel)
        self.pop.category_comboBox.currentTextChanged.connect(
            self.category_change)
        self.category_change(self.category)
        if self.budget: self.pop.budget_comboBox.setCurrentText(self.budget.name)
        self.dialog.show()

    def category_change(self, value):
        self.pop.budget_comboBox.clear()
        budgets = self.budget_system.getByCategory(value)
        self.budgets = {f"{b.start_date} {b.name}": b for b in budgets}
        self.pop.budget_comboBox.addItem("None")
        self.pop.budget_comboBox.addItems(self.budgets.keys())

    def confirm_edit(self):
        if(self.isfloat(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "Input in amount section is not a number")
            return
        
        if(self.Maximun(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "the Maximun of amount is 1 trillion")
            return

        if(self.isNegative(self.pop.amount_entry.text()) == True):
            self.pop.warning_label.setText(
                "amount cannot be negative")
            return
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

        self.expense_system.update(
            expense_id=self.id, date=self.date, category=self.category, amount=float(self.amount), note=self.note)

    def change_budget_index(self):
        index = self.pop.budget_comboBox.findText(
            f"{self.budget.start_date} {self.budget.name}", Qt.MatchFixedString)
        if index >= 0:
            self.index_bud = index
            self.pop.budget_comboBox.setCurrentIndex(index)

    def cancel(self):
        self.dialog.close()

    def add(self):
        self.layout.insertWidget(0, self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()
        self.expense_system.delete(self.id)


    def clear(self):
        self.layout.removeWidget(self)
        self.deleteLater()

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def isNegative(self,num):
        if float(num) < 0:
            return True
        else:
            return False
    
    def Maximun(self,num):
        if float(num) > 1000000000000:
            return False
        else:
            return True
