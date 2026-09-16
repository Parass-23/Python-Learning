class student:
    college="iit bombay"#class variable
    def __init__(self,name):
        self.name=name
s1=student("raj")
s2=student("paras")
s1.college="iit madras"#changing college for specific student
print(s1.name,s1.college)
print(s2.name,s2.college)