from peewee import *

db = SqliteDatabase('money.db')

class BaseModel(Model):
    class Meta:
        database = db

class Account(BaseModel):
    name = CharField(unique=True)
    profile_image = BlobField()
    created_date = DateTimeField(default=datetime.datetime.now)

class Category(BaseModel):
    name = CharField(unique=True, max_length=20)
    logo = BlobField()

class Expense(BaseModel):
    owner = ForeignKeyField(Account, backref = 'expenses')
    category = ForeignKeyField(Category)
    amount = DecimalField(14,2)
    frequency_day = IntegerField()
    note = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)

class Budget(BaseModel):
    owner = ForeignKeyField(Account, backref='budgets')
    category = ForeignKeyField(Category)
    amount = DecimalField(14,2)
    note = TextField()
    start_date = DateTimeField(default=datetime.datetime.now)
    end_date = DateTimeField()

class IncomeCategory(BaseModel):
    name = CharField(unique=True, max_length=20)
    logo = BlobField()

class Income(BaseModel):
    owner = ForeignKeyField(Account, backref='incomes')
    category = ForeignKeyField(IncomeCategory)
    amount = DecimalField(14,2)
    frequency_day = IntegerField()
    note = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)

class Reminder(BaseModel):
    account = ForeignKeyField(Account, backref='reminders')
    heading = CharField(max_length=50)
    note = CharField()
    read = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.datetime.now)