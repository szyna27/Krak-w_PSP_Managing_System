from src.iterator.VehicleIterator import VehicleIterator
from .Event import Event

# Class definition
class LocalHazard(Event):
    def __init__(self, color):
        super().__init__(color)
        self.vehicles_needed = 2

    def __str__(self):
        return f"{self.color}LocalHazard event in location: {self.location}{self.color_end}"