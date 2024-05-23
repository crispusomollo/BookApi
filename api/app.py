from os import getenv
from flask import Flask, jsonify, request
from markupsafe import escape
from config import Config
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)

#@app.route('/')
#def hello():
#    name = request.args.get("name", "World")
#    return f'Hello, {escape(name)}!'

mongo = PyMongo(app)
api = Api(app)

# Import resources and add routes
from resources.book import BookList, BookDetail
from resources.user import UserRegister, UserProfile
#from resources.reading_list import ReadingList, AddToReadingList
#from resources.reading_progress import ReadingProgress, UpdateReadingProgress

api.add_resource(BookList, '/books')
api.add_resource(BookDetail, '/books/<book_id>')
api.add_resource(UserRegister, '/users')
api.add_resource(UserProfile, '/users/<user_id>')
#api.add_resource(ReadingList, '/users/<user_id>/reading-list')
#api.add_resource(AddToReadingList, '/users/<user_id>/reading-list/<book_id>')
#api.add_resource(ReadingProgress, '/users/<user_id>/reading-progress/<book_id>')
#api.add_resource(UpdateReadingProgress, '/users/<user_id>/reading-progress/<book_id>')

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

