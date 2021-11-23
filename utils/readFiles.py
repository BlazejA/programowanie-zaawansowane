from Movie import Movie as m


def get_data():
    object_list = []
    with open('data/movies.csv', encoding="utf8") as file:
        for i in file:
            row = i.strip().split(',')
            object_list.append(m(row[0], row[1], row[2]).__dict__)
    return object_list[1:]
