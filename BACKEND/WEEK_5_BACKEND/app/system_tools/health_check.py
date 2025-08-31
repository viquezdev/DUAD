from app.db.pg_manager import PgManager



def system_monitor():
    try:
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        table_users_name='users'
        table_cars_name='cars'
        table_car_rentals_name='car_rentals'
        schema_name='lyfter_car_rental'
        result_users=db_manager.execute_query(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{schema_name}' AND table_name = '{table_users_name}');")[0][0]
        result_cars=db_manager.execute_query(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{schema_name}' AND table_name = '{table_cars_name}');")[0][0]
        result_car_rentals=db_manager.execute_query(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{schema_name}' AND table_name = '{table_car_rentals_name}');")[0][0]
        verify_car=db_manager.execute_query(f"SELECT EXISTS (SELECT 1 FROM {schema_name}.{table_cars_name} WHERE car_status='available');")[0][0]
        
        if result_users and result_cars and result_car_rentals:
            if verify_car:
                print("DB OK. Operating System running normally")
            else:
                print("DB ERROR. No available cars")
        else:
            print("DB ERROR. Missing tables in the database")

    
        
        db_manager.close_connection()

    except Exception as ex:
        print(f"DB error: {ex}")  

if __name__ == "__main__":
    system_monitor()