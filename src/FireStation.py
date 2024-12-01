# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Import necessary modules
from .Vehicle import Vehicle

# Class definition
class FireStation:
    # Constructor
    def __init__(self, name: str, location: tuple, num_vehicles: int):
        self.__name = name
        self.__location = location
        self.__availabile_vehicles = [Vehicle() for _ in range(num_vehicles)]
        self.__busy_vehicles = []   

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

    @property
    def available_vehicles(self):
        return self.__vehicles
    
    @available_vehicles.setter
    def available_vehicles(self, vehicles):
        self.__vehicles = vehicles

    def handle_event(self, vehicles_needed: int, event) -> int:
        if len(self.__availabile_vehicles) < vehicles_needed:
            vehicles_to_send = self.__availabile_vehicles
        else:
            vehicles_to_send = self.__availabile_vehicles[:vehicles_needed]

        for vehicle in vehicles_to_send:
            self.__send_vehicle(vehicle, event)

        return vehicles_needed - len(vehicles_to_send)
        
    def __send_vehicle(self, vehicle: Vehicle, event):
        self.__busy_vehicles.append(self.__availabile_vehicles.pop(self.__availabile_vehicles.index(vehicle)))
        vehicle.send(event)
