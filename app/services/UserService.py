from utils.tools import selDB, insDB
from base.baseModels import User

class UserService:
    def get():
        query = "select * from users;"
        users = selDB(query)
        return users
    
    def getById(user_id): pass

    def usernameExists(user: User):
        query = "select * from users where username=%s"
        values = (user.username,)
        user = selDB(query, values)
        return user
    
    def post(user: User):
        query = "insert into users(username, password) values(%s, %s)"
        values = user.username, user.password
        aux = insDB(query, values)
        return user
    