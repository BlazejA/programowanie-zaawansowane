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


stud1 = Student("Jan", 70)
stud2 = Student("Kasia", 30)
print(f"{stud1.is_passed()}, {stud2.is_passed()}")


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


lib1 = Library("Katowice", "Kwiatowa", "40-123", "8-17", "123123123")
lib2 = Library("Gdansk", "Dworcowa", "20-123", "10-20", "235235235")

book1 = Book("lib1", "20.02.2020", "Jan", "Kowalski", "133")
book2 = Book("lib1", "25.10.2012", "Dawid", "Nowak", "234")
book3 = Book("lib2", "22.04.2005", "Piotr", "Kowal", "43")
book4 = Book("lib2", "12.12.2000", "Monica", "Smith", "456")
book5 = Book("lib2", "05.07.2015", "Alex", "Brown", "231")

empl1 = Employee("Kasia", "Kowalska", "20.05.2004", "04.06.1981", "Gliwice", "Dluga", "12-123", "783534753")
empl2 = Employee("Maria", "Now", "12.07.2012", "09.11.1991", "Chorzow", "Krotka", "48-311", "782387123")
empl3 = Employee("Piotr", "Nowakowski", "24.08.2018", "22.01.1979", "Katowice", "Prosta", "53-576", "978765778")

stud3 = Student("Piotr", 23)
stud4 = Student("Patryk", 67)
stud5 = Student("Dominika", 90)

order1 = Order(empl1, stud3, book1, "20.10.2021")
order2 = Order(empl2, stud4, book2, "25.10.2021")
print()
order1.__str__()
print()
order2.__str__()


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


house = House("160m2", 4, "700000", "Dluga 1", 20)
flat = Flat("60m2", 2, "500000", "Prosta 12", "4")
print()
house.__str__()
flat.__str__()
