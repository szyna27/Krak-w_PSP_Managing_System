# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from abc import ABC, abstractmethod

# Interface for strategy classes
class Strategy(ABC):
    # Method for handling strategy
    @abstractmethod
    def execute(self):
        pass