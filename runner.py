from itertools import repeat
from classes.school import School
from classes.student import Student

school = School('Ridgemont High')

# students = school.list_students()
while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()
    # i+=1
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
    # i +=1
    elif mode == '5':
        print("Logging Out!!")
        exit()
    else:
        print('Thats an invalid input!')

