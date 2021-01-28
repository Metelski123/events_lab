class Event():
    def __init__(self, date, event_name, guest_number, room_location, description, repeat=False):
        self.date = date
        self.event_name = event_name
        self.guest_number = guest_number
        self.room_location = room_location
        self.description = description
        self.repeat = repeat