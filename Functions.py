# Simple function.
# def greet_user():
#     print("Hi there!")
#     print("welcome to program")

# print('start')
# greet_user()
# print("finish") 

# Function with argument.
def greet_user(f_name,l_name):  #we can assign multiple arguments to the function if we need it in function.
    print(f"Hi {f_name} {l_name}")
    print("wecome to program")

# greet_user("Dharm","Joshi")
# greet_user("Dharm") - if sometimes you pass just one parameter where you defined function using two arguments then it shows an error.
                        # about argument. This are positional arguments.where position of argument matters.
                        # for overcoming this issue you can use keyword argument.
# greet_user("Rushi","Tole")  # This process is called passing parameters to the function by calling it.

#  Kyeword Arguments
# greet_user(l_name ="Joshi", f_name="Dharm")
# because of this keyword arguments we need not to worry about position of arguments.
# You can use keyword argument with positional argument but you need to pass positional argument
# first and then keyword argument unless it will give error.
# Use keyword argument to improve readibility of code.

# Return keyword

def square (num):
    return num * num

# result = square(3)
# print(result)

# # or we can do it directly.

# print(square(3))

# if you dont have the return keyword in function but fuction has taking argument then it 
# shows output as None. Here is example.

# def square (num):
#     print( num * num)

# print(square(4))

