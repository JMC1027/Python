

#parent class
class School:
    name = "Florida State University"
    location = "Florida"
    major = "Multiple"
    category = "University"

    def schoolInfo(self):
        entry_name = input("Enter the schools name: ")
        entry_location = input("Enter the schools location: ")
        entry_major = input ("Enter the schools Majors: ")
        entry_category = input("Enter the category of school this is: ")
        if (entry_location == self.location and entry_major == self.major):
            print("This school is called {}".format(entry_name))
        else:
            print("This school is invalid")

#1st child class
class Student(School):
    gpa = 4.0
    living = "On or Off Campus"

    def schoolInfo(self):
        entry_name = input("Enter the schools name: ")
        entry_location = input("Enter the schools location: ")
        entry_major = input ("Enter the schools Majors: ")
        entry_gpa = input("what is the current sudents GPA: ")
        if (entry_location == self.location and entry_gpa == self.gpa):
            print("The Students GPA is 4.0".format(entry_name))
        else:
            print("The students GPA is below 4.0".format(entry_gpa))

#2nd child class
class Teacher(School):
    subject = "History"
    email = "Jdoe.FS@FS.com"

    def teacherInfo(self):
        entry_name = input("Enter the schools name: ")
        entry_location = input("Enter the schools location: ")
        entry_major = input ("Enter the schools Majors: ")
        entry_resource = input("Your teacher is a great resource: ")
        if (entry_location == self.location and entry_resource == self.resource):
            print("The teachers are a viable resource for all your questions".format(entry_name))
        else:
            print("Leave an email and the teacher will get back to you")

if __name__ == "__main__":
    student = Student()
    print(student.schoolInfo())

    teacher = Teacher()
    print(teacher.schoolInfo())
            
        
        
        
    
    
