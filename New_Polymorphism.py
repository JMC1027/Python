

#parent class
class School:
    name = "Florida State University"
    location = "Florida"
    majors = "Multiple"
    category = "University"

    def schoolInfo(self):
        entry_name = input("Enter the schools name: ")
        entry_location = input("Enter the schools location: ")
        entry_major = input ("Enter the schools Majors: ")
        entry_category = input("Enter the category of school this is")
        if (entry_location == self.location and entry_major == self.major):
            print("This school is called {}".format(entry_name))
        else:
            print("This school is invalid")

#1st child class
class Student(School):
    gpa = "4.0"
    living = "On or Off Campus"

    def schoolInfo(self):
        entry_name = input("Enter the schools name: ")
        entry_location = input("Enter the schools location: ")
        entry_major = input ("Enter the schools Majors: ")
        entry_gpa = input("Enter the students current GPA:")
        if (entry_location == self.location and entry_gpa == self.gpa):
            print("The Students GPA is 4.0".format(entry_name))
        else:
            print("The students GPA is below 4.0")

#2nd child class
class Teacher(School):
    subject = "History"
    email = "Jdoe.FS@FS.com"

    def teacherInfo(self):
        entry_name = input("Enter the schools name: ")
        entry_location = input("Enter the schools location: ")
        entry_major = input ("Enter the schools Majors: ")
        entry_email = input("Enter the teachers email: ")
        if (entry_location == self.location and entry_email == self.email):
            print("The teachers subject is Engineering".format(entry_subject))
        else:
            print("The teachers email is not listed")

if __name__ == "__main__":
    student = Student()
    print(student.schoolInfo())

    teacher = Teacher()
    print(teacher.teacherInfo())
            
        
        
        
    
    
