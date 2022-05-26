from datetime import datetime, timedelta, date
from peewee import *
from playhouse.shortcuts import model_to_dict

database = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = database

class Account(BaseModel):
    name = CharField(unique=True)
    password = CharField(max_length=30)
    profile_image = BlobField(null=True)
    created_date = DateTimeField(default=datetime.now)

    @property
    def expenses_ordered(self):
        return self.expenses.order_by(Expense.date.desc())

    @property
    def budgets_ordered(self):
        return self.budgets.order_by(Budget.start_date.desc())

    @property
    def incomes_ordered(self):
        return self.incomes.order_by(Income.date.desc())

    @property
    def reminders_ordered(self):
        return self.reminders.order_by(Reminder.created_date.desc())

class Expense(BaseModel):
    owner = ForeignKeyField(Account, backref = 'expenses')
    budget = ForeignKeyField(Account, backref='expenses')
    category = CharField()
    amount = DecimalField(14,2)
    note = TextField(null=True)
    date = DateTimeField(default=datetime.now)

class Budget(BaseModel):
    owner = ForeignKeyField(Account, backref='budgets')
    category = CharField()
    amount = DecimalField(14,2)
    note = TextField(null=True)
    start_date = DateTimeField(default=datetime.now)
    end_date = DateTimeField(null=True)

class Income(BaseModel):
    owner = ForeignKeyField(Account, backref='incomes')
    name = CharField()
    category = CharField()
    amount = DecimalField(14,2)
    frequency_day = IntegerField(null=True)
    note = TextField(null=True)
    date = DateTimeField(default=datetime.now)
    updated_date = DateTimeField()

class Reminder(BaseModel):
    owner = ForeignKeyField(Account, backref='reminders')
    heading = CharField(max_length=50)
    message = CharField()
    read = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.now)

class AccountMonthlyIncome(BaseModel):
    owner = ForeignKeyField(Account, backref='monthly_incomes')
    amount = DecimalField(14,2)
    month = IntegerField()

class ActionHistory(BaseModel):
    owner = ForeignKeyField(Account, backref='history')
    created_date = DateTimeField(default=datetime.now)
    action_type = CharField()
    action = CharField(max_length=20)
    description = CharField(max_length=70)    

# if config.config['testing']:
    # database.init(':memory:')
# else:
database.init('local2.db')

database.create_tables([Account, Expense, Budget, Income, Reminder, ActionHistory])
