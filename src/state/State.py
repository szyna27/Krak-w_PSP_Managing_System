from abc import ABC, abstractmethod

# Interface for state classes
class State(ABC):
    # Method for handling state change
    @abstractmethod
    def handle(self, vehicle, event):
        pass

    @abstractmethod
    def is_available(self):
        pass

    @abstractmethod
    def __str__(self):
        pass