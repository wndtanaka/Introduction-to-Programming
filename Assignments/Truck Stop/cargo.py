class Cargo:
    def __init__(self, description, destination_name):
        """Initialises the cargo"""
        self.description = description
        self.destination_name = destination_name
        pass

    def get_description(self):
        """Returns a description of the cargo"""
        return self.description
        pass

    def get_destination(self):
        """Returns the destination name of the cargo"""
        return self.destination_name
        pass
