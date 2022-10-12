import copy
# def append(appname):
#     appname.append("hello")
#     return 2

# spam = [1, 2, 3, 4]
# print(spam)
# append(spam)
# print(spam)

##this is what being a mutable value means
# spam = [1,2,3]
        # cheese = spam
        # cheese.append("helo")
        # print(spam)
##The change I made to the variable cheese, also changed the variable spam, because the variable spam
##    doesn't actually evaluate to the list inside of it, it references a list that the variable
##    cheese also references inside the computer memory

def plastic(cheese):
    return  cheese.insert(1, "Taha")    
    
milk = ["Calcium", "protein", "fats", "carbohydrates"]
cheese =copy.deepcopy(milk)
plastic(milk)
print("I have copied the milk variable which contains a list into the cheese variable"+ \
    "using the copy module's function 'deep copy' ")
print(milk, "This is the milk variable right now")
print(cheese, "this is the cheese variable right now")

