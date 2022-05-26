from PySide6.QtWidgets import *
import sys
import os
from moneyapp import AccountWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountWindow()
    sys.exit(app.exec_())
