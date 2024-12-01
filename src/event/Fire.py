# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from .Event import Event

# Class definition
class Fire(Event):
    def __init__(self):
        super().__init__()

    # Method for handling fire
    def handle(self):
        print("Fire is being handled")
        pass