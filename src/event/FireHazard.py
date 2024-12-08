from .Event import Event

# Class definition
class FireHazard(Event):
    def __init__(self, color):
        super().__init__(color)
        self.vehicles_needed = 3

    def __str__(self):
        return f"{self.color}FireHazard event in location: {self.location}{self.color_end}"