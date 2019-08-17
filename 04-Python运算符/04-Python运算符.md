# Python运算符

## 算数运算符
```
+   加法运算
-   减法运算
*   乘法运算
/   除法运算
%   模运算
**  幂运算
//  整除运算
```
### 实验笔记
```#算数运算符

numOne = 10
numTwo = 20

print("numOne + numTwo = %d" %(numOne + numTwo) )
print("numOne - numTwo = %d" %(numOne - numTwo) )
print("numOne * numTwo = %d" %(numOne * numTwo) )
print("numOne / numTwo = %d" %(numOne / numTwo) )
print("numOne % numTwo = {0}".format(numOne % numTwo ) )
print("numOne ** numTwo = %d" %(numOne ** numTwo))
print("numTwo  // numOne = %d" %(numTwo // numOne) )
```


## 比较运算符
```
==  等于运算符
!=  不等于
>   大于
<   小于
>=  大于等于
<=  小于等于

返回值是布尔类型  True False
```

### 实验源码
```
#比较运算符
number1 = 123
number2 = 456

#todo
print("number1 == number2 is ---> {0}".format(number1 == number2))
print("number1 != number2 is ---> {0}".format(number1 != number2))
print("number1 > number2 is ---> {0}".format(number1 > number2))
print("number1 < number2 is ---> {0}".format(number1 < number2))
print("number1 >= number2 is ---> {0}".format(number1 >= number2))
print("number1 <= number2 is ---> {0}".format(number1 <= number2))
```

## 赋值运算符

```
=  将右侧的值分配给左侧
+= 先相加然后将结果赋值给左侧
-= 先相减然后将结果赋值给左侧
*= 先相乘然后将结果赋值给左侧
/= 先相除然后将结果赋值给左侧
%= 先求模然后将结果赋值给左侧
**= 先幂运算然后将结果赋值给左侧
//= 先整除然后将结果赋值给左侧 
```

### 实验源码
```#赋值运算符

result = 10

print(result)


num1 = 10 
num2 = 20

num1 = num2
print("num1 = num2 ---> {0} ".format(num1))

num1 += num2
print("num1 += num2 ---> {0}".format(num1))

num1 -= num2 
print("num1 -= num2 ---> {0}".format(num1))

num1 *= num2 
print("num1 *= num2 ---> {0}".format(num1))

num1 /= num2 
print("num1 /= num2 ---> {0}".format(num1))

num1 %= num2
print("num1 %= num2 ---> {0}".format(num1))

num1 **= num2
print("num1 **= num2 ---> {0}".format(num1))

num1 //= num2 
print("num1 //= num2 ---> {0}".format(num1))
```

### 控制台输出
```
10
num1 = num2 ---> 20 
num1 += num2 ---> 40
num1 -= num2 ---> 20
num1 *= num2 ---> 400
num1 /= num2 ---> 20.0
num1 %= num2 ---> 0.0
num1 **= num2 ---> 0.0
num1 //= num2 ---> 0.0
```
## 逻辑运算符
```
and  逻辑与  两边所有为True 则True 否则 False
or   逻辑或  两边任意为True 则True 否则False
not  逻辑非  如果为True 则为False 变量为False 返回True
```

### 实验源码
```
A = True
B = False

print("A and B ---> {0}".format(A and B))
print("A or B ---> {0}".format( A or B))
print("not A ---> {0}".format(not A))
print("not B ---> {0}".format(not B))
```
### 控制台输出
```
A and B ---> False
A or B ---> True
not A ---> False
not B ---> True
```

## 成员运算符
```
in  存在 返回True False
not in  不存在 True False
```

### 实验 源码

```
# 成员运算符

student = ["zhangsan","lisi","wangwu"]

print("xiaoming is my student ? -->{0}".format("xiaoming" in student))
print("xiaohua is not my student ? -->{0}".format("xiaohua" not in student))
print("zhangsan is my student? -->{0}".format("zhangsan" in student))
```

### 控制台输出
```
xiaoming is my student ? -->False
xiaohua is not my student ? -->True
zhangsan is my student? -->True
```


## 身份运算符
```
is  如果两个对象为同一个内存地址返回True false
is not  不相同返回True  false
```

### 实验源码
```
#身份运算符

num1 = 10
num2 = 10

print("num1 is num2 --> {0}".format(num1 is num2))
print("num1 is not num2 --> {0}".format(num1 is not num2))

a = "123"
b = "123"
print("a  is b --> {0}".format(a is b))
```

### 控制台输出
```
num1 is num2 --> True
num1 is not num2 --> False
a  is b --> True
```

## 位运算符

```
&  位于运算
|  位或运算
^  异或运算
~  位取反

```
### 实验源码
```
#位运算符
num1 = 1000101
num2 = 10101

print("num1 & num2 = {0}".format(num1&num2))
print("num1 | num2 = {0}".format(num1|num2))
print("num1 ^ num2 = {0}".format(num1^num2))
print("~num1 = {0}".format(~num1))
print("~num2 = {0}".format(~num2))
```
### 控制台输出
```
num1 & num2 = 549
num1 | num2 = 1009653
num1 ^ num2 = 1009104
~num1 = -1000102
~num2 = -10102
```


## 运算符优先级
```
**
~ + -
* / % //
+ - 
>> <<
&
^|
<= <> >=
= %= /+= //= -+ += *= **=
is is not
in not in
not or and  
```
