class Moshina:
    def __init__(self, nomi, model, rang, km):
        self.nomi = nomi
        self.model = model
        self.rang = rang
        self.km = km

    def info(self):
        print(f" Nomi: {self.nomi}")
        print(f" Model: {self.model}")
        print(f" Rang: {self.rang}")
        print(f" Yurgan km: {self.km} km")

    def signal(self):
        print(f"{self.nomi}: Bip-bip! ")


# Obyekt
car1 = Moshina("Gentra", "Chevrolet", "oq", 54000)

# Metodlar
car1.info()
car1.signal()