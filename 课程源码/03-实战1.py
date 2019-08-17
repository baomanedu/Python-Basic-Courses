
## % 
name = "zhangsan"
age = 45

print("my name is : %s , my age is %s" % (name,str(age)))  

## format

name = "lisi"
age = 34
print("my name is {0}, my age is {1}".format(name,age))


## title
info = """
name = {0}
age = {1}
high = {2}
jobs = {3}
address = {4}
"""
print("---------------------")
print(info.format("zhangsan",24,178,"PythonDeveloper","Beijing"))
print("---------------------")