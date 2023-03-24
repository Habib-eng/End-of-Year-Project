from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from abc import ABC, abstractmethod

### Separation of concern : Data Layer(SQLRepository) and Bussiness Layer (UserService)

class IRepository(ABC):
    @abstractmethod
    def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self,id):
        raise NotImplementedError
    
    @abstractmethod
    def create(self, item):
        raise NotImplementedError
    
    @abstractmethod
    def update(self,item):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self,id):
        raise NotImplementedError
    
class SQLRepository(IRepository):
    
    def __init__(self,connection_uri,db_name,table_name) -> None:
        self._connection_uri = connection_uri
        self._connection = MongoClient(connection_uri)[db_name][table_name]
    
    def get_all(self):
        cursor = self._connection.find({})
        data = []
        for person in cursor:
            person["id"] = str(person.pop("_id"))
            data.append(person)
        return data
    
    def get_by_id(self, id):
        object_id = ObjectId(id)
        cursor = self._connection.find_one({"_id" : object_id})
        if cursor:
            cursor.pop("_id")
            res = cursor
        else:
            res = "Not Found Result"
        return res
    
    def create(self,item):
        self._connection.insert_one(item)
        return True
    
    def update(self, item):
        object_id = ObjectId(item["id"])
        filter = {"_id": object_id}
        cursor = self._connection.update_one(filter,{"$set":item})
        return True
    
    def delete(self, id):
        object_id = ObjectId(id)
        filter = {"_id" : object_id}
        self._connection.delete_one(filter)

class UserService:
    def __init__(self,repository: SQLRepository) -> None:
        self._repository = repository
    
    def get_all_users(self):
        return self._repository.get_all()
    
    def get_user_by_id(self,id):
        return self._repository.get_by_id(id)
    
    def create_user(self,user):
        return self._repository.create(user)
    
    def update_user(self, user):
        return self._repository.update(user)

    def delete_user(self,id):
        return self._repository.delete(id)