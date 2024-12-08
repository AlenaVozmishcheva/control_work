"""Используя понятие множественного наследования, разработайте класс «Окружность, вписанная в квадрат.
"""
import math



class Square:

    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

class InscribedCircle(Square, Circle):

    def __init__(self, square_side):
        Square.__init__(self, square_side)
        radius = square_side / 2
        Circle.__init__(self, radius)

    def circle_area_in_square(self):
        return self.area()


inscribed_circle = InscribedCircle(4)
print(f"Площадь квадрата:", inscribed_circle.area()) # Площадь квадрата
print(f"Площадь вписанной окружности:", inscribed_circle.circle_area_in_square()) # Площадь окружности


"""Используя механизм множественного наследования разработайте класс “Автомобиль”. Должны быть классы
«Колеса», «Двигатель», «Двери» и т.д."""


class Wheels:

    def __init__(self, number_of_wheels):
        self.__number_of_wheels = number_of_wheels

    def get_wheel_info(self):
        return f"Количество колес: {self.__number_of_wheels}"

class Engine:

    def __init__(self, horsepower):
        self.__horsepower = horsepower

    def get_engine_info(self):
        return f"Мощность двигателя: {self.__horsepower} л.с."

class Doors:

    def __init__(self, number_of_doors):
        self.__number_of_doors = number_of_doors

    def get_door_info(self):
        return f"Количество дверей: {self.__number_of_doors}"

class Car(Wheels, Engine, Doors):

    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

    def car_info(self):
        return self.get_wheel_info() + ", " + self.get_engine_info() + ", " + self.get_door_info()


my_car = Car(4, 150, 4)
print(my_car.car_info())


"""Создать базовый класс «Домашнее животное» и производные классы«Собака», «Кошка», «Попугай», «Хомяк».
С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого
из классов методы:
■ Sound — издает звук животного (пишем текстом в
консоль);
■ Show — отображает имя животного;
■ Type — отображает название его подвида;"""

class Pet:
    
    def __init__(self, name):
        self.__name = name

    def sound(self):
        pass

    def show(self):
        print(f"Имя: {self.__name}")

    def type(self):
        pass


class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Гав!")

    def type(self):
        return f"Собака"


class Cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Мяу!")

    def type(self):
        return f"Кошка"


class Parrot(Pet):
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Попугай говорит!")

    def type(self):
        return f"Попугай"


class Hamster(Pet):
    
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def sound(self):
        print("Хомяк писк!")

    def type(self):
        return f"Хомяк"




dog = Dog("Бобик", "Лабрадор")
cat = Cat("Мурка", "Сиамская")
parrot = Parrot("Кеша", "Зеленый")
hamster = Hamster("Хома", 2)


dog.show()
dog.sound()
print(f"Тип: {dog.type()} - Порода: {dog.breed}\n")


cat.show()
cat.sound()
print(f"Тип: {cat.type()} - Порода: {cat.breed}\n")


parrot.show()
parrot.sound()
print(f"Тип: {parrot.type()} - Цвет: {parrot.color}\n")


hamster.show()
hamster.sound()
print(f"Тип: {hamster.type()} - Возраст: {hamster.age} лет\n")


"""Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию о служащем. В случае 
базового класса это может быть строка c надписью This is Employer class. Создайте от него три производных класса: President,
Manager, Worker. Переопределите функцию Print() для
вывода информации, соответствующей каждому типу
служащего."""

class Employer:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def print_info(self):
        print(f"Имя: {self.__name}, фамилия: {self.__surname}, возраст: {self.__age}")

employer = Employer("Василий", "Петров", "32")
employer.print_info()

class President(Employer):

    def print_info(self):
        print(f"Информация о президенте:")
        super().print_info()

class Manager(Employer):

    def print_info(self):
        print(f"Информация о менеджере:")
        super().print_info()

class Worker(Employer):

    def print_info(self):
        print(f"Информация о работнике:")
        super().print_info()

president = President("Николай", "Васильев", "56" )
president.print_info()
print()
manager = Manager("Мария","Шишкина", "45")
manager.print_info()
print()
worker = Worker("Иван", "Иванов", "19")
worker.print_info()


"""Для классов из задания 4 реализуйте магический
метод str, а также метод int (должен возвращать возраст
служащего)"""

class Employer:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def print_info(self):
        print(f"Имя: {self.__name}, фамилия: {self.__surname}, возраст: {self.__age}")

    def __str__(self):
        return f"Имя: {self.__name}, фамилия: {self.__surname}, возраст: {self.__age}"

    def __int__(self):
        return self.__age

pres = President("Николай", "Васильев", "56" )
pres.print_info()
print(str(pres))
print(int(56))
manager = Manager("Мария","Шишкина", "45")
manager.print_info()
print(str(manager))
print(int(45))
worker = Worker("Иван", "Иванов", "19")
worker.print_info()
print(str(worker))
print(int(19))



