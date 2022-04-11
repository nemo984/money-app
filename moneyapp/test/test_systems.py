import unittest
import random
import string
import decimal
from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timedelta
from app.income_system import IncomeSystem
from app.budget_system import BudgetSystem
from app.expense_system import ExpenseSystem
from app.model import Income, Account, IncomeCategory, Expense, Category, Budget


def randomString(N):
    return ''.join(random.choices(string.ascii_uppercase, k=N))


def randomInt(N):
    return random.randrange(N)


def randomAmount():
    return decimal.Decimal(round(random.uniform(20000, 300000), 2))


def randomIncomeCategory():
    c = IncomeCategory(name=randomString(10))
    c.save()
    return c


def randomCategory():
    c = Category(name=randomString(10))
    c.save()
    return c


def randomDate(days):
    start = datetime.now()
    end = start + timedelta(days=10)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


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
            frequency = randomInt(69)
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


class TestBudgetSystem(unittest.TestCase):
    def setUp(self):
        self.system = BudgetSystem()
        self.owner = Account(name=randomString(10))
        self.owner.save()

        @dataclass
        class BudgetTestData:
            category: Category
            amount: float
            note: Optional[str] = None
            end_date: Optional[datetime] = None

        self.test_budgets = [
            BudgetTestData(randomCategory(), randomAmount()),
            BudgetTestData(randomCategory(), randomAmount(), randomString(50)),
            BudgetTestData(randomCategory(), randomAmount(),
                           randomString(50), randomDate(50)),
            BudgetTestData(randomCategory(), randomAmount(),
                           randomString(50), randomDate(50)),
            BudgetTestData(randomCategory(), randomAmount(),
                           end_date=randomDate(50)),
        ]
        self.test_add()

    def test_add(self):
        for b in self.test_budgets:
            budget = self.system.add(
                self.owner, b.category, b.amount, b.end_date, b.note)
            self.assertEqual(self.owner, budget.owner)
            self.assertEqual(b.category, budget.category)
            self.assertAlmostEqual(b.amount, budget.amount)
            self.assertEqual(b.end_date, budget.end_date)
            self.assertEqual(b.note, budget.note)

    def test_get(self):
        budgets = self.system.get(self.owner)
        self.assertEqual(len(self.test_budgets), len(budgets))

    def test_update(self):
        budgets = self.system.get(self.owner)
        for bg in budgets:
            category = randomCategory()
            amount = randomAmount()
            end_date = randomDate(100)
            note = randomString(50)
            budget = self.system.update(bg, category, amount, end_date, note)
            self.assertEqual(self.owner, budget.owner)
            self.assertAlmostEqual(amount, budget.amount)
            self.assertEqual(category.name, budget.category.name)
            self.assertEqual(note, budget.note)
            self.assertEqual(end_date, budget.end_date)

    def test_delete(self):
        budgets = self.system.get(self.owner)
        for bg in budgets:
            self.system.delete(bg)
        budgetsAfter = self.system.get(self.owner)
        self.assertEqual(len(budgetsAfter), 0)


class TestExpenseSystem(unittest.TestCase):
    def setUp(self):
        self.system = ExpenseSystem()
        self.owner = Account(name=randomString(10))
        self.owner.save()

        @dataclass
        class ExpenseTestData:
            category: Category
            amount: float
            frequency: Optional[int] = None
            note: Optional[str] = None

        self.test_expenses = [
            ExpenseTestData(randomCategory(), randomAmount()),
            ExpenseTestData(randomCategory(), randomAmount(), randomInt(50)),
            ExpenseTestData(randomCategory(), randomAmount(),
                            randomInt(50), randomString(50)),
            ExpenseTestData(randomCategory(), randomAmount(),
                            randomInt(50), randomString(50)),
            ExpenseTestData(randomCategory(), randomAmount(),
                            note=randomString(50))
        ]
        self.test_add()

    def test_add(self):
        for e in self.test_expenses:
            expense = self.system.add(
                self.owner, e.category, e.amount, e.frequency, e.note)
            self.assertEqual(self.owner, expense.owner)
            self.assertEqual(e.category, expense.category)
            self.assertEqual(e.frequency, expense.frequency_day)
            self.assertAlmostEqual(e.amount, expense.amount)
            self.assertEqual(e.note, expense.note)

    def test_get(self):
        expenses = self.system.get(self.owner)
        self.assertEqual(len(self.test_expenses), len(expenses))

    def test_update(self):
        expenses = self.system.get(self.owner)
        for e in expenses:
            category = randomCategory()
            amount = randomAmount()
            frequency = randomInt(100)
            note = randomString(50)
            expense = self.system.update(e, category, amount, frequency, note)
            self.assertEqual(self.owner, expense.owner)
            self.assertEqual(category, expense.category)
            self.assertEqual(frequency, expense.frequency_day)
            self.assertAlmostEqual(amount, expense.amount)
            self.assertEqual(note, expense.note)

    def test_delete(self):
        expenses = self.system.get(self.owner)
        for e in expenses:
            self.system.delete(e)
        expensesAfter = self.system.get(self.owner)
        self.assertEqual(len(expensesAfter), 0)


if __name__ == "__main__":
    unittest.main()
