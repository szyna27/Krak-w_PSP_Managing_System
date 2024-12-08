from .Observer import Observer

# HazardObserver class
class HazardObserver(Observer):
    def __init__(self, menager):
        self.__menager = menager

    def update(self, event, event_trigger, lock):
        with lock:
            self.__menager.events.append(event)
        event_trigger.set()
        