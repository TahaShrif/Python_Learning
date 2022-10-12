# from os import sep


# spam = ["Shrif", "Khadega", "Taha", "Abood", "Ibrahim", "Mariam", "Amina"]
# # print(spam[0])

# Family = [spam, ["Amina", "Marwa", "Ahmed", "Khaled"]]
# # print(Family[1][-1], Family[0][2])

# # print(Family[0][0:4])
# Family[0:1] = "Taha"
# print(Family)

# try:

pets = ["cat", "rat", "dog", "bird", "parrot"]
#     print('Before: ' +pets)
#     pets[2:] = ['Taha', 'Hema', "Ahmed"]
#     print("After: " +pets)
# except (TypeError):
#     print("TypeError: Can't concatenate lists to a string")
#     print("overall: ", pets)
# print(pets)
# del pets[2]
# print(pets)
# del pets[2]
# print(pets)




spam = ["Taha",'Hema', 'Shit']
ham = ['Shrif', 1, 2, 3, 'Hi', 5]
# print(spam + list(str(ham[4])))
Enter = input()
while str(Enter) not in spam:
    print("False")
    print("Try again")
    Enter = input()
print("True")
 
