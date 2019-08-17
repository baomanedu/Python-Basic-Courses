
##定义
a = []
print(type(a))

numlist = [1,2,3,4,5,6]
strlist = ["a","b","c","d"]

print(numlist,strlist)

##获取list元素
print(numlist[3],strlist[2])
print(numlist[:5])
print(len(numlist))


## 应用
ipAddress = [r"192.158.0.1",r"192.168.0.2"]
print(ipAddress)

## 遍历
for ip in ipAddress:
    print(ip)

#内置函数

testHosts = ["aa","bb","cc","dd"]
t1 = ["dd","cc"]

testHosts.append("EE")   #末尾追加
print(testHosts.count('bb'))   # 计算元素出现的次数
print(testHosts.extend(t1))    # 扩展列表、合并列表
print(testHosts.index("EE"))   # 获取列表中元素的索引
testHosts.insert(5,"DD")  #列表中插入元素 ，参数： 索引，元素
print(testHosts)
print(testHosts.pop(2))   #根据索引删除元素，并返回被删元素
print(testHosts)
testHosts.remove("EE")  ##删除元素
print(testHosts)
testHosts.reverse()  #反向列表
print(testHosts)
