# Python数据类型
## 字符串类型

- 字符串是通过一个或多个元素组成的序列。
- 字符串一般使用的 单引号，双引号，三单引号，三双引号标识。

### 转义符

r 禁用转义符号

- \n 换行
- \b 退格
- \r 回车
- \t 制表符
- \? 一个问号

### 练习代码

```python
str1 = "Hello World !"
str2 = '''   ssss
sssssss'''
print(str1,str2)
str3 = "你好 中国"
print(str3)


#切片
str4 = "hello I am zhangsan!"
print(str4[8])
print(str4[:5])  #终止位置不包含第五个元素，起始位置0可以省略。
print(str4[5:])    #起始位置包含第五个元素，起始位置0可以省略。
print(str4[-10:-1])


#拼接
str5 = "Hello"
str6 = "World !"
str7 = "123"
print(str5 + ' ' +  str6 + str7) # 字符拼接不能是int类型


#字符串格式化
name = "zzzz"
age = 123

newage = str(age)     # str()用于转换成字符串
print(type(newage))

print("my name is %s, my age is %d" %(name,age))  # %s字符串  %d 数值

msg = "my name is {0}, my age is {1}".format(name,age) 
print(msg)


# 转义字符
new1 = r"abc \n cba"
print(new1)

```

### 内置函数
- capitalize()  
- count()
- decode()
- encode()
- endswith()
- startswith()
- find()
- index()
- isalpha()
- lstrip()/rstrip()/strip()
- replace()
- upper()
- split()


```python
reponse = "  abcd123  45abcd  "
print(reponse.capitalize())   #将字符串开头字母大写
print(reponse.count('b',2,len(reponse)))    #统计元素出现的次数,参数： 元素，起始位置，结束位置
print(reponse.encode(encoding="UTF-8"))   #以某种编码加密字符串
newreponse = reponse.encode(encoding="UTF-8")
print(newreponse.decode(encoding="UTF-8"))   #以某种编码解码字符串
print(reponse.startswith("b"))  # 判断字符串以某个元素开头，True、False
print(reponse.endswith("c"))    # 判断字符串以某个元素结尾，True、False
print(reponse.find("ac"))   # 根据某个元素进行查找，0、-1
print(reponse.index('b'))  #返回元素的索引，-1
print(reponse.isalpha())   #判断字符串中元素是否都是字母，True、False
print(reponse.lstrip())  #去掉字符串左侧空格
print(reponse.rstrip())  #去掉字符串右侧空格
print(reponse.strip())   #去掉字符串前后空格
print(reponse.replace("  ",""))  # 替换元素
print(reponse.upper())  #将字符串所有的字符转换成大写
print(reponse.split("  "))   #根据元素分割，列表
```



## 数字类型

### 分类
- 整型
- 布尔型
- 浮点型
- 复数类型

### 运算符
` + - * / % ` 
`> = < >= <= ==`


### 练习代码

```python
age = 45    # 正整数
memory = -100   #负整数
a = 0x768A   #十六进制表示的正整数
print("my age is : %d, my memory is : %d" % (age,memory))
print(a)

a = True
b = False
print(int(a),int(b))

c = 1.2
d = 2.4 
print(c,type(d))


a = 123
b = 456


print("a + b = " + str(a+b) )
print("a - b = " + str(a-b))
print("a * b = " + str(a*b))
print("a / b = " + str(a /b) )


print("a > b " + str(a > b))
print("a < b " + str(a<b))

```

## 列表类型 list

### 内置函数
- append()
- count()
- extend()
- index()
- insert()
- pop()
- remove()
- reverse()


### 练习代码

```python
##定义
a = []
print(type(a))

numlist = [1,2,3,4,5,6]
strlist = ["a","b","c","d"]

print(numlist,strlist)

##获取list元素
print(numlist[3],strlist[2])
print(numlist[:5])
print(len(numlist))


## 应用
ipAddress = [r"192.158.0.1",r"192.168.0.2"]
print(ipAddress)

## 遍历
for ip in ipAddress:
    print(ip)

#内置函数

testHosts = ["aa","bb","cc","dd"]
t1 = ["dd","cc"]

testHosts.append("EE")   #末尾追加
print(testHosts.count('bb'))   # 计算元素出现的次数
print(testHosts.extend(t1))    # 扩展列表、合并列表
print(testHosts.index("EE"))   # 获取列表中元素的索引
testHosts.insert(5,"DD")  #列表中插入元素 ，参数： 索引，元素
print(testHosts)
print(testHosts.pop(2))   #根据索引删除元素，并返回被删元素
print(testHosts)
testHosts.remove("EE")  ##删除元素
print(testHosts)
testHosts.reverse()  #反向列表
print(testHosts)

```

## 元组类型

- 元组中元素是不可进行修改的

```python
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
```

## 字典类型

- key/value


### 内置函数
- clear()
- copy()
- get()
- items()
- keys()
- update()
- pop()
- values()


### 练习代码

```python
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

```


## 实战1- python格式化输出

```python

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

```

## 实战2- 列表增删改查

```python
## append
## remove  pop


students = ["zhangsan","lisi","wangwu"]


## 添加同学
newStudent = "aa"
students.append(newStudent)
print("class students is : %s " %(students,))

## 合并班级
twoStudents = ["cc","dd","ee"]
students.extend(twoStudents)
print("class students is : %s " %(students,))

## 换班
moveStudent = "wangwu"
students.remove(moveStudent)
print("class students is : %s " %(students,))

## 更新
studentName = "zhangsanfeng"
stuindex = students.index("zhangsan")
students[stuindex] = studentName
print("class students is : %s " %(students,))
```

## 实战3- 将json数据转换成字典

```python
import json 

## dict -> json
myinfo = {"name":"zhangsan","age":100}
jsonInfo = json.dumps(myinfo)
print(type(jsonInfo))

## json -> dict
dictInfo = json.loads(jsonInfo)
print(type(dictInfo))
print(dictInfo['age'])

## 
a = '{"name":"zhangsan"}'
print(json.loads(a))


```