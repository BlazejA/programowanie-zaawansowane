from zadania_lab4 import Student
from zadania_lab4 import Library
from zadania_lab4 import Book
from zadania_lab4 import Employee
from zadania_lab4 import Order
from zadania_lab4 import Flat
from zadania_lab4 import House

stud1 = Student("Jan", 70)
stud2 = Student("Kasia", 30)
print(f"{stud1.is_passed()}, {stud2.is_passed()}")

# Zad2
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

# zad3

house = House("160m2", 4, "700000", "Dluga 1", 20)
flat = Flat("60m2", 2, "500000", "Prosta 12", "4")
print()
house.__str__()
flat.__str__()
