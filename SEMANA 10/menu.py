def display_main_menu():
    try:
        info_menu=["1. Enter student information","2. View information of all entered students","3. View the top 3 students with the highest average grade","4. View the average grade among all students","5. Export all current data to a CSV file","6. Import data from a CSV file","7. Exit the program"]
        print("*****Student Management System*****"+"\n")
        for item in info_menu:
            print(item +"\n")
    except IndexError as ex:
        print(f"The index is out of range.Error: {ex}")
