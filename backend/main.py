from flask import Flask, request, jsonify
import config, database, module, strings

app = Flask(__name__)


@app.route('/newUser', methods=['POST'])
def registration_handler():
	user_key = module.generate_code(config.users, 'user_key', 32)
	result = module.newUser(user_key)
	result['ok'] = True
	database.insert_info(config.users, result)
	return jsonify(result)

@app.route('/user<user_key>/getMe', methods=['POST'])
def getMe_handler(user_key):
	if module.checker_in_mongo(config.users, {'user_key' : user_key}):
		result = {'ok' : True}
		result['items'] = [*database.get_info(config.todoItems, {'user_key' : user_key})]
		return jsonify(result)
	else:
		return jsonify({'ok' : False, 'error' : strings.INVALID_USER_KEY})

@app.route('/user<user_key>/add', methods=['POST'])
def add_handler(user_key):
	if module.checker_in_mongo(config.users, {'user_key' : user_key}):
		data = request.get_json()
		if 'name' in data and 'tag' in data:
			if len(data['name']) > 256:
				if data['tag'] in strings.TAGS:
					result = {'ok' : True}
					result['item'] = module.newToDoItem(user_key, data['name'], data['tag'])
					database.insert_info(config.todoItems, result['item'])
					return jsonify(result)
				else:
					return jsonify({'ok' : False, 'error' : strings.INVALID_TAG})
			else:
				return jsonify({'ok' : False, 'error' : strings.TOO_LANG_NAME})
		else:
			return jsonify({'ok' : False, 'error' : strings.INVALID_DATA})
	else:
		return jsonify({'ok' : False, 'error' : strings.INVALID_USER_KEY})


@app.route('/user<user_key>/check', methods=['POST'])
def check_handler(user_key):
	if module.checker_in_mongo(config.users, {'user_key' : user_key}):
		data = request.get_json()
		if 'item_id' in data:
			if module.checker_in_mongo(config.todoItems, data['item_id']):
				item_info = database.get_info(config.todoItems, {'item_id' : data['item_id']})[0]
				if item_info['user_key'] == user_key:
					item_info['check'] = not(item_info['check'])
					database.update_info(config.todoItems, {'item_id' : data['item_id']}, {'check' : item_info['check']})
					return jsonify({'ok' : True, 'item' : {item_info}})
				else:
					return jsonify({'ok' : False, 'error' : strings.INVALID_ITEM_ID})
			else:
				return jsonify({'ok' : False, 'error' : strings.INVALID_ITEM_ID})
		else:
			return jsonify({'ok' : False, 'error' : strings.INVALID_DATA})
	else:
		return jsonify({'ok' : False, 'error' : strings.INVALID_USER_KEY})


@app.route('/user<user_key>/delete', methods=['POST'])
def delete_handler(user_key):
	if module.checker_in_mongo(config.users, {'user_key' : user_key}):
		data = request.get_json()
		if 'item_id' in data:
			if module.checker_in_mongo(config.todoItems, data['item_id']):
				item_info = database.get_info(config.todoItems, {'item_id' : data['item_id']})[0]
				if item_info['user_key'] == user_key:
					database.delete_info(config.todoItems, {'item_id' : data['item_id']})
					return jsonify({'ok' : True})
				else:
					return jsonify({'ok' : False, 'error' : strings.INVALID_ITEM_ID})
			else:
				return jsonify({'ok' : False, 'error' : strings.INVALID_ITEM_ID})
		else:
			return jsonify({'ok' : False, 'error' : strings.INVALID_DATA})
	else:
		return jsonify({'ok' : False, 'error' : strings.INVALID_USER_KEY})


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


app.run()