from typing import List
from ..app.model import ActionHistory
from ..app.history import HistorySystem
from .uipy.history_wid import Ui_history_form
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class HistoryUI:
    def __init__(self, ui, s: HistorySystem, parent):
        self.ui = ui
        self.parent = parent
        self.system = s
        self.ui.searchHistory_lineEdit.textEdited.connect(self.filter_history)
        self.current = []
        
    async def update(self, histories):
        history_layout = self.ui.verticalLayout_39
        self.clear_layout()
        for history in histories:
            item = QListWidgetItem()
            account = HistoryItem(id=history.id, history_system=self.system, lay=history_layout, date=history.created_date, action=history.action, action_type=history.action_type, 
                                description=history.description)
            account.add()
            self.current.append(account)

    def filter_history(self, text):
        self.system.filter(text)

    def clear_layout(self):
        for history in self.current:
            history.delete()
        self.current = []


def clearLayout(layout):
  while layout.count():
    child = layout.takeAt(0)
    if child.widget():
      child.widget().deleteLater()

class HistoryItem(QWidget):
    def __init__(self, id, history_system, lay: QVBoxLayout, date, action, action_type, description):
        super(HistoryItem, self).__init__()
        self.id = id
        self.history_system = history_system
        self.layout = lay
        self.wid = Ui_history_form()
        self.wid.setupUi(self)
        self.wid.date_label.setText(date.strftime("%m/%d/%Y, %H:%M:%S"))
        self.wid.type_label.setText(action)
        self.wid.action_label.setText(action_type)
        self.wid.description_label.setText(description)
        self.wid.option_btn.clicked.connect(self.option)

    def option(self):
        menu = QMenu()
        self.info = QAction('Info', self)
        self.info.setData('Info')
        self.info.triggered.connect(self.more_info)
        self.delete_action = QAction('Delete', self)
        self.delete_action.setData('Delete')
        self.delete_action.triggered.connect(self.delete)
        #TODO: delete from database
        menu.addAction(self.info)
        menu.addAction(self.delete_action)
        menu.exec(QCursor.pos())

    def more_info(self):
        print("More info")

    def add(self):
        self.layout.insertWidget(0,self)

    def delete(self):
        self.layout.removeWidget(self)
        self.history_system.delete(self.id)
        self.deleteLater()