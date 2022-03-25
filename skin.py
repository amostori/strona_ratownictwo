from random import choice

skin_list = ["normalna", "wilgotna, sina", "marmurkowa", "różowa", "sinica centralna", "sinica obwodowa",
             "blada"]


class Skin:

    def __init__(self):
        self.skin = f"skóra: {choice(skin_list)}"
