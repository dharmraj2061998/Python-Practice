# this is Modules file which imports converter module.
from operator import imod
from sqlite3 import converters
import Converters
from Functions import square

print(Converters.kgs_to_lbs(78))
print(Converters.lbs_to_kgs(115))
print(square(3))
numbers = [ 10,21,3,4,7,8,100]
print(Converters.find_max(numbers))
print(max(numbers)) # max is built in function. The color of built in function is same as print function.
# Modules are other files from which we can import the functions, variables, data
# by import keyword and also we can import specific thing by using word from.