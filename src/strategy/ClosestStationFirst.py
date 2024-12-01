# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from .Strategy import Strategy

# Class definition
class ClosestStationFirst(Strategy):
    # Method for handling strategy
    def execute(self):
        print("Executing ClosestStationFirst strategy")