# Zadanie1
def print_names(name1, name2, name3, name4, name5):
    print(f'{name1}, {name2}, {name3}, {name4}, {name5}')


print_names('Błażej', 'Ola', 'Jan', 'Kasia', 'Dawid')

# Zadanie2
numbers_list = [2, 4, 5, 7, 2]
multiplies_numbers = []


def multiply_numbers_for(list):
    for i in list:
        multiplies_numbers.append(i * 2)
    return multiplies_numbers


print(multiply_numbers_for(numbers_list))


def multiply_numbers_list(list):
    multiplies_numbers = [num * 2 for num in list]
    return multiplies_numbers


print(multiply_numbers_list(numbers_list))

# Zadanie 3
for x in range(10):
    if x % 2 == 0:
        print(x)
print()

# Zadanie 4
for x in range(1, 11, 2):
    print(x)
