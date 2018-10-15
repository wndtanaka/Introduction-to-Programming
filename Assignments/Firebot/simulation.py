from perlin import Perlin
from tree import Tree


class Simulation:

    def __init__(self, seed, width, height):
        self.seed = seed
        self.width = width
        self.height = height
        pass

    def generate_trees(self, seed):
        ###################################
        ### DO NOT MODIFY THIS FUNCTION ###
        ###################################
        trees = []

        perlin = Perlin(seed)
        scale = 10.0 / min(self.width, self.height)

        for y in range(self.height):
            row = []
            for x in range(self.width):
                tree_h = perlin.noise(x * scale, y * scale, 0.5)
                tree_h = max(0, tree_h * 1.7 - 0.7) * 10
                row.append(Tree(int(tree_h)))
            trees.append(row)

        # `trees` is a grid (two-dimensional list) of `Tree` objects
        return trees
