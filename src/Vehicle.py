# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from .state import *

# Class definition
class Vehicle:
    # Constructor
    def __init__(self):
        self.__state = Available()

    # Getters and setters
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, state):
        self.__state = state

    # Method for handling sending vehicle
    def send(self, event):
        self.__state.handle(self, event)