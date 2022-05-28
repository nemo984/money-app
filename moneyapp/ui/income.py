from typing import List
from ..app.helpers import Observer
from ..app.model import Income
from ..app.income_system import IncomeSystem
from .uipy.income_popup import Ui_Dialog
from .uipy.income_wid import Ui_income_form
from .inputCheck import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtCharts import *

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
        lay = QHBoxLayout(self.ui.income_graph_container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.chartview)

    def change_graph(self, incomes_catagories):
        self.series.clear()
        for category, amount in incomes_catagories.items():
            if amount != 0: 
                self.series.append(category, amount)

        for slice in self.series.slices():
            slice.setLabel(f"{slice.label()} {100 * slice.percentage():.2f}%")

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

        if(check.isfloat(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "Input in amount section is not a number")
            return

        if(check.Stringlen(self.pop.name_entry.text()) == False):
            self.pop.warning_label.setText(
                "Name should be between 0-24 character")
            return

        if(check.Maximun(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "the Maximun of amount is 1 trillion")
            return

        if(check.isNegative(self.pop.amount_entry.text()) == True):
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

    async def update(self, incomes: List[Income]):
        self.clear_layout()
        for income in incomes:
            income = IncomeItem(income_id=income.id, income_system=self.system, lay=self.incomes_layout, date=income.date,
                                name=income.name, category=income.category, amount=income.amount, recurrence=income.recurrence, note=income.note,
                                index_cat=income_category_dropdown[income.category], index_rec=income_recurrence_dropdown[income.recurrence])
            income.add()
            self.incomes.append(income)

        data = self.system.get_incomes_total()
        self.change_total_incomes(data)
        self.change_graph(self.system.get_categories_total())

    def change_total_incomes(self, data):
        self.ui.income_daily_value.setText("฿{:,.2f}".format(data["daily"]))
        self.ui.income_weekly_value.setText("฿{:,.2f}".format(data["weekly"]))
        self.ui.income_monthly_value.setText("฿{:,.2f}".format(data["monthly"]))
        self.ui.income_yearly_value.setText("฿{:,.2f}".format(data["yearly"]))

    def filter_incomes(self, text):
        self.system.filter(text)

    def clear_layout(self):
        for income in self.incomes:
            income.clear()
        self.incomes = []


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

        if(check.isfloat(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "Input in amount section is not a number")
            return

        if(check.Stringlen(self.pop.name_entry.text()) == False):
            self.pop.warning_label.setText(
                "Name should be between 0-24 character")
            return

        if(check.Maximun(self.pop.amount_entry.text()) == False):
            self.pop.warning_label.setText(
                "the Maximun of amount is 1 trillion")
            return

        if(check.isNegative(self.pop.amount_entry.text()) == True):
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
