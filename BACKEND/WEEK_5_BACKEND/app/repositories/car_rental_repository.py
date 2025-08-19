class CarRentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car_rental(self,car_rental_record):
        return {
            "id": car_rental_record[0],
            "user_id": car_rental_record[1],
            "car_id": car_rental_record[2],
            "rental_date": car_rental_record[3],
            "rental_status": car_rental_record[4],
        }

    def create(self, user_id,car_id,rental_date,rental_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.car_rentals ( user_id,car_id,rental_date,rental_status) VALUES (%s, %s, %s,%s)",
                ( user_id,car_id,rental_date,rental_status),
            )
            print("Car rental inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a car rental into the database: ", error)
            return False

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,user_id,car_id,rental_date,rental_status FROM lyfter_car_rental.car_rentals;"
            )
            formatted_results = [self._format_car_rental(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all car rentals from the database: ", error)
            return False

    def get_by_id(self, _id):
        try:
            results = self.db_manager.execute_query(
                "SELECT id,user_id,car_id,rental_date,rental_status FROM lyfter_car_rental.car_rentals WHERE id = %s;",
                (_id,),
            )
            formatted_result = self._format_car_rental(results[0])
            return formatted_result
        except Exception as error:
            print("Error getting a car rental from the database: ", error)
            return False

    def update(self, _id,user_id,car_id,rental_date,rental_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.car_rentals SET (user_id,car_id,rental_date,rental_status) = (%s, %s, %s,%s) WHERE ID = %s",
                (user_id,car_id,rental_date,rental_status, _id),
            )
            print("Car rental updated successfully")
            return True
        except Exception as error:
            print("Error updating a car rental from the database: ", error)
            return False

    def delete(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM lyfter_car_rental.car_rentals WHERE id = (%s)", (_id,)
            )
            print("Car rental deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a car rental from the database: ", error)
            return False
        
    def update_status(self, _id,rental_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.car_rentals SET rental_status = %s WHERE ID = %s",
                (rental_status, _id),
            )
            print("Rental status updated successfully")
            return True
        except Exception as error:
            print("Error updating a rental status from the database: ", error)
            return False
        
    def complete_rental(self, _id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.car_rentals SET rental_status = %s WHERE ID = %s",
                ("completed",_id),
            )
            print("Rental completed successfully")
            return True
        except Exception as error:
            print("Failed to complete rental: ", error)
            return False