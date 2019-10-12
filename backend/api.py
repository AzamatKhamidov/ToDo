from flask import Flask, request
import urllib3
import pymongo
from pymongo import MongoClient
import json

db_client = pymongo.MongoClient() #put here your mongodb address, if need
db = db_client.todo
app = Flask(__name__)
#http = urllib3.PoolManager()

#кароч тут как бы основа есть, но надо еще написать филтрацию и флуд лимиты

def find_session(coll, key, uid=-1, name=None, is_autoraised=False):
	if uid == -1:
		uid = coll.count_documents()

	try:
		user = call.find_one({"key": session})
	except Exception as e:
		user = {
			"id": uid, #random.randint(17, 109878)
			"key": key,
			"name": name,
			"is_autoraised": is_autoraised,
		}
		db.insert_one(user)
	return user

@app.route('/todoapi/<session>/additem', methods=["POST"])
def additem(session):
	item = request.get_json()

	user = find_session(db.sessions, session)
	item["userid"] = user["id"]

	db.items.update_one({"_id": item["userid"], }, {"$set": item, }, upsert=True)

	return 200

@app.route('/todoapi/<session>/edititem', methods=["POST"])
def edititem(session):
	item = request.get_json()

	user = find_session(db.sessions, session)
	item["userid"] = user["id"]

	db.items.update_one({"_id": item["userid"], }, {"$set": item, })

	return 200

@app.route('/todoapi/<session>/delitem', methods=["POST"])
def delitem(session):
	item = request.get_json()

	user = find_session(db.sessions, session)
	item["userid"] = user["id"]

	db.items.delete_one({"_id": item["userid"], })

	return 200

@app.route('/todoapi/<session>/items.json', methods=["POST"])
def getitems(session)
	user = find_session(db.sessions, session)

	item = request.get_json()
	item["userid"] = user["id"]

	db.items.find()