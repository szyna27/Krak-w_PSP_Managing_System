from .FireStation import FireStation
from .observer import HazardObserver
from .event import *
from .strategy import *
from .CONSTANTS import *

class Manager:
    def __init__(self, event_trigger, lock):
        self.fire_stations = []
        for name, location in STATIONS.items():
            self.fire_stations.append(FireStation(name, location, NUM_VEHICLES))
        
        self.__observer = HazardObserver(self)
        self.__strategy = None
        self.__events = []
        self.__event_trigger = event_trigger
        self.__lock = lock

    @property
    def observer(self):
        return self.__observer
    
    @observer.setter
    def observer(self, observer):
        self.__observer = observer

    @property
    def events(self):
        return self.__events
    
    @events.setter
    def events(self, events):
        self.__events = events

    def __get_event(self):
        with self.__lock:
            if len(self.__events) > 0:
                return self.__events.pop(0)
        return None
    
    def handle_event(self, event):
        if isinstance(event, LocalHazard):
            self.__strategy = LocalHazardStrategy(self, event)
        elif isinstance(event, FireHazard):
            self.__strategy = FireHazardStrategy(self, event)

        self.__strategy.execute()

    def start(self):
        try:
            while True:
                event = self.__get_event()
                if event is not None:
                    self.handle_event(event)
                else:
                    print("Menager waiting for event")
                    self.__event_trigger.wait()
                    print("Menager woken up")
                    self.__event_trigger.clear()

        except KeyboardInterrupt:
            print("Menager stopped")

