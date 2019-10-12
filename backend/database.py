
def get_info(connecter, data=False):
    if data:
        return connecter.find(data)
    else:
        return connecter.find()

def update_info(connecter, data_by, data_what):
    connecter.update_many(data_by,{'$set' : data_what})


def insert_info(connecter, data):
    connecter.insert_one(data)

def delete_info(connecter, data):
    connecter.delete_one(data)