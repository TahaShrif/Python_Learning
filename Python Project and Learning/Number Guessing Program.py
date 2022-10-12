import random
print("Hello, What is your name")
name = input() #I know you're reading....bitch
print("Well " +name+ " , I had a number between 1 and 20 in mind, can you guess it?")
secretnumber = random.randint(1, 20)

#Debugging:
print(secretnumber)
for guesses in range(1,8):
    print("Guess")
    guess = int(input())
    if guess < secretnumber:
        print("Your number is too low")
    elif guess > secretnumber:
        print("Your number is too high")
    elif guess == secretnumber:
        break #This means you win
if guesses == 7 and guess != secretnumber:
    print("Sorry, you ran out of guesses, the number I was thinking of was " + str(secretnumber))
elif guess == secretnumber:
    print("congrats, you got it in " +str(guesses) + " guesses")

