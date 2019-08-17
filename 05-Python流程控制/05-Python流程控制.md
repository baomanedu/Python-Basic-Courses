# 流程控制
## 代码块
是由多行语句组成，：开始。


## 条件判断语句
- If语句

```
if 条件 ：
    做事情
else:
    做事情


if 条件：
    做事情
elif 条件：
    做事情
else：
    做事情
```

### 实验代码
```
# if 语句

score = 60

students = {"zhangsan":80,"lisi":70,"wangwu":40}

if students["wangwu"] >= score:
    print("及格了")
elif students["zhangsan"] >= 80:
    print("你很优秀")
else:
    print("不及格")


a=True
b=True

if a == True:
    print(True)
    if b == 1:
        print(False)

```

### 输出
```
你很优秀
```


## 循环语句
### for循环语句
```
for 变量名 in 序列:
    todo

```

### 实验代码
```
#For  循环语句

students = ["aa","bbb","ccc","ddd"]

for i in students:
    print("students's name is {0}".format(i))

    for index in range(len(students)):
        if students[index] == i:
            print(index)
```

### 输出
```
students's name is aa
0
students's name is bbb
1
students's name is ccc
2
students's name is ddd
3
```


### while循环语句
```
while 条件=True:
    todo
```

### 实验代码

```
#while 语句

a = 11

while a >= 10 :
    for i in range(100):
        print(i)
        if i == 5:
            a = i
            print(a)
            
```

### break continue语句
- 跳出循环
- 跳出当前循环，继续下次循环

```
#break continue

for i in range(10):
    if i == 5:
        break    
    else:
        print(i)


for i in range(10):
    if i == 5:
        continue  
    else:
        print(i)

```


## 迭代器
### Iterable
```
#迭代器

#lterable

from collections import Iterable

num=456
print(isinstance(num, Iterable))

num1 = [1,2,3]
print(isinstance(num1, Iterable))
```

#### 输出
```
False
True
```

### enumerate
```
#enumerate

names = ['z','a','b']
print(enumerate(names))

for i,value in enumerate(names):
    print(i,value)
```
```
0 z
1 a
2 b
```


### 列表推导式

```
#列表推导式

numlist = []
for x in range(5):
    numlist.append(x)
print(numlist)

#
print([x for x in range(5)])
```

```
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
```