import unittest
import random
import string
import decimal
from dataclasses import dataclass
from typing import Optional
from app.income_system import IncomeSystem
from app.model import Income, Account, IncomeCategory


def randomString(N):
    return ''.join(random.choices(string.ascii_uppercase, k=N))


def randomAmount():
    return decimal.Decimal(round(random.uniform(20000, 300000), 2))


def randomIncomeCategory():
    c = IncomeCategory(name=randomString(10))
    c.save()
    return c


class TestIncomeSystem(unittest.TestCase):

    def setUp(self):
        self.system = IncomeSystem()
        self.owner = Account(name=randomString(10))
        self.owner.save()
        self.income_category = randomIncomeCategory()
        self.income_category.save()

        @dataclass
        class IncomeTestData:
            amount: float
            note: Optional[str] = None
            frequency: Optional[int] = None
        self.test_incomes = [
            IncomeTestData(100, "Note"),
            IncomeTestData(140, "Another One", 21),
            IncomeTestData(501),
            IncomeTestData(404, "Not Found Income", 30),
            IncomeTestData(140.131114, "My Weekly Revenue for sleeping", 7),
        ]
        self.test_add()

    def tearDown(self):
        pass

    def test_add(self):
        for i in self.test_incomes:
            income = self.system.add(
                self.owner, self.income_category, i.amount, i.note, i.frequency)
            self.assertEqual(self.owner, income.owner)
            self.assertEqual(self.income_category, income.category)
            self.assertAlmostEqual(i.amount, income.amount)
            self.assertEqual(i.note, income.note)
            self.assertEqual(i.frequency, income.frequency_day)

    def test_get(self):
        incomes = self.system.get(self.owner)
        self.assertEqual(len(self.test_incomes), len(incomes))

    def test_update(self):
        incomes = self.system.get(self.owner)
        for ic in incomes:
            category = randomIncomeCategory()
            amount = randomAmount()
            note = randomString(50)
            frequency = random.randrange(69)
            income = self.system.update(
                income=ic, category=category, amount=amount, frequency=frequency, note=note)
            self.assertEqual(self.owner, income.owner)
            self.assertAlmostEqual(amount, income.amount)
            self.assertEqual(category.name, income.category.name)
            self.assertEqual(note, income.note)
            self.assertEqual(frequency, income.frequency_day)

    def test_delete(self):
        incomes = self.system.get(self.owner)
        for ic in incomes:
            self.system.delete(ic)
        incomes2 = self.system.get(self.owner)
        self.assertEqual(len(incomes2), 0)


if __name__ == "__main__":
    unittest.main()
