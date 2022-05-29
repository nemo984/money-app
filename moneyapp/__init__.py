from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from .app.budget_system import BudgetSystem
from .app.income_system import IncomeSystem
from .app.expense_system import ExpenseSystem
from .app.history import HistorySystem
from .app.reminder import ReminderSystem
from .ui import MoneyAppUI
from .ui.uipy.account import Ui_MainWindow
from .ui.uipy.account_wid import Ui_account_form
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PySide6.QtWidgets import QDialog, QMessageBox
from typing import List
import sys
import os
import pickle
from .app.account import AccountSystem


class MainApp:
    def __init__(self, account_id=None, parent=None):
        self.parent = parent
        self.account_system = AccountSystem()
        account = self.account_system.getByID(account_id)
        self.history_system = HistorySystem(owner=account)
        self.reminder_system = ReminderSystem(
            owner=account, history_system=self.history_system)
        self.income_system = IncomeSystem(
            owner=account, history_system=self.history_system)
        self.expense_system_budget = ExpenseSystem(account)
        self.budget_system = BudgetSystem(
            owner=account, reminder_system=self.reminder_system, expense_system=self.expense_system_budget, history_system=self.history_system)
        self.expense_system = ExpenseSystem(owner=account, budget_system=self.budget_system, history_system=self.history_system)
        self.ui = MoneyAppUI(account, self.income_system, self.budget_system, self.expense_system,
                             self.history_system, self.account_system, self.reminder_system, self.expense_system_budget)

    def show(self):
        self.ui.show()

class AccountWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.create_btn.clicked.connect(self.create_tab)
        self.ui.back_btn.clicked.connect(self.login_tab)
        self.ui.upload_btn.clicked.connect(self.upload_pic)
        self.ui.create_btn_2.clicked.connect(self.create_account)
        self.system = AccountSystem()
        self.imageFilePath = None
        if self.staySignIn():
            return

        self.load_accounts()
        self.show()

    def staySignIn(self):
        d = load_id()
        account_id = d[_account_id]
        staySignInChecked = d[_staySignInChecked]
        if not d[_staySignInChecked]:
            return False
        self.ui.staySignIn_checkBox.setChecked(True)
        if account_id == -1:
            return False
        self.dialog = MainApp(account_id=account_id, parent=self)
        self.dialog.show()
        self.hide()
        return True

    def load_accounts(self):
        accounts = self.system.get()
        for acc in accounts:
            item = QListWidgetItem()
            account = AccountItem(id=acc.id, name=acc.name, created_date=acc.created_date, last_login=acc.created_date,
                                  hash_pwd=acc.password, imageBlob=acc.profile_image)
            item.setSizeHint(account.size())
            self.ui.account_listWidget.addItem(item)
            self.ui.account_listWidget.setItemWidget(item, account)

    def add_account(self, account):
        item = QListWidgetItem()
        item.setSizeHint(account.size())
        self.ui.account_listWidget.addItem(item)
        self.ui.account_listWidget.setItemWidget(item, account)

    def login_tab(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def create_tab(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def login(self):
        items = self.ui.account_listWidget.selectedItems()
        if not items:
            return
        account = self.ui.account_listWidget.itemWidget(items[0])
        self.login_pop = LoginPopUp(
            account, self.ui.staySignIn_checkBox.isChecked(), self)
        self.login_pop.setWindowTitle("Enter Password")
        self.login_pop.show()

    def upload_pic(self):
        root = Tk()
        root.withdraw()
        self.imageFilePath = askopenfilename(title="Choose a Picture", filetypes=[
                                             ('image files', ('.png', '.jpg'))])
        root.update()
        root.destroy()
        self.ui.profile_label.setPixmap(QPixmap(self.imageFilePath))

    def create_account(self):
        if len(self.ui.name_lineEdit.text()) > 26:
            self.ui.warning_label.setText(
                "Password should shorter than 26 character")
            return
        name = self.ui.name_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        passwordConfirm = self.ui.passwordConfirm_lineEdit.text()
        if not (name and password and passwordConfirm):
            self.ui.warning_label.setText("Please fill in all the fields")
            return

        if password != passwordConfirm:
            self.ui.warning_label.setText("Passwords do not match")
            return

        createdAccount = self.system.add(
            name=name, password=password, profile_image_path=self.imageFilePath)
        accountItem = AccountItem(id=createdAccount.id, name=name, created_date=createdAccount.created_date, last_login=createdAccount.created_date,
                                  hash_pwd=createdAccount.password, imageFilePath=self.imageFilePath)
        self.add_account(accountItem)
        self.login_tab()

        self.ui.name_lineEdit.setText("")
        self.ui.password_lineEdit.setText("")
        self.ui.passwordConfirm_lineEdit.setText("")
        self.imageFilePath = ""
        self.ui.profile_label.setPixmap(QPixmap())


class AccountItem(QWidget):
    def __init__(self, id, name, created_date, last_login, hash_pwd, imageFilePath=None, imageBlob=None):
        super(AccountItem, self).__init__()
        self.id = id
        self.hash_pwd = hash_pwd
        self.wid = Ui_account_form()
        self.wid.setupUi(self)
        self.wid.name_label.setText(name)
        self.wid.last_login_label.setText(
            created_date.strftime("%m/%d/%Y, %H:%M:%S"))
        self.wid.created_date_label.setText(
            last_login.strftime("%m/%d/%Y, %H:%M:%S"))
        if imageFilePath is not None:
            self.wid.profile_label.setPixmap(QPixmap(imageFilePath))
        if imageBlob is not None:
            qimg = QImage.fromData(imageBlob)
            pixmap = QPixmap.fromImage(qimg)
            self.wid.profile_label.setPixmap(pixmap)

    def get_id(self):
        return self.id

    def login(self, password) -> bool:
        return self.hash_pwd == password


class LoginPopUp(QDialog):
    def __init__(self, account: AccountItem, stayLoggedIn: bool, parent=None):
        super(LoginPopUp, self).__init__(parent)
        self.parent = parent
        self.account = account
        self.stayLoggedIn = stayLoggedIn
        self.pwd_lineEdit = QLineEdit(self)
        self.pwd_lineEdit.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QVBoxLayout(self)
        layout.addWidget(self.pwd_lineEdit)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if self.account.login(self.pwd_lineEdit.text().strip()):
            save_staySignIn(account_id=self.account.id,
                            last_tab=-1, staySignInChecked=self.stayLoggedIn)
            self.dialog = MainApp(account_id=self.account.id, parent=self)
            self.dialog.show()
            self.hide()
            self.parent.hide()
        else:
            QMessageBox.warning(
                self, 'Error', 'Incorrect password')


_staySignInChecked = "staySignInChecked"
_account_id = "account_id"
_last_tab = "last_tab"


def load_id():
    try:
        with open('signin.pickle', 'rb') as f:
            d = pickle.load(f)
            AccountSystem().getByID(d[_account_id])
            return d
    except Exception:
        save_staySignIn()
        return {_staySignInChecked: False, _account_id: -1, _last_tab: -1}


def save_staySignIn(staySignInChecked: bool = False, account_id: int = -1, last_tab: int = -1):
    staySignInChecked = load_id(
    )[0] if staySignInChecked is None else staySignInChecked
    with open('signin.pickle', 'wb') as fobj:
        d = {_staySignInChecked: staySignInChecked,
             _account_id: account_id, _last_tab: last_tab}
        pickle.dump(d, fobj)
