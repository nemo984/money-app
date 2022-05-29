
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
        self.history_system.add_create("Reminder", f"A new reminder for '{budget.name}' budget is created", 
        f"A new reminder for '{budget.name}' budget is created. Budget '{budget.name}' hits {int(budget.progress_value)}%. The budget is for the {budget.category} category. The total budget is {budget.amount} and the amount used is {budget.amount_used}")
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
        self.history_system.add_delete("Reminder", f"You deleted a reminder for '{reminder.budget.name}'", 
        f"You deleted a reminder for '{reminder.budget.name}' that have category={reminder.budget.category}, amount={reminder.budget.amount}, start date={reminder.budget.start_date}, end date={reminder.budget.end_date}")
        reminder.delete_instance()
        self.get()

    def remove_budget(self, budget):
        q = (Reminder
                .update({Reminder.budget: None})
                .where(Reminder.budget == budget))
        q.execute()