import markdown
import os
import shelve

#import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

#Create instance of Flask
app=Flask(__name__)

#Create the Api
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("data/books.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    # Present some documentation

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)



class BookList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        books = []

        for key in keys:
            books.append(shelf[key])

        return {'message': 'Success', 'data': books}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('author', required=True)
        # parser.add_argument('controller_gateway', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Book added', 'data': args}, 201


class Book(Resource):
    def get(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'Book not found', 'data': {}}, 404

        return {'message': 'Book found', 'data': shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (identifier in shelf):
            return {'message': 'Book not found', 'data': {}}, 404

        del shelf[identifier]
        return '', 204

api.add_resource(BookList, '/books')
api.add_resource(Book, '/book/<string:identifier>')
