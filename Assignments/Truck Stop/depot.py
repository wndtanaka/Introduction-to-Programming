class Depot:
    def __init__(self, name):
        """Initialises the depot"""
        self.name = name
        self.cargo = []
        pass

    def get_name(self):
        """Returns the name of the depot"""
        pass

    def get_contents(self):
        """Returns the contents of the depot"""
        pass

    def add_cargo(self, cargo):
        """Adds cargo to the depot"""
        self.cargo.append(cargo)
        pass

    def take_cargo(self, truck):
        """Takes cargo from a truck intended for this depot"""
        pass

    def give_cargo(self, truck):
        """Gives cargo to a truck intended for another depot"""
        pass
