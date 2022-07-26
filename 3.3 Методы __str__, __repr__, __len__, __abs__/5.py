"""

"""

class Complex:

    def __init__(self,real, img):
        self.__real = real
        self.__img = img

    def __abs__(self,x):
        return abs(x)

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self,value):
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value

    def __setattr__(self, key, value):
        if type(value) not in (int,float):
            raise ValueError("Неверный тип данных.")
        return object.__setattr__(self, key, value)
