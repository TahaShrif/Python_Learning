print("What is the name of the wizard in Lord of the rings?")
wizard = input(" Enter his name ")
while wizard != "Gandalf":
    print("no, that's not true")
    wizard = input("try again: ")
print("ok")

print("Can you guess how old I am?")
myage = int(input("Enter my age: "))
while int(myage) != 16:
    print("nooo")
    if int(myage) < 16:
        print("I'm not that young")
    elif int(myage) > 16:
        print("I'm not that old either")
    myage = input("try again ")
print("You got it right, well done")