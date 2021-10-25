# Zadanie1
def printData(name, surname):
    return f"Cześć {name} {surname}!"


hello = printData("Jan", "Kowalski")
print(hello)


# Zadanie2
def multiply(int1: int, int2: int):
    return int1 * int2


print(multiply(2, 5))


# Zadanie3
def isEven(number: int) -> bool:
    if (number % 2 == 0):
        return True
    else:
        return False


isEven = isEven(5)
if (isEven):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


# Zadanie 4
def checkNumbers(int1: int, int2: int, int3: int) -> bool:
    if (int1 + int2 >= int3):
        return True
    else:
        return False


# Zadanie 5
def foundValue(list1: list, int1: int):
    for i in list1:
        if (i == int1):
            return True
    return False


print(foundValue([1, 2, 3, 4, 5, 6], 6))


# Zadanie 6
def join(list1: list, list2: list):
    for i in list2:
        if i not in list1:
            list1.append(i)
    list1 = [i ** 3 for i in list1]
    return list1


x = join([1, 2, 3], [3, 4, 5])
print(x)
