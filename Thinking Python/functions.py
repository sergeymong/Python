class Square:
    def __init__(self, height=1, angle='+', brick_wall='|', brick_base='-'):
        self.height = height
        self.angle = angle
        self.brick_wall = brick_wall
        self.brick_base = brick_base
        self.base = ' '.join(self.brick_base * self.height)
        self.wall = self.brick_wall + ' ' * (len(self.base) + 2) + self.brick_wall

    def build_wall(self, figure):
        for _ in range(self.height):
            figure = '\n'.join([figure, self.wall])
        return figure

    def f_square(self):
        """Get full square."""
        figure = ' '.join([self.angle, self.base, self.angle])
        figure = self.build_wall(figure)
        figure = '\n'.join([figure, ' '.join([self.angle, self.base, self.angle])])
        return figure

    def r_square(self):
        """Get right square."""
        self.wall = ' ' * (len(self.base) + 1) + self.brick_wall
        figure = ' '.join([self.base, self.angle])
        figure = self.build_wall(figure)
        figure = '\n'.join([figure, ' '.join([self.base, self.angle])])
        return figure

    def b_square(self):
        """Get bottom square."""
        figure = ''
        figure = self.build_wall(figure)
        figure = '\n'.join([figure, ' '.join([self.angle, self.base, self.angle])])
        return figure

    def br_square(self):
        """Get bottom right square."""
        self.wall = ' ' * (len(self.base) + 1) + self.brick_wall
        figure = ''
        figure = self.build_wall(figure)
        figure = '\n'.join([figure, ' '.join([self.base, self.angle])])
        return figure

    def null_square(self, sq_type='f'):
        """Get null square."""
        self.angle = ''
        self.brick_wall = ''
        self.brick_base = ''
        self.base = ' '.join(self.brick_base * self.height)

        if sq_type == 'f':
            self.wall = self.brick_wall + ' ' * (len(self.base) + 2) + self.brick_wall
            return self.f_square()
        if sq_type == 'r':
            self.wall = ' ' * (len(self.base) + 2) + self.brick_wall
            return self.r_square()
        if sq_type == 'b':
            self.wall = self.brick_wall + ' ' * (len(self.base) + 2) + self.brick_wall
            return self.b_square()
        if sq_type == 'br':
            self.wall = ' ' * (len(self.base) + 2) + self.brick_wall
            return self.br_square()

def cbind_square(*args):
    return ''.join([*args])


def rbind_square(square_1, square_2):
    if square_1 == '' or square_2 == '':
        return max(square_1, square_2)

    count_height = lambda s: s.count('|') / 2 if s.count('|') % 2 == 0 else s.count('|')
    height_1 = count_height(square_1)
    height_2 = count_height(square_2)

    if height_1 > height_2:
        size = square_1.split('\n')[0].count('-')
        squares = 0 if height_2 == 0 else int(height_1 / height_2) - 1
        square_2 = cbind_square(square_2, Square(height=size).null_square('br') * squares)
    elif height_2 > height_1:
        size = square_2.split('\n')[0].count('-')
        squares = 0 if height_1 == 0 else int(height_2 / height_1) - 1
        square_1 = cbind_square(square_1, Square(height=size).null_square('br') * squares)

    sq_1 = square_1.split('\n')
    sq_2 = square_2.split('\n')
    figure = ''

    for row in range(len(sq_1)):
        if row == 0:
            sep = ''
        else:
            sep = '\n'
        figure = sep.join([figure, ' '.join([sq_1[row], sq_2[row]])])
    return figure


def print_grid(squares=1, height=1):
    from math import sqrt

    s = Square(height=height)
    figure = ''
    full_squares = int(sqrt(squares))
    residual_squares = squares - full_squares ** 2
    right_squares = full_squares if residual_squares > full_squares else residual_squares
    bottom_squares = residual_squares - right_squares

    if full_squares == 1:
        figure = s.f_square()

    for col in range(full_squares - 1):
        if col == 0:
            figure = rbind_square(
                cbind_square(s.f_square(), s.b_square() * (full_squares - 1)),
                cbind_square(s.r_square(), s.br_square() * (full_squares - 1))
            )
        else:
            figure = rbind_square(
                figure,
                cbind_square(s.r_square(), s.br_square() * (full_squares - 1))
            )

    if right_squares > 0:
        figure = rbind_square(
            figure,
            cbind_square(s.r_square(), s.br_square() * (right_squares - 1))
        )

    if bottom_squares > 0:
        ns = Square(height=height)
        figure = cbind_square(
            figure,
            rbind_square(ns.b_square(), s.br_square() * (bottom_squares - 1))
        )
    print(figure)
    return None


for i in range(10):
    print_grid(i, height=2)
    print()
