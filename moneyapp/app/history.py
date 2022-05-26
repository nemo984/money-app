from typing import List
from .model import ActionHistory, Account
from .helpers import Observable

class HistorySystem(Observable):
    def __init__(self):
        super().__init__()
        self._history = []

    def add(
        self,
        owner: Account,
        action: str,
        action_type: str,
        description: str
    ) -> ActionHistory:
        history = ActionHistory(owner=owner, action=action, action_type=action_type, description=description)
        history.save()
        self._history.append(history)
        self.notify(self._history)
        return history

    def get(self, owner: Account) -> List[ActionHistory]:
        if not self._history:
            self._history = list(owner.history)
        return self._history

    def filter(self, query: str):
        filtered_history = []
        for history in self._history:
            s = f"{history.created_date}{history.action}{history.action_type}{history.description}"
            if query in s:
                filtered_history.append(history)
        return filtered_history