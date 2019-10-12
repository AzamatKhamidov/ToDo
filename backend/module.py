import random, time, config, database

def generate_password(m):
    pass1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    pass2 = 'abcdefghijkmnpqrstuvwxyz'
    pass3 = '23456789'
    pass4 = ''
    pass5 = [1,2,3]
    pass6 = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    for i in range(3):
        v = random.choice(pass5)
        if v == 1:
            pass4 += random.choice(pass1)
        elif v == 2:
            pass4 += random.choice(pass2)
        else:   
            pass4 += random.choice(pass3)
        if i == 0:
            if v == 1:
                pass5.remove(1)
            if v == 2:
                pass5.remove(2)
            if v == 3:
                pass5.remove(3)
        elif i == 1:
            if 3 in pass5:
                if 2 in pass5:
                    if v == 2:
                        pass5.remove(2)
                    else:
                        pass5.remove(3)
                else:
                    if v == 1:
                        pass5.remove(1)
                    else:
                        pass5.remove(3)
            else:
                if v == 1:
                    pass5.remove(1)
                else:
                    pass5.remove(2)
    for i in range(m-3):
        pass7 = random.choice(pass6)
        pass4 += pass7
    return pass4

def generate_code(connector, checker, length, check_lower=False):
	code = make_code(1, length)[0]
	if check_lower:
		if not checker_in_mongo(connector, {checker : code.lower()}):
			return code
	else:
		if not checker_in_mongo(connector, {checker : code}):
			return code
	generate_code(connector, checker, length)

def make_code(n, m):
    pass8 = []
    for i in range(n):
        q = generate_password(m)
        while q in pass8:
            q = generate_password(m)
        pass8.append(q)
    return pass8 

def checker_in_mongo(connector, data):
	try:
		database.get_info(connector, data)
		return True
	except:
		return False

def newToDoItem(user_key, name, tag):
	return {
		'user_key' : user_key,
		'name' : name,
		'tag' : tag,
		'parent_tag' : tag,
		'check' : False,
		'item_id' : generate_code(config.todoItems, 'item_id', 32)
	}

def newUser(user_key):
	return {
		'user_key' : user_key,
		'first_request' : time.time(),
		'last_request' : time.time()
	}