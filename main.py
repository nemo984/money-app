from moneyapp.ui import income, overview
from moneyapp.app.income_system import *
import time

icis = IncomeSystem()
i = income.IncomeUI()
ireport = overview.IncomeReportUI()

icis.add_observer(i)
icis.add_observer(ireport)


def addSomeIncomes():
    account = Account(name="John")
    account.save()
    c = IncomeCategory.create(name="Passive-Income")
    for i in range(5):
        icis.add(account, c, 1000 * i + i * 0.64)
        time.sleep(5)

def getIncomes():
    account = Account.get(Account.name == "John")
    icis.get(account)

addSomeIncomes()