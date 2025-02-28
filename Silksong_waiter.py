class Silksong_waiter:
    def __init__(self, nom: str, sanity: int):
        self.nom = nom
        self.sanity = sanity

    @property
    def nom(self):
        return self.nom

    @nom.setter
    def nom(self, nouveau_nom):
        self.nom = nouveau_nom

    @property
    def sanity(self):
        return self.sanity

    @sanity.setter
    def sanity(self, new_sanity):
        self.sanity = new_sanity

    def pass_day(self, sanity):
        pass

    def kms(self, sanity):
        pass


