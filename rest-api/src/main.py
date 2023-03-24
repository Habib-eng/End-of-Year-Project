from bottle import Bottle, request
import json
from db.repository import UserService, SQLRepository
from .models import Person

app = Bottle()
repository = SQLRepository(connection_uri="mongodb://root:12345678@127.0.0.1:27017/",db_name="database",table_name="persons")
person_model = UserService(repository=repository)

@app.route("/users",method="GET")
def getAllUsers():
    payload = person_model.get_all_users()
    return json.dumps(payload)

@app.route("/users/<id>",method="GET")
def get_user_by_id(id):
    payload = person_model.get_user_by_id(id)
    return {"data": payload}

@app.route("/users",method="POST")
def create_user():
    data = request.json
    payload = person_model.create_user(data)
    return payload

@app.route("/users/<id>",method="PUT")
def edit_user(id):
    data = request.json
    data["id"] = id
    is_inserted = person_model.update_user(data)
    return {"message": str(is_inserted)}

@app.route("/users/<id>", method="DELETE")
def delete_user(id):
    data = request.json
    is_deleted = person_model.delete_user(id)
    return {"message": str(is_deleted)}