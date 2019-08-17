
#定义
a = ()
print(type(a))

a = (1,2,3,4,5)
b = ("aa","bb","cc")

print(a,b)

#应用
test = ("java","tomcat","springboot")
print(test[1])
print(test[:2])

test1 = ([1,2,3],"aa")
print(test1)
test1[0].append(123)
print(test1)