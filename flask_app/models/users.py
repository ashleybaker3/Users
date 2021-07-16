from config.mysqlconnection import connectToMySQL

class user:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(firstName)s , %(lastName)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users').query_db( query, data )

    @classmethod
    def show(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id' : id}
        results = connectToMySQL('users').query_db(query, data)
        if len(results) > 0:
            return results[0]
        else:
            return False
    
    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name=%(firstName)s, last_name = %(lastName)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL('users').query_db(query,data)
        return True