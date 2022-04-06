from ..app.helpers import Observer

class IncomeUI(Observer):
    def update(self, subject):
        print("new incomes update")