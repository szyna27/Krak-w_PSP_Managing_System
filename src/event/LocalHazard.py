# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from .Event import Event

# Class definition
class LocalHazard(Event):
    def __init__(self):
        super().__init__()

    # Method for handling local hazard
    def handle(self):
        print("Local hazard is being handled")
        pass