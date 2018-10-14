class Tree:

    def __init__(self, height):
        self.height = height
        self.on_fire = False
        self.alive = True
        self.fire_level = 0
        self.wind_affected = False

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
        if self.fire_level < 9:
            self.fire_level += 1
        self.wind_affected = False

    def get_fire_level(self):
        if not self.on_fire:
            return self.height
        else:
            return self.fire_level

    def extinguish_fire(self):
        self.fire_level = 0
        self.on_fire = False

    def damage_tree(self):
        if self.fire_level >= 9 and self.alive:
            self.height -= 1
        if self.height <= 0:
            self.alive = False
            self.on_fire = False
            self.fire_level = 0