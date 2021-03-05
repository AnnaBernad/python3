# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def __repr__(self):
        return f'{self.name} {self.age} {self.size}'


class Prince(Human):
    def __init__(self, name, age, shsize):
        super().__init__(name, age)
        self.shsize = shsize

    def match(self, *princesses):
        for princess in princesses:
            if princess.size == self.shsize:
                return princess


prince = Prince("Oleg", "20", "38")
prin1 = Cinderella("Olena", "18", "39")
prin2 = Cinderella("Olga", "19", "38")
prin3 = Cinderella("Oksana", "21", "41")
prinall = [prin1, prin2, prin3]
print(prinall)




# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон


# class Rectangle():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return self.x * self.y + other.y * other.x
#
#     def __sub__(self, other):
#         return self.x * self.y - other.y * other.x
#
#     def __eq__(self, other):
#         return self.x * self.y == other.y * other.x and self.x * self.y != other.y * other.x
#
#     def __lt__(self, other):
#         return self.x * self.y < other.y * other.x
#
#     def __gt__(self, other):
#         return self.x * self.y > other.y * other.x
#     def __len__(self):
#         return self.x + self.y
#
#
# rec1 = Rectangle(6, 5)
# rec2 = Rectangle(2, 3)
# print(rec1 + rec2)
# print(rec1 - rec2)
# print(rec1 == rec2)
# print(rec1 != rec2)
# print(rec1 < rec2)
# print(rec1 > rec2)
# print(rec1.__len__())
# print(rec2.__len__())
