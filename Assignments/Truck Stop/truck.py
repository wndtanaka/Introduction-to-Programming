class Truck:
    def __init__(self, name, limit, itinerary):
        """Initialises the truck"""
        self.name = name
        self.limit = limit
        self.itinerary = itinerary
        pass

    def get_name(self):
        """Return the name of the truck"""
        return self.name
        pass

    def current_depot(self):
        """Returns the current depot it is at"""
        return
        pass

    def give_cargo(self, dest):
        """Returns a list of cargo that a depot will
        take ownership of. Helper method (optional)
        """
        pass

    def add_cargo(self, cargo):
        """Adds cargo item to the truck"""
        pass

    def get_stops(self):
        """Returns the itinerary"""
        pass

    def get_contents(self):
        """Returns the contents of the truck"""
        pass

    def has_stopped(self):
        """Returns a boolean to show whether the truck has stopped"""
        pass

    def move(self):
        """Moves the truck to the next depot"""
        pass

    def on_route(self, route):
        """Returns true if the truck is on route to a
        specified destination. Helper method: (Optional)
        """
        pass
