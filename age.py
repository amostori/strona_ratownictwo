from random import choice, randint


class Age:
    def __init__(self):
        self.age = self.get_age()

    def get_age(self):
        age = ["m.ż", "r.ż"]
        word_age = choice(age)
        if word_age == "months":
            months_years = randint(1, 12)
        else:
            months_years = randint(1, 15)
        return f"Dziecko w wieku {months_years} {word_age}"
