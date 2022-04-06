import abc

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, data):
        pass

class Observable:
    def __init__(self):
        self._observers = []
    
    def notify(self, data):
        for observer in self._observers:
            observer.update(data)
    
    def add_observer(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

