from typing import Optional, List
from .helpers import Observable
from .model import Account


class AccountSystem(Observable):

    def __init__(self):
        super().__init__()
        self._accounts = []

    def add(
        self,
        name: str,
        password: str,
        profile_image_path: Optional[str] = None
    ) -> Account:
        image = None
        if profile_image_path:
            with open(profile_image_path, 'rb') as file:
                image = file.read()

        account = Account(name=name, password=password, profile_image=image)
        account.save()
        self._accounts.append(account)
        self.notify(self._accounts)
        return account

    def get(self) -> List[Account]:
        self._accounts = list(Account.select())
        self.notify(self._accounts)
        return self._accounts

    def getByID(self, id) -> Account:
        return Account.get(Account.id == id)

    def update(
        self,
        account: Account,
        name: Optional[str],
        password: Optional[str],
        profile_image_path: Optional[str] = None,
        reminder_threshold1: Optional[int] = None,
        reminder_threshold2: Optional[int] = None,
    ) -> Account:
        if name:
            account.name = name
        if password:
            account.password = password
        if profile_image_path:
            with open(profile_image_path, 'rb') as file:
                account.profile_image = file.read()
        if reminder_threshold1:
            account.budget_reminder_threshold1 = reminder_threshold1
        if reminder_threshold2:
            account.budget_reminder_threshold2 = reminder_threshold2
        account.save()
        self.get()
        return account

    def delete(self, account: Account):
        account.delete_instance()
        self.get()
    