import time
spam = ["Shrif", "Mom", 'idiot', "Hema", 'Taha']
while "idiot" in spam:
    try:
        print(spam)
        idiotdel = input("Remove the word idiot from the list, please: ")
        spam.remove(idiotdel)
    except ValueError:
        print("       ERROR: The name you entered is not even in the list    ")
#This is for the case of the user deleting values other than idiot:
print("Hell yeah you did it")
if "Shrif" or "Mom" or "Hema" or "Taha" not in spam:
    time.time()
    time.sleep(0.8)
    print("You do know that i'm bringing back the other values that you deleted, right?")
    spam = ['Shrif', 'Mom', 'Hema', 'Taha']
time.sleep(0.5);print("Ok so the list now is: ",spam)


names = ['Alice', "Mark", "Taha", "dog", "Camera","Hello kitty",'wEIRD SHIT','alice', "bonasf", 'taha']
##This is for True Alphabetical order: List.sort(key=str.lower)
names.sort(key=str.lower)
# print(names)