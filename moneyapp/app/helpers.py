import abc
import asyncio


class Observer(abc.ABC):
    @abc.abstractmethod
    async def update(self, data):
        pass


class Observable:
    def __init__(self):
        self._observers = []

    def notify(self, data):
        async def notify():
            await asyncio.gather(*[o.update(data) for o in self._observers])
        asyncio.run(notify())

    def add_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
