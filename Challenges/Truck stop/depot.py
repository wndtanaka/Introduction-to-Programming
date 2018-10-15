class Depot:
    def __init__(self, name):
        """Initialises the depot"""
        self.name = name
        self.contents = []
        pass

    def get_name(self):
        """Returns the name of the depot"""
        return self.name
        pass

    def get_contents(self):
        """Returns the contents of the depot"""
        return self.contents
        pass

    def add_cargo(self, cargo):
        """Adds cargo to the depot"""
        self.contents.append(cargo)
        pass

    def take_cargo(self, truck):
        """Takes cargo from a truck intended for this depot"""
        i = 0
        # for item in truck.contents[:]:
        # 	if item.get_destination() == self.name:
        # 		self.add_cargo(item)
        # 		truck.give_cargo(self.name)
        # 		truck.weight -= 1
        while i < len(truck.contents):
            if truck.contents[i].get_destination() == self.name:
                self.add_cargo(truck.contents[i])
                truck.give_cargo(self.name)
                truck.weight -= 1
            i += 1

    def give_cargo(self, truck):
        """Gives cargo to a truck intended for another depot"""
        i = 0
        stops = []
        for stop in truck.get_stops():
            stops.append(stop.name)
        total_contents = len(self.contents)
        sent = []
        # if truck.weight < truck.limit:
        #     # for item in self.contents:
        #     #     if item.get_destination() in stops:
        #     #         truck.add_cargo(item)
        #     #         truck.weight += 1
        #     #         self.contents.remove(item)
        # #print(stops)
        #     while i < len(self.contents):
        #         if self.contents[i].get_destination() != self.name:
        #             truck.add_cargo(self.contents[i])
        #             truck.weight += 1
        #             self.contents.remove(self.contents[i])
        #             print('ok')
        #         i += 1
        while i < total_contents:
            if self.contents[i].get_destination() in stops:
                truck.add_cargo(self.contents[i])
                truck.weight += 1
                sent.append(self.contents[i])
                #self.contents.remove(self.contents[i])
            i += 1

        for item in sent:
            print(item.get_description())
            self.contents.remove(item)