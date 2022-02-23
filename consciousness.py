from random import choice, randint


class Consciousness:
    def __init__(self):
        self.consciousness = self.get_consciousness()

    def get_consciousness(self):
        consciousness_list = ["Przytomne", "Reaguje na głos", "Reaguje na ból", "Nieprzytomne"]
        return choice(consciousness_list)
