from random import choice, randint

vt_list = ["częstoskurcz komorowy",
           "częstoskurcz nadkomorowy", ]
blok_list = ["blok II stopnia Mobitz II", "blok II stopnia Mobitz I", "blok III stopnia", "rytm zatokowy",
             "rytm zatokowy", "rytm zatokowy"]


class Ecg:

    def __init__(self):
        self.pulse_rate = randint(0, 30)
        self.ekg = self.get_ekg(self.pulse_rate)

    def get_ekg(self, rate):
        rate *= 6
        ekg = ""
        if rate > 100:
            ekg = choice(vt_list)
        elif 100 > rate > 50:
            ekg = choice(blok_list)
        else:
            ekg = "rytm_zatokowy"
        return f"zapis ekg: {ekg}"
