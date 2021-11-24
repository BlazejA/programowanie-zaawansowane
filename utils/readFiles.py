from Models.Links import Link


def get_data(open_file):
    rows_list = []
    with open_file as file:
        for i in file:
            row = i.strip().split(',')
            rows_list.append(row)
    return rows_list[1:]


def read_movies():
    return open('data/movies.csv', encoding="utf8")


def read_links():
    return open('data/links.csv', encoding="utf8")


def read_ratings():
    return open('data/ratings.csv', encoding="utf8")


def read_tags():
    return open('data/tags.csv', encoding="utf8")
