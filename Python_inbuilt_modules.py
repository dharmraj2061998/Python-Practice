# there are lot of python 3 inbuilt modules for reuse you can search it 
# online and make use of it . Nobody knows all built in python modules.

# Here we are generating random values with the use of built in python module.

# import random
# for i in range(3):
#     print(random.random())
#     print(random.randint(10,20))

# members = ['Vasu','DJ','Hemant','Rushi','Gaurav']
# print(random.choice(members))

# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return(first,second)


# dice1 = Dice()
# print(dice1.roll())

from pathlib import Path

# Absolute path - from root of our hard- disc c:\Program_files\Microsoft  
# Relative path - path starting from current directory 
path = Path() # to check where given directory exists or not.
# print(path.exists())
# path = Path("emails") 
# print(path.mkdir()) # to make the new directory.
# print(path.rmdir()) # to remove the directory.
for file in path.glob('*.py'):
    print(file) # by print it gernerates an object  and by for loops it shows files.
    
