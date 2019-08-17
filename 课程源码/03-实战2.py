## append
## remove  pop


students = ["zhangsan","lisi","wangwu"]


## 添加同学
newStudent = "aa"
students.append(newStudent)
print("class students is : %s " %(students,))

## 合并班级
twoStudents = ["cc","dd","ee"]
students.extend(twoStudents)
print("class students is : %s " %(students,))

## 换班
moveStudent = "wangwu"
students.remove(moveStudent)
print("class students is : %s " %(students,))

## 更新
studentName = "zhangsanfeng"
stuindex = students.index("zhangsan")
students[stuindex] = studentName
print("class students is : %s " %(students,))
