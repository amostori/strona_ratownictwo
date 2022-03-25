from random import choice, randint


class Consciousness:
    def __init__(self):
        self.consciousness = self.get_consciousness()

    def get_consciousness(self):
        consciousness_list = ["przytomne", "przytomne", "przytomne", "podsypiające", "podsypiające", "podsypiające",
                              "reaguje na głos", "reaguje na ból",
                              "nieprzytomne"]
        return choice(consciousness_list)
