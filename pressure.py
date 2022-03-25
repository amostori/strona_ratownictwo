from random import choice, randint


class Pressure:

    def __init__(self):
        self.pressure = self.count_pressure()

    def count_pressure(self):
        pressure_ok = False
        skurcz = randint(0, 180)
        while not pressure_ok:
            rozkurcz = randint(0, 120)
            if skurcz > rozkurcz + 20:
                return f"ciśnienie {skurcz}/{rozkurcz} mmHg"
