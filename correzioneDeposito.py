class Deposito:
    def __init__(self, capacita_massima):
        self.capacita_massima = capacita_massima
        self.pacchi = []
        self._peso_massimo = 0  # Peso massimo registrato nel deposito

    def aggiungiPacco(self, pacco):
        if len(self.pacchi) >= self.capacita_massima:
            return False
        self.pacchi.append(pacco)
        peso_totale = self.quantoPeso()
        if peso_totale > self._peso_massimo:
            self._peso_massimo = peso_totale
        return True

    def trovaPacco(self, numeroPacco):
        for pacco in self.pacchi:
            if pacco.numero == numeroPacco:
                return pacco
        return None

    def quantiPacchi(self):
        return len(self.pacchi)

    def quantoPeso(self):
        return sum(pacco.peso for pacco in self.pacchi)

    def maxPeso(self):
        return self._peso_massimo

    def togliPacco(self, pacco):
        if pacco in self.pacchi:
            self.pacchi.remove(pacco)
            return True
        return False

    def togliPaccoNumero(self, numeroPacco):
        pacco = self.trovaPacco(numeroPacco)
        if pacco:
            self.pacchi.remove(pacco)
            return True
        return False

    def __str__(self):
        descrizione = (f"Deposito (Capacità massima: {self.capacita_massima}, "
                       f"Pacchi presenti: {self.quantiPacchi()}, Peso totale: {self.quantoPeso()}g, "
                       f"Peso massimo registrato: {self.maxPeso()}g)\n")
        descrizione += "\n".join(str(pacco) for pacco in self.pacchi)
        return descrizione