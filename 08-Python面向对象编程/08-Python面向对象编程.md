# 面向对象编程
## 面向对象编程介绍
## 类和对象
   - 创建类
   - 实例化
   - self参数
   - 类变量
   - 实例变量
```python
#first class

class Car:
    brand = "baoma"
    color = "red"

    def run(self,s):
        print("当前车速为:",s,"km/h")


test = Car()

print(test.brand)
test.color = "blue"
print(test.color)

test.run(60)
```



## 继承类
   - 单继承
   - 多继承
   - 方法重载
   - super函数
   - 访问权限
## 类的内置属性