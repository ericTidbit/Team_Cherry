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
        if isinstance(self.sanity, int):
            self._sanity = new_sanity
        else:
            raise ValueError("NaN")
        

    def pass_day(self, sanity):
        if self.sanity <= 10:
            kms(sanity)
        else:
            self.sanity += 5

    def kms(self, sanity):
        self.sanity = sanity
        print("Tu t'est suicidé, rip")
        sys.exit(0)


