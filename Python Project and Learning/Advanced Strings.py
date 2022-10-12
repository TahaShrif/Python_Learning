##Just learned about escape characters and this is a demonstration of some of what 
## I've learned so far
# print("Using \n is for linebreaks,\
    # using \' is for quotes,\
    # using\"is for double quotes\n\
    # and using \t is for Tab(a big space, apparently)\n\
    #     also if you want to use a backslash you'll just tpe \\")

##Raw strings are strings that print out just like they are written
##It's used by typing r"string", like this:
# print(r"Your Email\Password is incorrect")

##Strings use indexes and other list commands:
spam = """"Taha was nine when he first discovered the magical tooth fairy,
 it was a gross being with no teeth at all,
 He also wasn't exactly a smart person....he was nine"""
print(spam[-4:])
if "person" in spam:
    print('The word "Person is in the variable spam"')
else:
    print("Simply false")