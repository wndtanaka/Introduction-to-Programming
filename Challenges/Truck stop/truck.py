class Truck:
    def __init__(self, name, limit, itinerary):
        """Initialises the truck"""
        self.name = name
        self.limit = limit
        self.itinerary = itinerary
        self.current_stop = 0
        self.contents = []
        self.is_stopped = False
        self.weight = 0
        pass

    def get_name(self):
        """Return the name of the truck"""
        return self.name
        pass

    def current_depot(self):
        """Returns the current depot it is at"""
        return self.itinerary[self.current_stop]
        pass

    def give_cargo(self, dest):
        """Returns a list of cargo that a depot will
        take ownership of. Helper method (optional)
        """
        if dest == self.itinerary[self.current_stop].name:
            for item in self.contents:
                if item.get_destination() == self.itinerary[self.current_stop].name:
                    self.contents.remove(item)
        return self.contents

    def add_cargo(self, cargo):
        """Adds cargo item to the truck"""
        if self.weight <= self.limit:
            # for item in cargo:
            self.contents.append(cargo)

    def get_stops(self):
        """Returns the itinerary"""
        return self.itinerary
        pass

    def get_contents(self):
        """Returns the contents of the truck"""
        return self.contents
        pass

    def has_stopped(self):
        """Returns a boolean to show whether the truck has stopped"""
        return self.is_stopped
        pass

    def move(self):
        """Moves the truck to the next depot"""
        # print(self.weight)
        if self.current_stop < len(self.itinerary) - 1:
            self.current_stop += 1
        else:
            self.is_stopped = True

    def on_route(self, route):
        """Returns true if the truck is on route to a
        specified destination. Helper method: (Optional)
        """
        if not self.is_stopped:
            return True
        pass
