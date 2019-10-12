import pymongo

client = pymongo.MongoClient()
main_db = client['todo']
users = main_db['users']
todoItems = main_db['todo_items']