# 函数
## 函数定义与调用
- 函数： 一些语句块的集合封装，减少重复代码。

```python
def PrintMsg():
    print("Hello world!")

```

## 函数编写规范

```python
def print_msg():
    print("hello world!")

print_msg()
```
### 文档字符串

```python
def print_msg():
    """
    This is a function ! 
    print hello world! 
    """

    print("hello world!")
print_msg()


print(print_msg.__doc__)
```
### 函数注释

```python
#function

def print_msg(x:"这是一个数字"=0,y:"这是第二个数字"=0):
    """
    This is a function ! 
    print hello world! 
    """
    print("hello world!")
    print("x + y = {0} ".format(x+y))


print(dir(print_msg))

print(print_msg.__doc__)

print_msg(1,3)
print(print_msg.__annotations__)

```

```
hello world!
x + y = 4 
{'x': '这是一个数字', 'y': '这是第二个数字'}
```

## 函数参数
### 位置参数
```python
def print_mes(name,age):
    print("Your name is {0},Your age is {1}".format(name,age))

print_mes("zhangsan",29)
```

```python
def print_mes(name,age):
    print("Your name is {0},Your age is {1}".format(name,age))

print_mes(age=29,name="zhangsan")
```

```python
age=29
name="zhangsan"

def print_mes(name,age):
    print("Your name is {0},Your age is {1}".format(name,age))

print_mes(name,age)
```

### 默认参数
```python
def print_mes(name,age=0):
    print("Your name is {0},Your age is {1}".format(name,age))

print_mes("zhangsan")
```
### 关键字参数

```python
def print_mes(*test,**kw):
    print(test)
    print(kw)

print_mes("zhangsan","lisi","123",a=123,b=234,c=345)
```


```
('zhangsan', 'lisi', '123')
{'a': 123, 'b': 234, 'c': 345}`
```


### 练习

```python
scores = {"zhangsan":99,"lisi":89}

def select(name):
    if name in scores.keys():
        print("正在查询成绩--> {0}".format(name))
        print("{0}的成绩是:{1}".format(name,scores[name]))
    else:
        print("{0}的成绩还未整理".format(name))


select("lisi")


```