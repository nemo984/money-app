from typing import List
from .model import ActionHistory, Account
from .helpers import Observable

class HistorySystem(Observable):
    def __init__(self, owner: Account):
        super().__init__()
        self.owner = owner
        self._history = []

    def add(
        self,
        action: str,
        action_type: str,
        description: str
    ) -> ActionHistory:
        history = ActionHistory(owner=self.owner, action=action, action_type=action_type, description=description)
        history.save()
        self._history.append(history)
        self.notify(self._history)
        return history

    def get(self) -> List[ActionHistory]:
        self._history = list(self.owner.history)
        self.notify(self._history)
        return self._history

    def getByType(self, typeStr:str):
        histories = ActionHistory.select().where(ActionHistory.action == typeStr)
        return list(histories)


    def filter(self, query: str):
        if query == "":
            return self.get()

        filtered_history = []
        for history in self._history:
            date = history.created_date.strftime("%m/%d/%Y, %H:%M:%S")
            s = f"{date}{history.action}{history.action_type}{history.description}"
            if query in s:
                filtered_history.append(history)
        self.notify(filtered_history)
        return filtered_history

    def delete(self, history_id):
        history = ActionHistory.get(ActionHistory.id == history_id)
        history.delete_instance()
        self.get()
