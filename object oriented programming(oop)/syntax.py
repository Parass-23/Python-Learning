# class classname:#class
#     x=10
# p1=classname()#object
# print(p1.x)
#-------------------------------------
class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display(self):
        print(self.name, self.age, self.city)


p1 = person("paras", "18", "mumbai")
p2 = person("pramod", "49", "mumbai")

p1.display()
p2.display()