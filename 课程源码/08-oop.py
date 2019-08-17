
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