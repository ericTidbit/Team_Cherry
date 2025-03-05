import sys

class Silksong_waiter:
    def __init__(self, nom: str, sanity: int):
        self.nom = nom
        self.sanity = sanity

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
        if isinstance(new_sanity, int):
            self._sanity = new_sanity
        else:
            raise ValueError("La valeur doit être un chiffre entier. ")
        

    def pass_day(self, value):
        if not isinstance(value, int):
            raise ValueError("Sanity doit être un nombre entier. ")
        if value <= 10:
            self.kms(value)
        else:
            self.sanity += 5

    def kms(self, value):
        self.sanity = value
        print("Tu t'est suicidé, rip")
        sys.exit(0)


