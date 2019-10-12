import pymongo

client = pymongo.MongoClient('mongodb+srv://backend:DcXS76xc0G6r3vqm@todo-xwkpu.azure.mongodb.net/test?retryWrites=true&w=majority')
main_db = client['todo']
users = main_db['users']
todoItems = main_db['todo_items']