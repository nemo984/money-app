from account_ui import *
from Main import BudgetItem, MainWindow
from account_wid import Ui_account_form
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PySide6.QtWidgets import QDialog, QMessageBox
from typing import List
import sys
import os
import pickle

def load_id():
    try:
        with open('signin.pickle', 'rb') as f:
            return pickle.load(f) 
    except FileNotFoundError:
        save_staySignIn(False, -1, -1)
        return [False, -1, -1]

def save_staySignIn(account_id: int, last_tab: int, staySignInChecked: bool = None):
    staySignInChecked = load_id()[0] if staySignInChecked is None else staySignInChecked
    with open('signin.pickle', 'wb') as fobj:
        pickle.dump([staySignInChecked, account_id, last_tab], fobj)

class AccountWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.create_btn.clicked.connect(self.create_tab)
        self.ui.back_btn.clicked.connect(self.login_tab)
        self.ui.upload_btn.clicked.connect(self.upload_pic)
        self.ui.create_btn_2.clicked.connect(self.create_account)
        self.imageFilePath = None
        if self.staySignIn():
            return
        self.load_accounts()
        self.show()

    def staySignIn(self):
        staySignInChecked, account_id, last_tab = load_id()
        print(load_id())
        if not staySignInChecked:
            return False
        self.ui.staySignIn_checkBox.setChecked(True)
        if account_id == -1:
            return False
        #TODO: pass in with account_id, last_tab
        self.dialog = MainWindow(self)
        self.dialog.show()
        self.hide()
        return True

    def load_accounts(self):
        #mock accounts
        for i in range(5):
            item = QListWidgetItem()
            account = AccountItem(i, "Johnny Rol", "5/2/5", str(i), os.getcwd() + "/rabbit.png")
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
        self.login_pop = LoginPopUp(account, self.ui.staySignIn_checkBox.isChecked(), self)
        self.login_pop.show()

    def upload_pic(self):
        root = Tk()
        root.withdraw()
        self.imageFilePath = askopenfilename(title="Choose a Picture", filetypes=[('image files', ('.png', '.jpg'))])
        root.update()
        root.destroy()
        self.ui.profile_label.setPixmap(QPixmap(self.imageFilePath))

    def create_account(self):
        name = self.ui.name_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        passwordConfirm = self.ui.passwordConfirm_lineEdit.text()
        if not (name and password and passwordConfirm):
            self.ui.warning_label.setText("Please fill in all the fields")
            return
        
        if password != passwordConfirm:
            self.ui.warning_label.setText("Passwords do not match")
            return

        #createdAccount = self.system.create_account()
        #use account details from the createdAccount
        accountItem = AccountItem(11, name, password, password, self.imageFilePath)
        self.add_account(accountItem)
        self.login_tab()

        self.ui.name_lineEdit.setText("")
        self.ui.password_lineEdit.setText("")
        self.ui.passwordConfirm_lineEdit.setText("")
        self.imageFilePath = ""
        self.ui.profile_label.setPixmap(QPixmap())

class AccountItem(QWidget):
    def __init__(self, id, name, last_login, hash_pwd, imageFilePath = None):
        super(AccountItem, self).__init__()
        self.id = id
        self.hash_pwd = hash_pwd
        self.wid = Ui_account_form()
        self.wid.setupUi(self)
        self.wid.name_label.setText(name)
        self.wid.date_label.setText(last_login)
        if imageFilePath is not None:
            self.wid.profile_label.setPixmap(QPixmap(imageFilePath))

    def get_id(self):
        return self.id
    
    def login(self, password) -> bool:
        #hash the given pwd
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
            save_staySignIn(self.account.id, -1, self.stayLoggedIn)
            #also pass in the account details
            self.dialog = MainWindow(self.parent)
            self.dialog.show()
            self.hide()
            self.parent.hide()
        else:
            QMessageBox.warning(
                self, 'Error', 'Incorrect password')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #call when user logs out of an account
    #save_staySignIn(-1, -1)
    
    window = AccountWindow()
    window.show()
    sys.exit(app.exec_())