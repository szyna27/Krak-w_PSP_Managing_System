from abc import ABC, abstractmethod
from random import random
from ..CONSTANTS import *

# Interface for event classes
class Event(ABC):
    def __init__(self, color):
        self.location = (
            random() * SIMULATION_WIDTH + SIMULATION_AREA_X[0],
            random() * SIMULATION_HEIGHT + SIMULATION_AREA_Y[0]
        )
        self.handled = False
        self.color = color
        self.color_end = "\033[0m"
        self.__is_true = True
        if random() < 0.05:
            self.__is_true = False

    def is_true(self):
        return self.__is_true
    
    @abstractmethod
    def __str__(self):
        pass