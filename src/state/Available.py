from .State import State

# Class definition
class Available(State):
    # Method for handling state change
    def handle(self, vehicle, event):
        vehicle.set_prepared()

    def is_available(self):
        return True
    
    def __str__(self):
        return "Available"
