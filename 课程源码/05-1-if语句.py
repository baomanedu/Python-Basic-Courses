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