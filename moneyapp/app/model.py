from datetime import datetime, timedelta, date
from peewee import *
from playhouse.shortcuts import model_to_dict

database = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = database

class Account(BaseModel):
    name = CharField(unique=True)
    profile_image = BlobField(null=True)
    created_date = DateTimeField(default=datetime.now)

    @property
    def expenses_ordered(self):
        return self.expenses.order_by(Expense.created_date.desc())

    @property
    def budgets_ordered(self):
        return self.budgets.order_by(Budget.created_date.desc())

    @property
    def incomes_ordered(self):
        return self.incomes.order_by(Income.created_date.desc())

    @property
    def reminders_ordered(self):
        return self.reminders.order_by(Reminder.created_date.desc())

class Category(BaseModel):
    name = CharField(unique=True, max_length=20)
    logo = BlobField(null=True)

class Expense(BaseModel):
    owner = ForeignKeyField(Account, backref = 'expenses')
    category = ForeignKeyField(Category)
    amount = DecimalField(14,2)
    frequency_day = IntegerField(null=True)
    note = TextField(null=True)
    created_date = DateTimeField(default=datetime.now)

class Budget(BaseModel):
    owner = ForeignKeyField(Account, backref='budgets')
    category = ForeignKeyField(Category)
    amount = DecimalField(14,2)
    note = TextField(null=True)
    created_date = DateTimeField(default=datetime.now)
    end_date = DateTimeField(null=True)

class IncomeCategory(BaseModel):
    name = CharField(unique=True, max_length=20)
    logo = BlobField(null=True)

class Income(BaseModel):
    owner = ForeignKeyField(Account, backref='incomes')
    category = ForeignKeyField(IncomeCategory)
    amount = DecimalField(14,2)
    frequency_day = IntegerField(null=True)
    note = TextField(null=True)
    created_date = DateTimeField(default=datetime.now)

class Reminder(BaseModel):
    owner = ForeignKeyField(Account, backref='reminders')
    heading = CharField(max_length=50)
    message = CharField()
    read = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.now)

# if config.config['testing']:
    database.init(':memory:')
# else:
# database.init('local.db')

database.create_tables([Account, Category, Expense, Budget, IncomeCategory, Income, Reminder])
