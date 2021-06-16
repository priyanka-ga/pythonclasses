'''class employee(object):
    def __init__(self,employeeid,name,age,position):
        self.employeeid = employeeid
        self.name = name
        self.age =age
        self.position =position
    def get_name(self):
        return self.name
e=employee (1,"priyanka",23,"position")
print(e.get_name())'''


class employee(object):
    def __init__(self,name,rollnum,age):
        self.name = name
        self.rollnum =rollnum
        self.age = age
    def get_name(self): 
        return self.name
e=employee ("priyanka",1,"position")
print(e.get_name())
        
    