from abc import ABC, abstractmethod

# Interface for iterator classes
class Iterator(ABC):
    # Method for handling iteration
    @abstractmethod
    def next(self):
        pass

    # Method for checking if iteration is complete
    @abstractmethod
    def has_next(self):
        pass