from lib.user import *

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['id'], row['email_address'], row['username'])
            users.append(item)
        return users

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [id])
        row = rows[0]
        user = User(row['id'], row['email_address'], row['username'])
        return user

    def create(self, user):
        self._connection.execute('INSERT INTO users (email_address, username) VALUES(%s,%s)', [user.email_address, user.username])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None