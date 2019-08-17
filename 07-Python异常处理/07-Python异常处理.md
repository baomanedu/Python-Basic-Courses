
# 异常处理

## 异常简介
    程序执行过程中，出现的错误。

## 错误与异常

## 异常处理
```python
try: 
    int("2w3w")
except ValueError:
    print("语法错误")    

print("hello")
```
## 抛出异常

```python
a = "123"
b = "456"

if a < b :
    raise Exception("error!")
```

## 自定义异常
## finally字句

```python
try: 
    #int("2w3w")
    print("aaa")
except ValueError:
    print("语法错误")  
else:
    print("ok")  
finally:
    print("hello")
```

```
aaa
ok
hello
```