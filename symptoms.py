from random import randint, choice

from wywiad import Wywiad
from pressure import Pressure
from age import Age
from consciousness import Consciousness
from exam import Exam
from ecg import Ecg
from temperature import Temperature
from skin import Skin

drgawki = ['bez drgawek', 'drgawki']


def get_symptoms():
    age = Age()
    consciousness = Consciousness()
    pressure = Pressure()
    temp = Temperature()
    skin = Skin()
    ecg = Ecg()
    return f"{age.age}, {consciousness.consciousness}, {choice(drgawki)}, częstość oddechu: {randint(0, 10)}/10 sek, saturacja {randint(50, 100)}%, częstość tętna {ecg.pulse_rate}/10 sek., {pressure.pressure}, {temp.temperature}, {skin.skin}, {ecg.ekg}."


def get_sample():
    sample = Wywiad()
    return f"{sample.symptoms}."


def get_exam():
    exam = Exam()
    return f"{exam.exam}."


class Symptoms:

    def __init__(self):
        self.symptoms = get_symptoms()
