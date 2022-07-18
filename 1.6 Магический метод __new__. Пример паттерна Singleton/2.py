"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/uE1uf7Qtbh4

Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно.
"""

class SingletonFive:
    coun = 0
    s = None

    def __new__(cls,*args,**kwargs):
        if cls.coun<5:
            cls.s = super().__new__(cls)
            cls.coun += 1
        return cls.s

    def __init__(self,name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]
print(objs)