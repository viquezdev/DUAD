total_grades=0
grade_counter=1
current_grade=0
passed_grades_count=0
failed_grades_count=0
passed_grades_average=0
failed_grades_average=0
overall_grades_average=0
total_grades=int(input("Enter the total number of grades: "))
while(grade_counter<=total_grades):
    current_grade=int(input((f"Enter grade number {grade_counter}: ")))
    if(current_grade<70):
        failed_grades_count+=1
        failed_grades_average+=current_grade
    else:
        passed_grades_count+=1
        passed_grades_average+=current_grade
    overall_grades_average+=(current_grade/total_grades)
    grade_counter+=1
if(failed_grades_count>0):
    failed_grades_average=failed_grades_average/failed_grades_count
if(passed_grades_count>0):
    passed_grades_average=passed_grades_average/passed_grades_count
print(f"The student has this number of passed grades {passed_grades_count}")
print(f"This is the average of passed grades {passed_grades_average}")
print(f"The student has this number of failed grades {failed_grades_count}")
print(f"This is the average of failed grades {failed_grades_average}")
print(f"This is the overall grade average {overall_grades_average}")