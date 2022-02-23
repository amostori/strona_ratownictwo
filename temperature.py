from random import choice

temp_list = ["35,5", "36,5", "37.0", "35,5", "36,5", "37.0", "37,8", "38,2", "38,8", "39,9", "40,1", "41"]


class Temperature:

    def __init__(self):
        self.temperature = f"Temperatura {choice(temp_list)} stopni C"
