from itertools import count
import pprint


paragraph = "Hello and welcome to my summer day at the beach house with "\
"Taha, today we are going to watch an umbrella fall down"

dic = {}
for i in paragraph:
    dic.setdefault(i, 0)
    dic[i] = dic[i] + 1
pprint.pprint(dic)