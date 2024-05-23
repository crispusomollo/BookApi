from flask import request
from flask_restful import Resource
from api.app import mongo

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        user_id = mongo.db.users.insert_one(data).inserted_id
        return {"id": str(user_id)}, 201

class UserProfile(Resource):
    def get(self, user_id):
        user = mongo.db.users.find_one_or_404({"_id": user_id})
        return {"id": str(user["_id"]), "username": user["username"], "email": user["email"]}, 200

