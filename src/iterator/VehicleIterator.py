from .Iterator import Iterator

# VehicleIterator class
class VehicleIterator(Iterator):
    # Constructor
    def __init__(self, vehicles):
        self.__vehicles = vehicles

    # Method for handling iteration
    def next(self) -> object:
        for vehicle in self.__vehicles:
            if vehicle.state.is_available():
                return vehicle
        return None
    
    # Method for checking if iteration is complete
    def has_next(self) -> bool:
        for vehicle in self.__vehicles:
            if vehicle.state.is_available():
                return True
        return False
