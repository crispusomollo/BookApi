from flask import request
from flask_restful import Resource
from api.app import mongo

class ReadingProgress(Resource):
    def get(self, user_id, book_id):
        progress = mongo.db.reading_progress.find_one({"user_id": user_id, "book_id": book_id})
        if not progress:
            return {"msg": "No reading progress found"}, 404
        return progress, 200

class UpdateReadingProgress(Resource):
    def put(self, user_id, book_id):
        data = request.get_json()
        mongo.db.reading_progress.update_one({"user_id": user_id, "book_id": book_id}, {"$set": data}, upsert=True)
        return {"msg": "Reading progress updated"}, 200

