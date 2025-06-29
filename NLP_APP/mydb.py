import json

class Database:
    def add_data(self,name,email,password):

        with open('db.json','r') as rf:
            data = json.load(rf)

        if email in data:
            return 0
        else:
            data[email]=[name,password]

            with open('db.json','w') as wf:
                json.dump(data,wf)
            return 1
    def search(self,email,password):
        with open('db.json','r') as rf:
            database = json.load(rf)
        if email in database:
            if database[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0

