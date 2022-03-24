# tuples are same as list but we cant modify tuple. cant remove the items from tuple.
# Tuples are immutable. 
# Mutable = can be changed or Modified
# Immutable = cant be changed or modified.

data = (1,2,3,4,5)
data [2] = "jeevan" # this line gives this type error = 'tuple' object does not support item assignment
                    # by which here we proved that tuple is immutable.
print(data[3])
print(data[1:])
print(data[3:])
print(data[-3:-1]) # if you want to access elements of list and tuple through - index then
                   # you have to give - index from left first then right.

names = tuple(["Dharm", "Gaurav", "Rushi", "Vasu"])
x,y,z,i = names # This is another method to access elements of tuple only not of list with use of variables.
print(x)
print(y)
print(z)
print(i) 

