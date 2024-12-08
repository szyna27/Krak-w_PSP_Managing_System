from .VehicleCollection import VehicleCollection

# Class definition
class FireStation:
    # Constructor
    def __init__(self, name: str, location: tuple, num_vehicles: int):
        self.__name = name
        self.__location = location
        self.__vehicles = VehicleCollection(num_vehicles, name)

    # Getters and setters
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, location):
        self.__location = location
        
    def send_vehicle(self, event):
        vehicle = self.__vehicles.iterator.next()
        if vehicle is not None:
            vehicle.send(event)
            return vehicle
        return None
