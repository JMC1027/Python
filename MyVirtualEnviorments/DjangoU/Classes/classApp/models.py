from django.db import models

class DjangoClasses(models.Model):#Class name
    Title = models.CharField(max_length=60, default="", blank=True, null=False)#setting title to sting value
    Course_Number = models.IntegerField(default="")#integer value
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)#String value
    Duration = models.FloatField(default="")#float value

# first object assigning atribute values to the course variables
obj1 = DjangoClasses(
Title = "Biology", Course_Number = 101, Instructor_Name = "Mr. Sanders", Duration = 10.0)
# saves the first object to the database
obj1.save()
# second object
obj2 = DjangoClasses(
Title = "Math", Course_Number = 321, Instructor_Name = "Mr. Bondstein", Duration = 30.0)
# saves the second object to the database
obj2.save()
# third object
obj3 = DjangoClasses(
Title="Science", Course_Number=201, Instructor_Name="Mr. Smith", Duration=20.0)
obj3.save()

objects = models.Manager()

def __str__(self):
    return self.name

