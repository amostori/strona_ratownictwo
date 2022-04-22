from random import randint, choice

exam_glucose = randint(20, 100)
exam_head_list = [
    "uraz głowy", "nierówne źrenice", "asymetria twarzy", "ślinotok", "niewyraźna mowa", "sztywność karku",
    "oczy szopa", "zasinienie za uszami", "głowa bez zmian", "głowa bez zmian", "głowa bez zmian", "głowa bez zmian",
    "głowa bez zmian", "głowa bez zmian", ]
exam_chest_list = ["świsty", "trzeszczenia nad płucami", "szmer pęcherzykowy", "szmer pęcherzykowy",
                   "szmer pęcherzykowy", "szmer pęcherzykowy", "szmer pęcherzykowy",
                   "szmer pęcherzykowy", "brak szmeru", "furczenia", "zasinienie w okolicy klatki piersiowej"]
exam_stomach_list = ["zasinienie brzucha", "brzuch bez zmian", "brzuch bez zmian", "brzuch bez zmian",
                     "brzuch bez zmian", "brzuch bez zmian", "brzuch bez zmian", "brzuch bez zmian", "brzuch bez zmian",
                     "brzuch bez zmian", "brzuch bez zmian", "brzuch bez zmian",
                     "brak perystaltyki", "bolesny, tkliwy brzuch", "brzuch deskowaty"]
exam_croch_list = ["krocze bez zmian", "krocze bez zmian",
                   "krocze bez zmian", "krocze bez zmian", "krocze bez zmian", "krocze bez zmian", "krocze bez zmian",
                   "krocze bez zmian", "krocze bez zmian",
                   "nieblędnąca wysypka w okolicy krocza"]
exam_extremites_list = ["uraz uda lewego", "uraz uda prawego", "uraz obu kości udowych",
                        "uraz kości ramiennej prawej",
                        "uraz obu rąk", "kończyny bez zmian", "kończyny bez zmian", "kończyny bez zmian",
                        "kończyny bez zmian", "kończyny bez zmian", "kończyny bez zmian", "kończyny bez zmian",
                        "kończyny bez zmian", "kończyny bez zmian", "kończyny bez zmian", "kończyny bez zmian",
                        "kończyny bez zmian", ]


class Exam:

    def __init__(self):
        self.exam = self.get_exam()

    def get_exam(self):
        exam_head = choice(exam_head_list)
        exam_chest = choice(exam_chest_list)
        exam_stomach = choice(exam_stomach_list)
        exam_croch = choice(exam_croch_list)
        exam_extremites = choice(exam_extremites_list)
        return f"\nObjawy badania przedmiotowego: glukoza {exam_glucose} mg/dl, {exam_head}, {exam_chest}, {exam_stomach}, {exam_croch}, {exam_extremites}"
