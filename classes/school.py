from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        temp_list = []
        student_list =''
        i = 0
        print("----Student Roster----")
        for student in self.students:
           i+=1
           temp_list.append(f'{i}. {student.name} {student.school_id}')
        student_list= '\n'.join(temp_list)
        print(student_list)   

    def find_student_by_id(self, student_id) :
        for student in self.students:
            if student.school_id == student_id :
                return student
            else:
                return ('No student found with that ID')

