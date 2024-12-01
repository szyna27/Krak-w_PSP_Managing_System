# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from .State import State
from .Busy import Busy

# Class definition
class Available(State):
    # Method for handling state change
    def handle(self, vehicle, event):
        vehicle.status = Busy()
