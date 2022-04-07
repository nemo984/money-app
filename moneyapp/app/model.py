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
    body = CharField()
    read = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.now)

# if config.config['testing']:
    database.init(':memory:')
# else:
# database.init('local.db')

database.create_tables([Account, Category, Expense, Budget, IncomeCategory, Income, Reminder])

# #TODO: move somewhere else and do proper test? how to do
# #for formatting output
# import pprint
# pp = pprint.PrettyPrinter(depth=4)

# def test_models():
#     a1 = Account.create(name="John")
#     c = Category.create(name="Transportation") #This will be predefined?
#     c2 = Category.create(name="Shopping")
#     income_c = IncomeCategory.create(name="Full-Time Job")
#     income_c2 = IncomeCategory.create(name="Passive Income")

#     expenses = [
#         {'owner': a1, 'category': c, 'amount': 121314.23, 'note': "submarine ride to college fare", 'frequency_day': 1}, #means every 1 day frequency for this expense
#         {'owner': a1, 'category': c, 'amount': 14914, 'note': "plane back to home fare", 'frequency_day': 7},
#         {'owner': a1, 'category': c2, 'amount': 32},
#     ]
#     Expense.insert_many(expenses).execute()

#     budgets = [
#         {'owner': a1, 'category': c, 'amount': 100002320.1014, 'note': "save money with public transportation", 'end_date': date.today() + timedelta(days=30)},
#         {'owner': a1, 'category': c2, 'amount': 149, 'end_date': date.today() + timedelta(days=7)},
#     ]
#     Budget.insert_many(budgets).execute()

#     incomes = [
#         {'owner': a1, 'category': income_c, 'amount': 0.1014, 'note': "My monthly salary!", 'frequency_day': 28},
#         {'owner': a1, 'category': income_c2, 'amount': 1000000, 'frequency_day': 28},
#     ]
#     Income.insert_many(incomes).execute()

#     pp.pprint(model_to_dict(a1, backrefs=True))

# if config.config['testing']:
#     test_models()