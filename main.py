class BudynekMieszkalny:
    def __init__(self, id_budynku: int, metraz: float, cena: float, adres: str):
        self._id_budynku = id_budynku
        self._metraz = metraz
        self._cena = cena
        self._adres = adres

    @property
    def id_budynku(self) -> int:
        return self._id_budynku

    @property
    def metraz(self) -> float:
        return self._metraz

    @property
    def cena(self) -> float:
        return self._cena

    @property
    def adres(self) -> float:
        return self._adres

    def __str__(self):
        return f"Mieszkanie numer: {self.id_budynku}, metraż: {self.metraz}," \
               f" cena: {self.cena}, adres: {self.adres}"


class Dom(BudynekMieszkalny):

    def __init__(self, id_budynku: int, metraz: float, cena: float, adres: str):
        super().__init__(id_budynku, metraz, cena, adres)

    def __str__(self):
        return super().__str__()


class Mieszkanie(BudynekMieszkalny):

    def __init__(self, id_budynku: int, metraz: float, cena: float, adres: str):
        super().__init__(id_budynku, metraz, cena, adres)

    def __str__(self):
        return super().__str__()


class Zamowienie:
    @property
    def id(self) -> int:
        return self._id

    @property
    def zamowione_mieszkania(self) -> list:
        return self._zamowione_mieszkania

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @id.setter
    def id(self, value: int):
        self._id = value

    @zamowione_mieszkania.setter
    def zamowione_mieszkania(self, value: list):
        self._zamowione_mieszkania = value

    @imie.setter
    def imie(self, value: str):
        self._imie = value

    @nazwisko.setter
    def nazwisko(self, value: str):
        self._nazwisko = value

    def __str__(self):
        return f"Zamówienie numer: {self.id}" \
               f"\nmieszkania: {', '.join(str(i) for i in self.zamowione_mieszkania)}\n" \
               f"dla: {self.imie} {self.nazwisko}"

    def wylicz_wartosc(self):
        return sum(i.cena for i in self.zamowione_mieszkania)

    def wylicz_powierzchnie(self):
        return sum(i.metraz for i in self.zamowione_mieszkania)


class Developer:
    def __init__(self, id: int, nazwa: str, ilosc_nieruchomosci: int, nip: int):
        self._id = id
        self._nazwa = nazwa
        self._ilosc_nieruchomosci = ilosc_nieruchomosci
        self._nip = nip

    def __str__(self):
        return f"Developer: {self.nazwa} / {self.id} NIP: {self.nip}" \
               f"posiada: {self.ilosc_nieruchomosci} nieruchomości"

    @property
    def id(self) -> int:
        return self._id

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def ilosc_nieruchomosci(self) -> int:
        return self._ilosc_nieruchomosci

    @property
    def nip(self) -> int:
        return self._nip


dom1 = Dom(1, 95.23, 650000.234, "Katowice, słoneczna")
dom2 = Dom(2, 130.50, 724000.00, "Katowice, chorzowska")
mieszkanie1 = Mieszkanie(1, 183.00, 834000.00, "Chorzów, katowicka")
mieszkanie2 = Mieszkanie(2, 60, 450000, "Katowice, paderewskiego")

lista = [dom1, dom2, mieszkanie1, mieszkanie2]

zamowienie = Zamowienie()
zamowienie.id = 1
zamowienie.zamowione_mieszkania = lista
zamowienie.imie = "Janusz"
zamowienie.nazwisko = "Kowalski"

print("Wartość: {:.2f}".format(zamowienie.wylicz_wartosc()))
print("Powierzchnia: {:.2f}".format(zamowienie.wylicz_powierzchnie()))
print()
print(zamowienie)
