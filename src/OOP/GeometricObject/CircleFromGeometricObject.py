from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    
    def getAreaa(self):
        return self.__radius * self.__radius * math.pi


def main():
    circle = Circle(5)
    print("A circle", circle)
    print("The radisu is", circle.getRadius())
    print("The area is", circle.getAreaa())

main()