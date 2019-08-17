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


#args



def print_mes(*test,**kw):
    print(test)
    print(kw)

print_mes("zhangsan","lisi","123",a=123,b=234,c=345)



#

scores = {"zhangsan":99,"lisi":89}

def select(name):
    if name in scores.keys():
        print("正在查询成绩--> {0}".format(name))
        print("{0}的成绩是:{1}".format(name,scores[name]))
    else:
        print("{0}的成绩还未整理".format(name))


select("lisi")