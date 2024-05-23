# resources/user.py
from flask_restful import Resource
from flask import request

class UserRegister(Resource):
    def post(self):
        from app import mongo
        data = request.get_json()
        user_id = mongo.db.users.insert_one(data).inserted_id
        return {"id": str(user_id)}, 201

class UserProfile(Resource):
    def get(self, user_id):
        from app import mongo
        from bson.objectid import ObjectId
        user = mongo.db.users.find_one_or_404({"_id": ObjectId(user_id)})
        return {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}, 200
