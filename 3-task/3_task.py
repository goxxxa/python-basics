'''
Создать иерархию классов Фигур: квадрат, прямоугольник, треугольник, круг. Каждый класс должен реализовывать следующие методы:

вычисление площади
вычисление периметра
сравнение площади с другой фигурой (больше или меньше)
сравнение периметра с другой фигурой (больше или меньше)
'''
from __future__ import annotations

from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):
    def __init__(self):
        self._perimeter: float | None = None
        self._area: float | None = None

    def get_area(self) -> float:
        if self._area is None:
            self._calculate_area()
        return self._area

    def get_perimeter(self) -> float:
        if self._perimeter is None:
            self._calculate_perimeter()
        return self._perimeter

    def __lt__(self, other: Shape):
        return self.get_area() < other.get_area()

    def __gt__(self, other: Shape):
        return self.get_area() > other.get_area()

    def __eq__(self, other: Shape):
        return self.get_area() == other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    @abstractmethod
    def _calculate_area(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def _calculate_perimeter(self) -> None:
        raise NotImplementedError()


class Square(Shape):

    def __init__(self, length: float):
        super().__init__()
        if length <= 0:
            raise ValueError('Сторона квадрата должна быть положительной')
        self.length = length

    def _calculate_perimeter(self) -> None:
        self._perimeter = 4 * self.length

    def _calculate_area(self) -> None:
        self._area = self.length ** 2


class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        super().__init__()
        if width <= 0 or height <= 0:
            raise ValueError("Длины сторон должны быть положительными")
        self.length = width
        self.height = height

    def _calculate_perimeter(self) -> None:
        self._perimeter = 2 * self.length + 2 * self.height

    def _calculate_area(self) -> None:
        self._area = self.length * self.height


class Circle(Shape):

    def __init__(self, radius: float):
        super().__init__()
        if radius <= 0:
            raise ValueError('Радиус должен быть положительным')
        self.radius = radius

    def _calculate_perimeter(self) -> None:
        self._perimeter = 2 * pi * self.radius

    def _calculate_area(self) -> None:
        self._area = pi * self.radius ** 2


class Triangle(Shape):
    '''
    Треугольник равносторонний
    '''

    def __init__(self, length: float):
        super().__init__()
        if length <= 0:
            raise ValueError('Сторона треугольника должна быть положительной')
        self.length = length

    def _calculate_perimeter(self) -> None:
        self._perimeter = 3 * self.length

    def _calculate_area(self) -> None:
        self._area = (self.length ** 2 * sqrt(3)) / 4


if __name__ == '__main__':
    square = Square(4)
    rectangle = Rectangle(4, 6)
    circle = Circle(3)
    triangle = Triangle(5)

    print(f'Площадь квадрата: {square.get_area()}')
    print(f'Периметр квадрата: {square.get_perimeter()}')

    print(f'Площадь прямоугольника: {rectangle.get_area()}')
    print(f'Периметр прямоугольника: {rectangle.get_perimeter()}')

    print(f'Площадь круга: {circle.get_area()}')
    print(f'Периметр круга: {circle.get_perimeter()}')

    print(f'Площадь треугольника: {triangle.get_area()}')
    print(f'Периметр треугольника: {triangle.get_perimeter()}')

    print('Сравнение площадей:')
    print(f'Прямоугольник vs Квадрат → {rectangle > square}')
    print(f'Квадрат vs Круг → {square <= circle}')

    print('Сравнение периметров:')
    print(f'Треугольник vs Квадрат → {triangle == square}')
    print(f'Круг vs Прямоугольник → {circle <= rectangle}')
