# ЗАДАЧА С КУРСА ДЕНЬ 5
# пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник
#
# вычисляем периметр и площадь. выводим в консоль.
# можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами.

import math

class Shape(object):

    def __init__(self, *sides):
        sides_qty = len(sides)

        if (sides_qty < 1) and (sides_qty > 4):
            raise ValueError('Ошибка при инициализации фигуры! Кол-во сторон {}, а должно быть в диапазоне от 1 до 4.'.format(sides_qty))
        else:
            if sides_qty == 1:
                self.sides = [n for n in sides] * 4
            elif sides_qty == 2:
                self.sides = [n for n in sides] * 2
            else:
                self.sides = [n for n in sides]

    def _calc_per(self):
        return sum(self.sides)

    def print_sides(self, comment='Стороны фигуры'):
        print(comment,':',self.sides)

    def print_per(self, figure_name='фигуры'):
        print('Периметр {} = {}'.format(figure_name, self._calc_per()))


class Rectange(Shape):

    def _calc_sqr(self):
        return self.sides[0] * self.sides[1]

    def print_sqr(self):
        print('Площадь прямоугольника = {}'.format(self._calc_sqr()))


class Square(Rectange):

    def print_sqr(self):
        print('Площадь квадрата = {}'.format(self._calc_sqr()))


class Triangle(Shape):

    def __init__(self, *sides):

        sides_qty = len(sides)

        if sides_qty != 3:
            raise ValueError('Ошибка при инициализации треугольника! Кол-во сторон {}, а должно быть 3.'.format(sides_qty))
        else:
            self.sides = [n for n in sides]


        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]
        two_sides_sum = self.sides[0] + self.sides[1]

        if two_sides_sum <= larger_side:
            raise ValueError('Ошибка при инициализации треугольника! Со сторонами такой длины сторон построить треугольник невозможно!')

    def _calc_sqr(self):
        half_per = self._calc_per() / 2
        return math.sqrt(half_per * (half_per - self.sides[0]) * (half_per - self.sides[1]) * (half_per - self.sides[2]))

    def print_sqr(self):
        print('Площадь треугольника = {}'.format(self._calc_sqr()))

class Polygon(Shape):

    def __init__(self, *sides):

        sides_qty = len(sides)

        if sides_qty != 4:
            raise ValueError('Ошибка при инициализации четырехугольника! Кол-во сторон {}, а должно быть 4.'.format(sides_qty))
        else:
            self.sides = [n for n in sides]


        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]
        three_sides_sum = self.sides[0] + self.sides[1] + self.sides[2]

        if three_sides_sum <= larger_side:
            raise ValueError('Ошибка при инициализации четырехугольника! Со сторонами такой длины сторон построить четырехугольник невозможно!')

    def _calc_sqr(self):
        return 'Рассчитать площадь произвольного четырехугольника без знания 2 углов невозможно'

    def print_sqr(self):
        print(self._calc_sqr())



rect = Rectange(1,2)
rect.print_sides('Стороны прямоугольника')
rect.print_per('прямоугольник')
rect.print_sqr()

print('\n')
sqr = Square(5)
sqr.print_sides('Стороны квадрата')
sqr.print_per('квадрат')
sqr.print_sqr()

print('\n')

try:
    trgl = Triangle(5, 2, 3)
except Exception as e:
    print('ERROR', e)

trgl2 = Triangle(5, 2, 4)
trgl2.print_sides('Стороны треугольника')
trgl2.print_per('треугольник')
trgl2.print_sqr()

print('\n')

try:
    plgn = Polygon(5, 2, 1, 1)
except Exception as e:
    print('ERROR', e)

plgn2 = Polygon(5, 2, 4, 3)
plgn2.print_sides('Стороны четырехугольника')
plgn2.print_per('четырехугольник')
plgn2.print_sqr()