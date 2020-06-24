# import pymongo


# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["printds"]
# col = db["ids"]

# # print(pymongo.version)
# # db.col.find( { "status": True } ).count_documents()
# # please = db.col.count_documents({ "status": False })

# # results = db.col.find({ "status": False })
# # results_count = results.count()
# # print(results_count)
# # if db.col.count_documents({}) > 0:
# #     print("yasss")
# # else:
# #     print("fuarrk")

# count = 0
# for record in db.col.find({ "checked": False }):
#     print(count)
#     count +=1