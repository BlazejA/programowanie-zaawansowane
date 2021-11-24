from flask import Flask
from flask_restful import Resource, Api

from Models.Movie import Movie
from Models.Rating import Rating
from utils.readFiles import *
from Models.Links import Link
from Models.Tag import Tag

app = Flask(__name__)
api = Api(app)


class GetMovies(Resource):

    def get(self):
        objects_list = []
        for i in get_data(read_movies()):
            objects_list.append(Movie(i[0], i[1], i[2]).__dict__)
        return objects_list


class GetLinks(Resource):

    def get(self):
        objects_list = []
        for i in get_data(read_links()):
            objects_list.append(Link(i[0], i[1], i[2]).__dict__)
        return objects_list


class GetRatings(Resource):

    def get(self):
        objects_list = []
        for i in get_data(read_ratings()):
            objects_list.append(Rating(i[0], i[1], i[2], i[3]).__dict__)
        return objects_list


class GetTags(Resource):

    def get(self):
        objects_list = []
        for i in get_data(read_tags()):
            objects_list.append(Tag(i[0], i[1], i[2], i[3]).__dict__)
        return objects_list


api.add_resource(GetMovies, '/movies')
api.add_resource(GetLinks, '/links')
api.add_resource(GetRatings, '/ratings')
api.add_resource(GetTags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
