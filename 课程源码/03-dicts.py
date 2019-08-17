#定义

a = {}
print(type(a))

myinfo = {"name":"zhangsan","age":45}
print(myinfo)
print(myinfo['name'])

myinfo["job"] = "devops1"    #增加、修改元素
print(myinfo)



#内置函数
myinfo = {"name":"zhangsan","age":45}

#print(myinfo.clear())   #清空字典
print(myinfo)

data1 = myinfo.copy()   #复制一个独立的副本
print(data1)

data1["name"] = "lisi"
print(data1)
print(myinfo)

print(myinfo.get("name"))  #获取key 的值

print(myinfo.items())  #格式化将key和value组合成元组并存放到列表中
print(type(myinfo.items()))

print(myinfo.keys())   #获取所有的key
print(myinfo.values())  #获取所有的value

print(myinfo.pop("name"))  #通过key删除键值对
print(myinfo)
