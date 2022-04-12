
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
        message: str,
    ) -> Reminder:
        reminder = Reminder(owner=owner, heading=heading, message=message)
        reminder.save()
        self._reminders.append(reminder)
        print("Reminder updated: Notifying observers")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
        self.notify(self._reminders)
        return reminder

    def get(self, account: Account) -> List[Reminder]:
        self._reminders = list(account.reminders_ordered)
        self.notify(self._reminders)
        return self._reminders

    def read(self, reminder: Reminder) -> Reminder:
        owner = reminder.owner
        reminder.read = True
        reminder.save()
        self.get(owner)
        return reminder
