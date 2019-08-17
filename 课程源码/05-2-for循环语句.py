#For  循环语句

students = ["aa","bbb","ccc","ddd"]

for i in students:
    print("students's name is {0}".format(i))

    for index in range(len(students)):
        if students[index] == i:
            print(index)




for name,age in {"aa":'bb'}:
    print(name,age)
    