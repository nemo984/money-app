
from typing import List
from .helpers import Observable
from .model import Reminder, Account


class ReminderSystem(Observable):
    def __init__(self, owner, history_system):
        super().__init__()
        self._reminders = []
        self.owner = owner
        self.history_system = history_system

    def add(
        self,
        heading: str,
        message: str,
        budget,
    ) -> Reminder:
        if self.exists(heading, message):
            return
        reminder = Reminder(owner=self.owner, heading=heading, message=message, budget=budget)
        reminder.save()
        self._reminders.append(reminder)
        self.notify(self._reminders)
        return reminder

    def exists(self, heading, message) -> bool:
        reminder = Reminder.get_or_none(Reminder.heading == heading, Reminder.message == message)
        return reminder is not None

    def get(self) -> List[Reminder]:
        self._reminders = list(self.owner.reminders_ordered)
        self.notify(self._reminders)
        return self._reminders

    def getByID(self, reminder_id) -> Reminder:
        reminder = Reminder.get_or_none(Reminder.id == reminder_id)
        return reminder

    def update(self, reminder_id) -> Reminder:
        reminder = self.getByID(reminder_id)
        if reminder is None:
            return
        reminder.read = True
        reminder.save()
        self.get()
        return reminder

    def delete(self, reminder_id):
        reminder = self.getByID(reminder_id)
        if reminder is None:
            return
        reminder.delete_instance()
        self.get()
