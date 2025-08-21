class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self,car_record):
        return {
            "id": car_record[0],
            "make": car_record[1],
            "model": car_record[2],
            "manufacture_year": car_record[3],
            "car_status": car_record[4],
        }

    def create(self, make,model,manufacture_year,car_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars ( make,model,manufacture_year,car_status) VALUES (%s, %s, %s,%s)",
                ( make,model,manufacture_year,car_status),
            )
            print("Car inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a car into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,make,model,manufacture_year,car_status FROM lyfter_car_rental.cars;"
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all cars from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,make,model,manufacture_year,car_status FROM lyfter_car_rental.cars WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_car(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
        
    def get_by_make(self, _make):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,make,model,manufacture_year,car_status FROM lyfter_car_rental.cars WHERE make = %s;",
                (_make,),
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
        
    def get_by_model(self, _model):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,make,model,manufacture_year,car_status FROM lyfter_car_rental.cars WHERE model = %s;",
                (_model,),
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
        
    def get_by_manufacture_year(self, _manufacture_year):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,make,model,manufacture_year,car_status FROM lyfter_car_rental.cars WHERE manufacture_year = %s;",
                (_manufacture_year,),
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
        
    def get_by_car_status(self, _car_status):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,make,model,manufacture_year,car_status FROM lyfter_car_rental.cars WHERE car_status = %s;",
                (_car_status,),
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False

    def update(self, _id,make,model,manufacture_year,car_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET (make,model,manufacture_year,car_status) = (%s, %s, %s,%s) WHERE ID = %s",
                (make,model,manufacture_year,car_status, _id),
            )
            print("Car updated successfully")
            return True
        except Exception as error:
            print("Error updating a car from the database: ", error)
            return False

    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.cars WHERE id = (%s)", (_id,)
            )
            print("Car deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a car from the database: ", error)
            return False
        
    def update_status(self, _id,car_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status = %s WHERE ID = %s",
                (car_status, _id),
            )
            print("Car status updated successfully")
            return True
        except Exception as error:
            print("Error updating a car from the database: ", error)
            return False
        
    