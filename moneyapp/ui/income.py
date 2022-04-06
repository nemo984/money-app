from ..app.helpers import Observer
from ..app.model import *
from typing import List
import asyncio
import time

class IncomeUI(Observer):
    async def update(self, incomes: List[Income]):
        await asyncio.sleep(3)

        print("Incomes updated: Updating income page UI")
        for income in incomes:
            print(f"{income.created_date} {income.owner} {income.category} {income.amount} {income.frequency_day} {income.note}")
        print("================")