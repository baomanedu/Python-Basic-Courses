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