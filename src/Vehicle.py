from threading import Thread
from .state import *

# Class definition
class Vehicle:
    # Constructor
    def __init__(self, name: str, number: int):
        self.__station_name = name
        self.__number = number
        self.__state = Available()

    # Getters and setters
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def station_name(self):
        return self.__station_name
    
    @station_name.setter
    def station_name(self, name):
        self.__station_name = name
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        self.__number = number

    # Methods for setting states
    def set_available(self):
        self.state = Available()

    def set_prepared(self):
        self.state = Prepared()

    def set_driving(self):
        self.state = Driving()

    def set_returning(self):
        self.state = Returning()

    def set_busy(self):
        self.state = Busy()

    # Method for handling sending vehicle
    def send(self, event):
        """Creates a new thread to handle the event"""
        self.state.handle(self, event)
        thread = Thread(target=self.__handle_send, args=(self, event))
        thread.daemon = True    # Thread will close if program is stopped
        thread.start()

    # Method for thread handling
    @staticmethod
    def __handle_send(vehicle, event):
        """Handles the event"""
        while not vehicle.state.is_available():
            print(f"{event.color}Vehicle {vehicle.number} from {vehicle.station_name} is {vehicle.state}{event.color_end}")
            vehicle.state.handle(vehicle, event)
