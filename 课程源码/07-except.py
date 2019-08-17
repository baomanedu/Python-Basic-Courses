try: 
    #int("2w3w")
    print("aaa")
except ValueError:
    print("语法错误")  
else:
    print("ok")  
finally:
    print("hello")



a = "123"
b = "456"

if a < b :
    raise Exception("error!")