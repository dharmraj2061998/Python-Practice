# Inheritace is we not use in python its been used in all object oriented 
# programming language.
# Where we use class there is inheritance.
# In any programming we have to apply one rule as follows.
#DRY - Dont Repeat Yourself.

class Mamal:
    def walk(self):
        print("walk")


class Dog(Mamal):
    def bark(self):
        print("Bhau")


class Cat(Mamal):
    def be_annoying(self):
        print("annoying")

cat = Cat()
cat.be_annoying()
cat.walk()

dog = Dog()
dog.walk() 
dog.bark()

# This example shown inheritace beautifully.
