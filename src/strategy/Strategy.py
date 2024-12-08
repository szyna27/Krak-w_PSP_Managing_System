from abc import ABC, abstractmethod

# Interface for strategy classes
class Strategy(ABC):
    def __init__(self, manager, event):
        self.manager = manager
        self.event = event
        self.distances = None
        self.calculate_distances()

    # Method for handling strategy
    @abstractmethod
    def execute(self):
        pass

    def calculate_distances(self):
        event_location = self.event.location
        self.distances = {
            station: self.__calculate_distance(event_location, station.location)
            for station in self.manager.fire_stations
        }

    def choose_nearest_station(self):
        if not self.distances:
            return None
        return min(self.distances, key=self.distances.get)

    def __calculate_distance(self, loc1, loc2):
        return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5