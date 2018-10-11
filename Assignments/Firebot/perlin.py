################################
### DO NOT MODIFY THIS CLASS ###
################################

import math


class Perlin:
    """Makes use of Java's RNG, rewritten in Python by Corbin Simpson.

    https://github.com/MostAwesomeDude/java-random
    """

    def __init__(self, seed):
        self.seed = seed
        self.start_seed = seed

    def set_seed(self, seed):
        self.seed = seed

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, seed):
        self._seed = (seed ^ 0x5deece66d) & ((1 << 48) - 1)

    def next_(self, bits):
        if bits < 1:
            bits = 1
        elif bits > 32:
            bits = 32

        self._seed = (self._seed * 0x5deece66d + 0xb) & ((1 << 48) - 1)
        retval = self._seed >> (48 - bits)

        if retval & (1 << 31):
            retval -= (1 << 32)

        return retval

    def randlong(self):
        return (self.next_(32) << 32) + self.next_(32)

    def randdouble(self):
        return ((self.next_(26) << 27) + self.next_(27)) / float(1 << 53)

    def rand(self, x, y, freq):
        self.set_seed(self.start_seed)
        self.set_seed((self.randlong() + int((x * 40303 + y * 325679) * freq)))
        return self.randdouble()

    def interpolate(self, x, y, frac):
        frac = (1 - math.cos(frac * math.pi)) / 2
        return x + (y - x) * frac

    def noise(self, x, y, persistence):
        sum_ = 0
        amp = 1
        freq = 1
        value = 0

        for stage in range(8):
            xx = int(x * freq) / freq
            yy = int(y * freq) / freq

            step = 1.0 / freq
            r00 = self.rand(xx, yy, freq)
            r10 = self.rand(xx + step, yy, freq)
            r01 = self.rand(xx, yy + step, freq)
            r11 = self.rand(xx + step, yy + step, freq)

            xxfrac = (x - xx) / step
            yyfrac = (y - yy) / step

            v1 = self.interpolate(r00, r10, xxfrac)
            v2 = self.interpolate(r01, r11, xxfrac)
            v3 = self.interpolate(v1, v2, yyfrac)

            value += v3 * amp
            sum_ += amp
            freq *= 2
            amp *= persistence

        return value / sum_
