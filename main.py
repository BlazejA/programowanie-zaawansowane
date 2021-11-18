from flask import Flask
from flask_restful import Resource, Api

from utils.readFiles import get_data as file

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self):
        return file()


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
