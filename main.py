from src import *
from threading import Lock, Event

lock = Lock()
event_trigger = Event()

manager = Manager(event_trigger, lock)
event_creator = EventCreator(event_trigger, lock)
event_creator.add_observer(manager.observer)

event_creator.start()
manager.start()

