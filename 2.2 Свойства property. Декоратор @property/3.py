"""

"""

class StackObj:




class Stack:

    def __init__(self,data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self,obj):
        self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        self.__data = obj


