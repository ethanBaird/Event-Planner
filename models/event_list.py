from models.event import Event

event1 = Event("11/03/2022", "Batman Premiere", 50, "Filmhouse", "Screening of the new Batman film", True)
event2 = Event("16/06/2022", "Wonderwoman", 60, "The Cameo", "Screening of the new Wonder Woman film", False)

events = [event1, event2]

def add_event_to_list(new_event):
        events.append(new_event)

def remove_event_from_list(event):
    events.remove(event)