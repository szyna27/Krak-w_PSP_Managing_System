from .iterator.VehicleIterator import VehicleIterator
from .Vehicle import Vehicle

# VehicleCollection class
class VehicleCollection:
    """Class that holds all vehicles in queue, adding them to the end after 
    they come back from event handling and removing them from the front,
    also holds Iterator class for iterating through the collection"""
    def __init__(self, num_vehicles: int, name: str):
        self.__vehicles = [Vehicle(name, i) for i in range(num_vehicles)]
        self.iterator = VehicleIterator(self.__vehicles)
    
    # Method for adding vehicle to the collection
    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)
    
    # Method for removing vehicle from the collection
    def remove_vehicle(self):
        self.__vehicles.pop(0)
    
    # Method for getting vehicle from the collection
    def get_vehicle(self, index):
        return self.__vehicles[index]
    
    # Method for getting the length of the collection
    def get_length(self):
        return len(self.__vehicles)
