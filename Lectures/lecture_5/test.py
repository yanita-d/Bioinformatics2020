lang = ["python", "java", "c++"]

grt_3 = (lambda x: x > 3)

print(grt_3(1))

print([len(s) for s in lang])

for s in lang:
    if s == "python":
        print(s +" - "+ str(len(s)))

print([len(s) for s in lang if s == "python"])


class Car:
    engine = "v12"
    __price_engine = 100
    __price_over = 200

    def __init__(self, model):
        self.model = model

    def calculatePrice(self):
        return __price_engine + __price_over

    @property
    def getModel(self):
        print(self.model)

    def __eq__(self, value):
        return self.engine == value.engine


try:
    raise NameError('Why hello there!')  
except NameError:
    print("name error is raised")

mcar = Car("fort")
f1car = Car("ferr")

mcar.getModel()

mcar.engine = "v8"
print("Program End")

