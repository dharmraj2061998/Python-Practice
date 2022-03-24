class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    
    def draw(self):
        print("draw")

point = Point(10,20)
print(point.x)
print(point.y)

class Person_inf:
    def __init__(self, name): # here init function is used as constructor.
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name} how are you ?")

person = Person_inf("Jeevan")

person.talk()
print(person.name)

Rishi = Person_inf("Rishi")
Rishi.talk()