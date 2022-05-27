
from typing import List
from .helpers import Observable
from .model import Reminder, Account


class ReminderSystem(Observable):
    def __init__(self, owner):
        super().__init__()
        self._reminders = []
        self.owner = owner

    def add(
        self,
        heading: str,
        message: str,
    ) -> Reminder:
        reminder = Reminder(owner=self.owner, heading=heading, message=message)
        reminder.save()
        self._reminders.append(reminder)
        self.notify(self._reminders)
        return reminder

    def get(self) -> List[Reminder]:
        self._reminders = list(self.owner.reminders_ordered)
        self.notify(self._reminders)
        return self._reminders

    def getByID(self, reminder_id) -> Reminder:
        reminder = Reminder.get_or_none(Reminder.id == reminder_id)
        return reminder


    def update(self, reminder_id) -> Reminder:
        reminder = self.getByID(reminder_id)
        if reminder is not None:
            return
        reminder.read = True
        reminder.save()
        self.get()
        return reminder
