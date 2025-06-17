class Student:
    def __init__(self,full_name,section,spanish_grade,english_grade,social_studies_grade,science_grade,final_average):
        self.full_name=full_name
        self.section=section
        self.spanish_grade=spanish_grade
        self.english_grade=english_grade
        self.social_studies_grade=social_studies_grade
        self.science_grade=science_grade
        self.final_average=final_average
    

    def valid_grade(grade_name):
        while(True):
                try:
                    valid_grade=float(input(f"Enter {grade_name}:"))
                    if(valid_grade>=0 and valid_grade<=100):
                        return valid_grade
                        break
                    else:
                        print("Enter a valid grade...")
                except ValueError as error:
                    print(f'The number selected is invalid. Error: {error}')


    def create_student():
        full_name = input("Enter full name: ")
        section = input("Enter section: ")
        spanish_grade=Student.valid_grade("spanish_grade")
        english_grade=Student.valid_grade("english_grade")
        social_studies_grade=Student.valid_grade("social_studies_grade")
        science_grade=Student.valid_grade("science_grade")
        final_average=(spanish_grade+english_grade+social_studies_grade+science_grade)/4
        new_student=Student(full_name,section,spanish_grade,english_grade,social_studies_grade,science_grade,final_average)
        return new_student

    
def view_all_students(students_info):
    try:
        for student in students_info:
            print(f"{student.full_name} {student.section} {student.spanish_grade} {student.english_grade} {student.social_studies_grade} {student.science_grade} {student.final_average} '\n' ")
    except IndexError as ex:
        print(f"The index is out of range.Error: {ex}")
    
    
def view_top_three_students(students_info):
    try:
        average_list=[]
        for student in students_info:
            average_list.append(float(student.final_average))
        average_list.sort(reverse=True)
        for element in average_list[:3]:
            for student in students_info:
                if(float(student.final_average)==element):
                    print(f"{student.full_name} {student.final_average}")
    except IndexError as ex:
        print(f"The index is out of range.Error: {ex}")
    

def calculate_average_grade(students_info):
    try:
        if not students_info:
            return 0
        else:
            sum_total=0
            average=0
            for student in students_info:
                sum_total+=float(student.final_average)
            average=sum_total/len(students_info)
            return average
    except IndexError as ex:
        print(f"The index is out of range.Error: {ex}")
