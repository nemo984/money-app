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

        
    async def update(self, histories):
        for history in histories:
            item = QListWidgetItem()
            account = HistoryItem(lay=self.ui.self.verticalLayout_39 ,date=history.created_date, action=history.action, action_type=history.action_type, 
                                description=history.description)
            item.setSizeHint(account.size())
            self.ui.account_listWidget.addItem(item)
            self.ui.account_listWidget.setItemWidget(item, account)

    def filter(self):
        pass


class HistoryItem(QWidget):
    def __init__(self, lay: QVBoxLayout, date, action, action_type, description):
        super(HistoryItem, self).__init__()
        self.layout = lay
        self.wid = Ui_history_form()
        self.wid.setupUi(self)
        self.wid.date_label.setText(date)
        self.wid.action_label.setText(action)
        self.wid.action_type_label.setText(action_type)
        self.wid.description_label.setText(description)

    def option(self):
        menu = QMenu()
        Edit = menu.addAction('Edit')
        delete = menu.addAction('Delete')
        menu.exec(QCursor.pos())

    def add(self):
        self.layout.insertWidget(0,self)

    def delete(self):
        self.layout.removeWidget(self)
        self.deleteLater()