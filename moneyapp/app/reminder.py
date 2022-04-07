
from typing import List
from .helpers import Observable
from .model import *


class ReminderSystem(Observable):
    def __init__(self):
        super().__init__()
        self._reminders = []

    def add(
        self,
        owner: Account,
        heading: str,
        body: str,
    ):
        reminder = Reminder(account=owner, heading=heading, body=body)
        reminder.save()
        self._reminders.append(reminder)
        print("Reminder updated: Notifying observers")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
        self.notify(self._reminders)

    def get(self, account: Account) -> List[Reminder]:
        self._reminders = account.reminders_ordered
        self.notify(self._reminders)
        return self._reminders
