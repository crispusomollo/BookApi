from flask import request
from flask_restful import Resource
from app import mongo

class ReadingList(Resource):
    def get(self, user_id):
        user = mongo.db.users.find_one_or_404({"_id": user_id})
        return user.get("reading_list", []), 200

class AddToReadingList(Resource):
    def post(self, user_id, book_id):
        user = mongo.db.users.find_one_or_404({"_id": user_id})
        mongo.db.users.update_one({"_id": user_id}, {"$addToSet": {"reading_list": book_id}})
        return {"msg": "Book added to reading list"}, 200

