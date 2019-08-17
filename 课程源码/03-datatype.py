
"""
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


# 内置函数
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
"""


## number

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

