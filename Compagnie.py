import datetime

class Compagnie:
    def __init__(self):
        self._nom: str = "Team Cherry"
        self._nombre_fans: int = 1_000_000
        self._release_date = None

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        nom = value

    @property
    def nombre_fans(self):
        return self._nombre_fans

    @nombre_fans.setter
    def nombre_fans(self, value):
        nombre_fans = value

    def annoncer(self):
        release_date = datetime.date.today()

    def shadowdrop(self):
        pass

    def generate_bait(self):
        pass

    def lie(self):
        pass

    def cancel(self):
        pass

    def __str__(self):
        return f"{self.nom} à {self.nombre_fans} fans!"

