import random
import pymongo
from decouple import config
import logging

cities = [
        "Bizerte",
        "Tunis",
        "Ariana",
        "Beja",
        "Gabes",
        "Mednine",
        "Sfax",
        "Jendouba",
        "Nabeul",
        "Sousse",
        "Mahdia"
    ]

def main():
    client = pymongo.MongoClient(config("DATABASE_URI"))
    db = client[config("DATABASE_NAME")][config("COLLECTION")]
    data = []
    for i in range(10):
        num = random.randint(0,10)
        payload = {
            "name": f"guest_{num}",
            "email": f"guest_{num}@guested.com",
            "age": num,
            "address": {
                "street": f"street N° {num}",
                "city": cities[i],
                "zip_code": num + 200
            },
            "contact": [
                {
                    "type": "phone number",
                    "value": f"{num}{i}856{num}32{i}" 
                }
            ]
        }
        data.append(payload)

    try:
        db.insert_many(data)
    except Exception as e:
        logging.error(e)

def confirm_seeder():
    client = pymongo.MongoClient(config("DATABASE_URI"))
    db = client[config("DATABASE_NAME")][config("COLLECTION")]    
    data = db.find({})
    for row  in data:
        print(row)
        
if __name__ == "__main__":
    confirm_seeder()