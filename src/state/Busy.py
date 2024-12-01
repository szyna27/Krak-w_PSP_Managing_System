# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from .State import State
from .Available import Available

# Class definition
class Busy(State):
    # Method for handling state change
    def change_status(self, vehicle, event):

        vehicle.status = Available()
        