from random import choice


class Wywiad:
    def __init__(self):
        self.symptoms = f"Wywiad: {self.pick_symptoms()}, {self.pick_alergies()}, {self.pick_past()}, {self.pick_last_meal()}, {self.pick_events()}, {self.pick_onset()}, {self.pick_provocation()}"

    def pick_symptoms(self):
        symptoms_list = ["wymioty", "biegunka", "duszność", "kaszel", "ból brzucha", "ból głowy",
                         "ból w klatce piersiowej", "ból pleców", "utrudniony kontakt", "gorączka",
                         "kaszel szczekający", "wysypka", "obrzęki", "uraz głowy", "uraz nogi", "uraz brzucha",
                         "oparzenie","duszność","duszność","duszność","osłabienie","osłabienie","osłabienie","osłabienie","osłabienie"]
        return choice(symptoms_list)

    def pick_alergies(self):
        alergy_list = ["uczulone na paracetamol", "uczulone na penicylinę", "na nic nie uczulone",
                       "na nic nie uczulone", "na nic nie uczulone"]
        return choice(alergy_list)

    def pick_past(self):
        past_list = ["choruje na astmę", "ma wadę serca", "na nic nie choruje", "na nic nie choruje",
                     "na nic nie choruje"]
        return choice(past_list)

    def pick_last_meal(self):
        last_meal_list = ["ostatnio jadło godzinę temu", "ostatnio jadło wczoraj"]
        return choice(last_meal_list)

    def pick_events(self):
        events = ["wczoraj uraz brzucha", "", "", "","", "", "","", "", "", "wczoraj wymioty", "wczoraj biegunka", "",
                  "dziecko pobite wczoraj"]
        return choice(events)

    def pick_onset(self):
        onset = ["objawy od wczoraj", "objawy od godziny", "objawy od teraz", "objawy od kilku dni", "objawy od teraz"]
        return choice(onset)

    def pick_provocation(self):
        provocation = ["ruch nasilają objawy", "","", "", "", "wysiłek nasila objawy", "dotyk nasila objawy", ""]
        return choice(provocation)
