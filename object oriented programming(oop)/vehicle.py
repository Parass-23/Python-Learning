class vehicle:
    def __init__(self,brand):
        self.brand=brand

    def show(self):
        print("brand of car is : ",self.brand)

v1=vehicle("ROLLS ROYCE")#parent class 
v1.show()

class car(vehicle):#child class 
    engine="rolls 1"#class var
c1=car("ROLLS ROYCE")
c1.show()
print(c1.engine)

