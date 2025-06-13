import menu
import actions
import data


def main():
    

    try:
        students_info=[]
        while(True):
            menu.display_main_menu()
            option=int(input("Enter an option:"))
            if(option==1):
                student=actions.Student.create_student()
                students_info.append(student)
                print("The student has been successfully added.")
            if(option==2):
                if (not students_info):
                    print("The data has not been imported.")
                else:
                    print("List of the students:"+"\n")
                    actions.view_all_students(students_info)
            if(option==3):
                if (not students_info):
                    print("The data has not been imported.")
                else:
                    print("List top three: "+"\n")
                actions.view_top_three_students(students_info)
            if(option==4):
                if (not students_info):
                    print("The data has not been imported.")
                else:
                    print(f"the average grade among all students: {actions.calculate_average_grade(students_info)} "+"\n")
                
            if(option==5):
                if(not students_info):
                    print("No information to add.")
                else:
                    data.export_data_to_csv('students_data.csv',students_info,["full_name","section","spanish_grade","english_grade","social_studies_grade","science_grade","final_average"])
                    print("Data was exported.")
            if(option==6):
                try:
                    students_info=data.import_data_csv('students_data.csv')
                    print("Data has been imported.")
                except FileNotFoundError:
                    print("The file has not been generated..")
            if(option==7):
                break

    except Exception as error:
        print(f'An error has occurred: {error}')
        
	

if __name__ == '__main__':
	main()
