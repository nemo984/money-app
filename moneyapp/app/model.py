from datetime import datetime, timedelta, date
from peewee import *
from playhouse.shortcuts import model_to_dict

database = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = database

class Account(BaseModel):
    name = CharField()
    password = CharField(max_length=30)
    profile_image = BlobField(null=True)
    created_date = DateTimeField(default=datetime.now)
    budget_reminder_threshold1 = IntegerField(default=50)
    budget_reminder_threshold2 = IntegerField(default=80)
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

class Budget(BaseModel):
    owner = ForeignKeyField(Account, backref='budgets',  on_delete="CASCADE")
    name = CharField()
    category = CharField()
    amount = DecimalField(14,2)
    amount_used = DecimalField(14, 2, default=0)
    note = TextField(null=True)
    start_date = DateTimeField(default=datetime.now)
    end_date = DateTimeField(null=True)

    @property
    def progress_value(self):
        return (self.amount_used / self.amount) * 100

class Expense(BaseModel):
    owner = ForeignKeyField(Account, backref = 'expenses', on_delete="CASCADE")
    budget = ForeignKeyField(Budget, backref='expenses', null=True, on_delete='SET NULL')
    category = CharField()
    amount = DecimalField(14,2)
    note = TextField(null=True)
    date = DateTimeField(default=datetime.now)

class Income(BaseModel):
    owner = ForeignKeyField(Account, backref='incomes', on_delete="CASCADE")
    name = CharField()
    category = CharField()
    amount = DecimalField(14,2)
    recurrence = CharField(null=True)
    note = TextField(null=True)
    date = DateTimeField(default=datetime.now)
    updated_date = DateTimeField(null=True)

class Reminder(BaseModel):
    owner = ForeignKeyField(Account, backref='reminders', on_delete="CASCADE")
    budget = ForeignKeyField(Budget, backref='reminders', on_delete='SET NULL', null=True)
    heading = CharField(max_length=50)
    message = CharField()
    read = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.now)

class AccountMonthlyIncome(BaseModel):
    owner = ForeignKeyField(Account, backref='monthly_incomes', on_delete="CASCADE")
    amount = DecimalField(14,2)
    month = IntegerField()

class ActionHistory(BaseModel):
    owner = ForeignKeyField(Account, backref='history', on_delete="CASCADE")
    created_date = DateTimeField(default=datetime.now)
    action_type = CharField()
    action = CharField(max_length=20)
    brief_description = CharField()    
    long_description = CharField(null=True)    

# if config.config['testing']:
    # database.init(':memory:')
# else:
database.init('local2.db')

database.create_tables([Account, Expense, Budget, Income, Reminder, ActionHistory])
