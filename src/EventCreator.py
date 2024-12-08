from src.CONSTANTS import EVENT_PROBABILITY
from .event import *
from random import random
from threading import Thread
from time import sleep

# Class definition
class EventCreator:
    def __init__(self, event_trigger, lock):
        self.__observers = []
        self.__event_trigger = event_trigger
        self.__lock = lock
        # Create list of colors that will be added in prints connected to specific event
        self.__colors = ["\033[90m", "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
        self.__index = 0

    # Method for adding observer
    def add_observer(self, observer):
        self.__observers.append(observer)

    # Method for removing observer
    def remove_observer(self, observer):
        self.__observers.remove(observer)

    # Method for notifying observers
    def notify_observers(self, event):
        for observer in self.__observers:
            observer.update(event, self.__event_trigger, self.__lock)

    # Method for creating event
    def create_event(self):
        if random() < 0.7:
            hazard = LocalHazard(self.__colors[self.__index])
        else:
            hazard = FireHazard(self.__colors[self.__index])

        self.__index = (self.__index + 1) % len(self.__colors)
        return hazard
        
    # Method for starting the event creator
    def start(self):
        thread = Thread(target=self.__event_creation_loop, args=(self,))
        thread.daemon = True
        thread.start()        

    @staticmethod
    def __event_creation_loop(event_creator):
        while True:
            if random() < EVENT_PROBABILITY:
                event = event_creator.create_event()
                print(f"New event: {event}")
                event_creator.notify_observers(event)
            sleep(1)
        