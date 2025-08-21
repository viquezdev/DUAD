class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "name": user_record[1],
            "email": user_record[2],
            "username": user_record[3],
            "password": user_record[4],
            "birth_date": user_record[5],
            "account_status": user_record[6],
        }

    def create(self,name,email,username,password,birth_date,account_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users(name,email,username,password,birth_date,account_status) VALUES (%s, %s, %s,%s,%s,%s)",
                (name,email,username,password,birth_date,account_status),
            )
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,name, email,username, password,birth_date,account_status FROM lyfter_car_rental.users;"
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,name, email,username, password,birth_date,account_status FROM lyfter_car_rental.users WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
    
    def get_by_name(self, _name):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,name, email,username, password,birth_date,account_status FROM lyfter_car_rental.users WHERE name = %s;",
                (_name,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
        
    def get_by_email(self, _email):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,name, email,username, password,birth_date,account_status FROM lyfter_car_rental.users WHERE email = %s;",
                (_email,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
        
    def get_by_username(self, _username):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,name, email,username, password,birth_date,account_status FROM lyfter_car_rental.users WHERE username = %s;",
                (_username,),
            )
            formatted_result = self._format_user(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
        
    def get_by_birth_date(self, _birth_date):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,name, email,username, password,birth_date,account_status FROM lyfter_car_rental.users WHERE birth_date = %s;",
                (_birth_date,),
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
        
    def get_by_account_status(self, _account_status):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,name, email,username, password,birth_date,account_status FROM lyfter_car_rental.users WHERE account_status = %s;",
                (_account_status,),
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False

    def update(self, _id, name, email,username, password,birth_date,account_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET (name, email,username, password,birth_date,account_status) = (%s, %s, %s,%s, %s, %s) WHERE ID = %s",
                (name, email,username, password,birth_date,account_status, _id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.users WHERE id = (%s)", (_id,)
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False
        
    def update_status(self, _id,account_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE ID = %s",
                (account_status, _id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False
    
    def flag_user_as_moroso(self, _id):
        try:
            result=self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE ID = %s",
                ("moroso",_id),
            )
            print("User flagged as moroso")
            return result
        except Exception as error:
            print("Failed to flag user as moroso: ", error)
            return False