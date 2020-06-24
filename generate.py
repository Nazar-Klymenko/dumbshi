import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["printds"]

col = db["ids"]


def getRand():
    characters = '0123456789qwertyuiopasdfghjklzxcvbnm'
    result = ''
    for i in range(0, 6):
        result += random.choice(characters)
    dbdata = { "img_id": result, "checked": False, "source":"", "status": False}
    fin = col.insert_one(dbdata)
    print(result)

for x in range(0, 1000):
    getRand()