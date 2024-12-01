# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from abc import ABC, abstractmethod

# Interface for state classes
class State(ABC):
    # Method for handling state change
    @abstractmethod
    def handle(self, vehicle, event):
        pass
