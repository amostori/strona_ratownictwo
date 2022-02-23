from random import randint
from wywiad import Wywiad
from pressure import Pressure
from age import Age
from consciousness import Consciousness
from exam import Exam
from ecg import Ecg
from temperature import Temperature
from skin import Skin


class Symptoms:

    def __init__(self):
        self.symptoms = self.get_symptoms()

    def get_symptoms(self):
        age = Age()
        consciousness = Consciousness()
        ecg = Ecg()
        pressure = Pressure()
        temp = Temperature()
        skin = Skin()
        wywiad = Wywiad()
        exam = Exam()
        return f"{age.age}, {consciousness.consciousness}\nCzęstość oddechu: {randint(0, 10)}/10 sek, saturacja {randint(50, 100)}%. częstość tętna {ecg.pulse_rate}/10 sek.\n{pressure.pressure}, {temp.temperature}, {skin.skin}\n{wywiad.symptoms}\n{exam.exam}\n{ecg.ekg}"
