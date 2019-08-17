#迭代器

#lterable

from collections import Iterable

num=456
print(isinstance(num, Iterable))

num1 = [1,2,3]
print(isinstance(num1, Iterable))



#enumerate

names = ['z','a','b']
print(enumerate(names))

for i,value in enumerate(names):
    print(i,value)


