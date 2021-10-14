

class School: #Parent
    def __init__(self, school):
        self._school = school#protected attribute
        self.__name = 'Florida State'#private attribute

    def schoolname(self):#using self to call on private attribute to return set value
        return self.__name #returns private attribute outside of class

    def setname(self, school): #this function is used so we can change the private attribute 
        self.__name = school #self._name is now equal to school

obj = School('Georgetown')#school now has a value = Georgetown which changed from the origonal value Florida State
print(obj._school)#printing new value set for school = Georgetown
school_name = obj.schoolname()#setting variable team_name to return value of the private attribute fuction getname 
print(school_name)#Florida state will now be returned 

obj.setname('University of Georgia')#University of Georgia is the return value of the function setname
school_name = obj.schoolname() #since the function setname is = 'University of Georgia', team_name = obj.getname will return the value of 'University of Georgia'
print(school_name)#University of Georgia get returned
