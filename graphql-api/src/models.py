from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from decouple import config

client = MongoClient(config("DATABASE_URI"))
db = client[config("DATABASE_NAME")][config("COLLECTION")]

class Person(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None
    address: dict | None = None
    contact: list[dict] | None = None

    def save(self):
        is_inserted = False
        try:
            db.insert_one(self.model_dump_json())
            is_inserted = True
        except Exception as e:
            is_inserted = False
        return is_inserted

    @classmethod
    def get_all_persons(cls):
        try:
            users_list = list(db.find({}))

            ### convert _id from ObjectId to str type
            for person in users_list:
                person["id"] = str(person["_id"])
            payload = {
                "success": True,
                "users": users_list
            }
        except Exception as error:
            payload = {
                "success": False,
                "errors": [str(error)]
            }
        return payload
    
def users_resolver():
    person_repo = Person()
    payload = person_repo.get_all_persons()
    return payload