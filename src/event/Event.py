# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from abc import ABC, abstractmethod
from random import random
from ..CONSTANTS import *

# Interface for event classes
class Event(ABC):
    def __init__(self):
        self.asigned_vehicles = []
        self.location = [
            random() * SIMULATION_WIDTH + SIMULATION_AREA_X[0],
            random() * SIMULATION_HEIGHT + SIMULATION_AREA_Y[0]
        ]

    # Method for handling event
    @abstractmethod
    def handle(self):
        pass