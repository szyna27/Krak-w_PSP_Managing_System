from .State import State
from time import sleep
from random import random

# Class definition
class Busy(State):
    # Method for handling state change
    def handle(self, vehicle, event):
        sleep(5 + random() * 20)
        event.handled = True
        vehicle.set_returning()

    def is_available(self):
        return False
        
    def __str__(self):
        return "Busy"