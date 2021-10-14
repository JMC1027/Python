

from abc import ABC, abstractmethod# abstraction method

class School(ABC): #parent
    def name(self, name):
        print("This schools name is: ", name)#passing in an unkown argument
    @abstractmethod
    def location(self, name):
        pass

class LocationOfSchool(School):#child
    def location(self, name):#implimenting the location function from the parent class
        print("The state this school is located is {} ".format(name))

obj = LocationOfSchool()
obj.name('Florida State')
obj.location('Florida')
