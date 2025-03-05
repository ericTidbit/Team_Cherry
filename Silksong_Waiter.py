import sys

class Silksong_Waiter:
    def __init__(self, nom: str, sanity: int):
        self.nom = nom
        self._sanity = sanity


    @property
    def nom(self):
        return self._nom


    @nom.setter
    def nom(self, nouveau_nom):
        self._nom = nouveau_nom


    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, new_sanity):
        if not isinstance(new_sanity, int):
            raise ValueError("La valeur doit être un chiffre entier. ")
        self._sanity += new_sanity


    def pass_day(self, value):
        if not isinstance(value, int):
            raise ValueError("Sanity doit être un nombre entier. ")
        if value <= 10:
            self.kms(0)
        else:
            self._sanity += 5


    def kms(self, sanity):
        self._sanity = 0
        print(f"{self.nom} s'est suicidé, rip")
        sys.exit(0)



