# # List, tuple, Dictionary, Set are mainly used data structures in python
# # there are many other data stuctures but we work with this four built in data structures mainly

# customer = {
#     "name":"Dharmraj",
#     "age" : 24,
#     "is_student" : True
# }
# print(customer["name"])
# print(customer.get("name"))
# #print(customer['bdate']) #this line will give an error for resolving this use get method.
# print(customer.get("bdate")) # this method does not give you error but return none.
# print(customer.get("bdate", "20th June 1998")) - by giving the default value we can solve the error.
#  # we can add new key value pair to the dictionary.
# customer["bdate"] = "20-06-1998"
# print(customer["bdate"])

# Phone = input("Phone >")
# digits_mapping ={
#     "1":"one",
#     "2":"Two",
#     "3":"Three",
#     "4": "Four",
    
# }
# output =""
# for ch in Phone:
#     output += digits_mapping.get(ch,"!") +" "
# print(output)

