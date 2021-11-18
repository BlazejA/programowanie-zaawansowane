# Zadanie 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks > 50:
            return True
        else:
            return False


# Zadanie 2
class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        print(f"Miasto: {self.city}, ulica: {self.street}, kod pocztowy: {self.zip_code},"
              f"godziny otwarcia: {self.open_hours}, numer telefonu: {self.phone}")


class Order:
    def __init__(self, employee, student, book, order_date):
        self.employee = employee
        self.student = student
        self.book = book
        self.order_date = order_date

    def __str__(self):
        print(
            f"Pracownik: {self.employee.first_name} {self.employee.last_name}, student: {self.student.name},"
            f" \nksiążka: {self.book.author_name} {self.book.author_surname},"
            f" \ndata zamówienia: {self.order_date}")


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        print(
            f"Imię: {self.first_name}, nazwisko: {self.last_name}, data zatrudnienia: {self.hire_date},"
            f" urodziny: {self.birth_date} miasto: {self.city}, ulica: {self.street}, kod pocztowy: {self.zip_code}, "
            f" numer telefonu: {self.phone}")


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        print(f"Biblioteka: {self.library}, data publikacji: {self.publication_date},"
              f" Autor: {self.author_name} {self.author_surname}, ilość stron: {self.number_of_pages}")


# Zadanie 3

class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        print(f"powierzchnia: {self.area}, pokoje: {self.rooms}"
              f" cena: {self.price}, adres: {self.address}")


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self):
        print(f"powierzchnia: {self.area}, pokoje: {self.rooms}"
              f" cena: {self.price}, adres: {self.address}, rozmiar działki: {self._plot}")


class Flat(Property):

    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self):
        print(f"powierzchnia: {self.area}, pokoje: {self.rooms}"
              f" cena: {self.price}, adres: {self.address}, piętro: {self._floor}")
