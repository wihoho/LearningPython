class Circle():
    def __init__(self, radius):
        if radius < 0:
            raise RuntimeError("Negative radius")
        else:
            self.__radius = radius

try:
    circle = Circle(-1)
except RuntimeError as ex:
    print(ex)