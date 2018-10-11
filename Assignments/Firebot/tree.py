class Tree:

    def __init__(self, height):
        self.height = height
        self.on_fire = False
        self.alive = True
        self.fire_level = 0
        pass

    def get_height(self):
        return self.height

    def is_alive(self):
        if self.height == 0:
            self.alive = False
        return self.alive

    def is_on_fire(self):
        return self.on_fire

    def burn_tree(self):
        self.on_fire = True
        self.fire_level += 1

    def get_fire_level(self):
        if not self.on_fire:
            return self.height
        else:
            return self.fire_level