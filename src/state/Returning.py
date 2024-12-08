from .State import State
from time import sleep
from random import random

# Class definition
class Returning(State):
    # Method for handling state change
    def handle(self, vehicle, event):
        sleep(random() * 3)
        vehicle.set_available()
    
    def is_available(self):
        return False
    
    def __str__(self):
        return "Returning"