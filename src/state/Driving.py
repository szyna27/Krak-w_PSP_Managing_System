from .State import State
from time import sleep
from random import random

# Class definition
class Driving(State):
    # Method for handling state change
    def handle(self, vehicle, event):
        sleep(random() * 3)
        if event.is_true():
            vehicle.set_busy()
        else:
            vehicle.set_returning()
    
    def is_available(self):
        return False
    
    def __str__(self):
        return "Driving"