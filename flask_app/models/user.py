from MySQLConnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.email = data['email']
        self.created_at = data ['created_at']
        self.updated_at = ['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(server_first_name)s, %(server_last_name)s, %(server_email)s );'
        
        return connectToMySQL('users_crud').query_db(query, data)
    
    @classmethod
    def get_all_users(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('users_crud').query_db(query)
        users = []
        for each_result in results:
            users.append(User(each_result))
            return users

    @classmethod
    def get_one_user(cls, data):
        query = 'SELECT * FROM users WHERE id = %(server_user_id)s;'
        results = connectToMySQL('users_crud').query_db(query)
        return User(results[0])
    
    @classmethod
    def update_user(cls, data):
        query = 'UPDATE users SET first_name = %(server_first_name)s, last_name = %(server_last_name)s, email = %(server_email)s) WHERE id = %(user_id)s;'
        return connectToMySQL('users_crud').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(user_id)s;'
        return connectToMySQL('users_crud').query_db(query, data)