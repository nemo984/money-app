from typing import List
from ..app.helpers import Observer
from ..app.model import Income
from ..app.income_system import IncomeSystem


class IncomeUI(Observer):
    
    def __init__(self, ui, s: IncomeSystem):
        self.ui = 0
        self.system = s


    # Income: 100 / frequency_day
    # Every 10 day -> (100 * 10) / frequency_day 

    # Problem: Show income history every month
    # 1. User add the first income with amount = 20000, frequency = 28 - January
    # 2. User add the second income with amount = 1500, frequency = 7 - January
    # 3. User edited the first income to amount = 36000 - March

    # Problem: Show income history every month
    # 1. User add the first income with amount = 20000, frequency = 28 - January
    # 2. User add the second income with amount = 1500, frequency = 7 - Feb
    # 3. User edited the first income to amount = 36000 - March

    # Problem: Show income history every month
    # 1. User add the first income with amount = 20000, frequency = 28 - Feb
    # 2. User add the second income with amount = 1500, frequency = 7 - Feb
    # 3. User edited the first income to amount = 36000 - March

    # January, 26000
    # Feb, 26000
    # March, 42000

    #            create_date, amount
    # Add Income 1: January, 30000
    # Add Income 2: January, 2500
    # Add Income 3: Feb, 20000
    # incomes = [[January, 30000], [January, 2500], [Feb, 20000]]
    async def update(self, incomes: List[Income]):
        print("Incomes updated: Updating income page UI")

        n = 28
        total = 0
        for income in incomes:
            total += (income.amount * n) / income.frequency_day #Total Income per N day
    
            print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")

        # 1,.., 12
        for month in range(1, 13):
            month_total = 0
            for income in incomes:
                if income.created_date.month > month:
                    continue
                month_total += (income.amount * 28) / income.frequency_day

            print(f"Month {month} : {month_total}")
        

        # Month 1 : 32500
        # Month 2 : 52500

        print("================")
    