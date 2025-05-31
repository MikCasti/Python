class Pacco:
    _counter = 1  # Contatore per generare numeri univoci dei pacchi

    def __init__(self, destinazione, peso=1000, altezza=100, larghezza=100, lunghezza=100):
        self._numero = Pacco._counter
        Pacco._counter += 1
        self.destinazione = destinazione
        self._peso = peso
        self._altezza = altezza
        self._larghezza = larghezza
        self._lunghezza = lunghezza

    @property
    def numero(self):
        return self._numero

    @property
    def peso(self):
        return self._peso

    @property
    def altezza(self):
        return self._altezza

    @property
    def larghezza(self):
        return self._larghezza

    @property
    def lunghezza(self):
        return self._lunghezza

    def __str__(self):
        return (f"Pacco #{self.numero}: Destinazione: {self.destinazione}, Peso: {self.peso}g, "
                f"Dimensioni: {self.altezza}x{self.larghezza}x{self.lunghezza} cm")
    