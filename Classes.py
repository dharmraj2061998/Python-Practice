# In class naming convension we use camel casing in which first word of the name
# is capital
# Class is blueprint of object. just like an architecture which first draws the blueprint
# of any construction. He can use that same blueprint for another constructions also. like that
# we define class as blueprint of object which we use to create new objects by same class.


# Here we defining a class
class Point:
    def move(self):
        print("Move")
    
    def draw(self):
        print("draw")

# after that we are creating object below.
point1 = Point() #object created using class name with () parenthesis.
# now below we accessing properties of class using '.' operator.
point1.draw() # calling draw method of class point using . operator.
point1.move() # there are some inbuilt methods also present there.

point1.x = 10 # we can also give and access new properties to object
point1.y = 20 # like this x and y co-ordinates.
print(point1.x)
print(point1.y)

point2 = Point()
print(point2.x) # this will give an attribute error because
# we have given x and y attributes to only point1 object so we cant access
# it by using point2. 