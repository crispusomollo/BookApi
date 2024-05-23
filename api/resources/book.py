# resources/book.py
from flask_restful import Resource
from flask import request
from bson.objectid import ObjectId

class BookList(Resource):
    def get(self):
        from app import mongo
        books = mongo.db.books.find()
        return [{"id": str(book["_id"]), "title": book["title"], "author": book["author"]} for book in books], 200

    def post(self):
        from app import mongo
        data = request.get_json()
        book_id = mongo.db.books.insert_one(data).inserted_id
        return {"id": str(book_id)}, 201

class BookDetail(Resource):
    def get(self, book_id):
        from app import mongo
        book = mongo.db.books.find_one_or_404({"_id": ObjectId(book_id)})
        return {"id": str(book["_id"]), "title": book["title"], "author": book["author"], "isbn": book["isbn"]}, 200
