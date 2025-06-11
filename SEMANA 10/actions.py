def enter_student_information():
    final_average=0
    sum_of_grades=0
    student_data={
        "full_name":"",
        "section":"",
        "spanish_grade":0,
        "english_grade":0,
        "social_studies_grade":0,
        "science_grade":0
        }
    for key in student_data.keys():
        if(key=="full_name" or key=="section"):
            student_data[key]=input(f"Enter {key}:")
        else:
            while(True):
                try:
                    valid_grade=float(input(f"Enter {key}:"))
                    if(valid_grade>=0 and valid_grade<=100):
                        student_data[key]=valid_grade
                        sum_of_grades+=valid_grade
                        break
                    else:
                        print("Enter a valid grade...")
                except ValueError as error:
                    print(f'The number selected is invalid. Error: {error}')
    final_average=sum_of_grades/4
    student_data['final_average']=final_average   
    return student_data


def view_all_students(students_info):
    try:
        student_info=[]
        for item in students_info:
            print(list(item.values()))
    except IndexError as ex:
        print(f"The index is out of range.Error: {ex}")
    
    
def view_top_three_students(students_info):
    try:
        average_list=[]
        for item in students_info:
            average_list.append(float(item["final_average"]))
        average_list.sort(reverse=True)
        for element in average_list[:3]:
            for item in students_info:
                if(float(item["final_average"])==element):
                    print(f"{item['full_name']} {item['final_average']}")
    except IndexError as ex:
        print(f"The index is out of range.Error: {ex}")
    

def calculate_average_grade(students_info):
    try:
        if not students_info:
            return 0
        else:
            sum_total=0
            average=0
            for item in students_info:
                sum_total+=float(item["final_average"])
            average=sum_total/len(students_info)
            return average
    except IndexError as ex:
        print(f"The index is out of range.Error: {ex}")
