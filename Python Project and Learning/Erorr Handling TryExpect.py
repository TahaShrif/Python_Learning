try:
    print("How many school subjects do you have?")
    sub = input("Enter number of subjects here: ")
    if int(sub) < 0:
        print("Error: dude don't be an idiot, what do you mean a negative number of subjects?")
    elif int(sub) <= 7:
        print("Well, that's okay, not much not a little")
    elif int(sub) > 7:
        ("Tough luck man, sorry for you")
    
except ValueError:
    print("Error: Please enter a number")
