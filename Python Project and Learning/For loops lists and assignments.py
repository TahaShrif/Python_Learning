spam = 14
spam += 1
spam
15
spam += 123
spam
138
spam /= 25
spam
5.52
spam -= 0.52
spam = int(spam)
print(spam)
for i in range(50):
    spam += 1
    print(spam)
    if spam == 25:
        break