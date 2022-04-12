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
        profile_image_path: Optional[str] = None
    ) -> Account:
        image = None
        if profile_image_path:
            with open(profile_image_path, 'rb') as file:
                image = file.read()

        account = Account(name=name, profile_image=image)
        account.save()
        self._accounts.append(account)
        self.notify(self._accounts)
        return account

    def get(self) -> List[Account]:
        self._accounts = list(Account.select())
        self.notify(self._accounts)
        return self._accounts

    def update(
        self,
        account: Account,
        name: Optional[str],
        profile_image_path: Optional[str] = None
    ) -> Account:
        if name:
            account.name = name
        if profile_image_path:
            with open(profile_image_path, 'rb') as file:
                account.profile_image = file.read()
        account.save()
        self.get()
        return account

    def delete(self, account: Account):
        account.delete_instance()
        self.get()
    