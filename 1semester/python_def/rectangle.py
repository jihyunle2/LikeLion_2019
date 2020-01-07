class Rect:
    width = 0
    height = 0
    color = ""

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calc_area(self):
        area = self.width * self.height
        return area

    @staticmethod
    def is_square(rect_width, rect_height):
        return rect_width == rect_height

rect1=Rect(30,40)
print(rect1.width)
print(rect1.height)
print(rect1.calc_area())

rect2=Rect(50,20)
rect3=Rect(40,30)

rect1.color="blue"
rect2.color="pink"
rect3.color="red"

print(rect1.color)

square=Rect.is_square(30,30)
print(square)
