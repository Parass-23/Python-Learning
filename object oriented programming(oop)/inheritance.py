#parent class-->the class we are inheriting from-->base class
#child class-->the class that inherits from another class -->derived class
class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def show(self):
        print(self.firstname,self.lastname)

p1=person("paras","nagdeve")
p1.show()

class student(person):
    pass

s1=student("paras","nagdeve")
s1.show()
