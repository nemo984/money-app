import abc

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, subject):
        pass

class Observable:
    def __init__(self):
        self._observers = []
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def add_observer(self, observer : Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer : Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

