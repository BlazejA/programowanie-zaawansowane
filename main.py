class Firma:
    def __init__(self, nazwa, adres, zatrudnienie, nip, wlasciciel):
        self._nazwa = nazwa
        self._adres = adres
        self._zatrudnienie = zatrudnienie
        self._nip = nip
        self._wlasciciel = wlasciciel

    def __str__(self):
        return f"Firma: {self.nazwa} właściel: {self.wlasciciel}\n" \
               f"NIP: {self.nip}, adres: {self.adres}\n" \
               f"zatrudnienie: {self.zatrudnienie}"

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def adres(self):
        return self._adres

    @property
    def zatrudnienie(self):
        return self._zatrudnienie

    @property
    def nip(self):
        return self._nip

    @property
    def wlasciciel(self):
        return self._wlasciciel


class Pojazd:
    def __init__(self, marka, model, rodzaj, ladownosc, rejestracja):
        self._marka = marka
        self._model = model
        self._rodzaj = rodzaj
        self._ladownosc = ladownosc
        self._rejestracja = rejestracja

    def __str__(self):
        return f"Samochód: {self.marka} {self.model} rodzaj: {self.rodzaj}, " \
               f"ładowność: {self.ladownosc}, rejestracja: {self.rejestracja}"

    @property
    def marka(self):
        return self._marka

    @property
    def model(self):
        return self._model

    @property
    def rodzaj(self):
        return self._rodzaj

    @property
    def ladownosc(self):
        return self._ladownosc

    @property
    def rejestracja(self):
        return self._rejestracja


class Odcinek:

    def __init__(self, numer_trasy: int, odleglosc: int, cel: str, start: str):
        self._numer_trasy = numer_trasy
        self._odleglosc = odleglosc
        self._cel = cel
        self._start = start

    def __str__(self):
        return f"Trasa o numerze: {self.numer_trasy}, odleglosc: {self.odleglosc}\n" \
               f"start trasy: {self.start} koniec: {self.cel}"

    @property
    def start(self):
        return self._start

    @property
    def cel(self):
        return self._cel

    @property
    def odleglosc(self):
        return self._odleglosc

    @property
    def numer_trasy(self):
        return self._numer_trasy


class Kurs:

    def __init__(self, pojazd: Pojazd, odcinek, cel: Odcinek, start: Odcinek, kierowca: str):
        self._start = start
        self._cel = cel
        self._kierowca = kierowca
        self._pojazd = pojazd
        self._odcinek = odcinek

    @property
    def start(self) -> None:
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def cel(self) -> None:
        return self._cel

    @cel.setter
    def cel(self, value):
        self._cel = value

    @property
    def kierowca(self) -> None:
        return self._kierowca

    @kierowca.setter
    def kierowca(self, value):
        self._kierowca = value

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value) -> Pojazd:
        self._pojazd = value

    @property
    def odcinek(self) -> Odcinek:
        return self._odcinek

    @odcinek.setter
    def odcinek(self, value) -> Odcinek:
        self._odcinek = value

    def sum(self):
        return self.odcinek.odleglosc

    def nazwa_pojazdu(self):
        return self.pojazd.marka


class FirmaTransportowa(Firma):
    def __init__(self, nazwa, adres, zatrudnienie, nip, wlasciciel):
        super().__init__(nazwa, adres, zatrudnienie, nip, wlasciciel)

    def __str__(self):
        return super().__str__()


class FirmaSpozywcza(Firma):

    def __init__(self, nazwa, adres, zatrudnienie, nip, wlasciciel):
        super().__init__(nazwa, adres, zatrudnienie, nip, wlasciciel)

    def __str__(self):
        return super().__str__()


pojazd1 = Pojazd("VW", "Passat", "Kombi", 1000, "Sk1234")
odcinek1 = Odcinek(1, 250, "Katowice", "Lodz")

kurs1 = Kurs(pojazd1, odcinek1, odcinek1.cel, odcinek1.start, "Janek")

print(kurs1.sum())
print(kurs1.nazwa_pojazdu())
