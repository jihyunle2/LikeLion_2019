class Car:
    color = ""
    speed = 0

    def speedUp(self, value):
        self.speed += value
    def speedDown(self, value):
        self.speed -= value

myCar = Car()
myCar.speedUp(30)
print(myCar.speed)

myCar.speedDown(20)
print(myCar.speed)

myCar.color = "yellow"
print(myCar.color)