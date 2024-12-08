from .State import State

# Class definition
class Prepared(State):
    # Method for handling state change
    def handle(self, vehicle, event):
        vehicle.set_driving()

    def is_available(self):
        return False
    
    def __str__(self):
        return "Prepared"