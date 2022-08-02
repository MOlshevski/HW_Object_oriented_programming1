import math  # Importing the math module


class Sphere:  # Creating a class
    def __init__(self, radius=5, coordinate_x=3, coordinate_y=4, coordinate_z=2):  # Creating a constructor
        self.radius = radius
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_z = coordinate_z

    def get_volume(self):  # Creating methods
        print(f'Площадь шара = {4 * self.radius ** 3 * math.pi}')

    def get_square(self):
        print(f'Площадь внешней поверхности сферы = {(2 * self.radius) ** 2 * math.pi}')

    def get_radius(self):
        print(f'Радиус сферы = {self.radius}')

    def get_center(self):
        print(f'Координаты центра: {self.coordinate_x} - По оси x, {self.coordinate_y} - '
              f'По оси y, {self.coordinate_z} - По оси z')

    def set_radius(self):
        self.radius = int(input('Введите значение радиуса - '))

    def set_center(self):
        self.coordinate_x = int(input('Введите координаты по оси x - '))
        self.coordinate_y = int(input('Введите координаты по оси y - '))
        self.coordinate_z = int(input('Введите координаты по оси z - '))

    def is_point_inside(self):
        if self.coordinate_x >= int(input('Координаты оси х - ')) and \
                self.coordinate_y >= int(input('Координаты оси y - ')) and \
                self.coordinate_z >= int(input('Координаты оси z - ')):
            print('True')
        else:
            print('False')


print('Выберите метод класса:\n'  # Output of the methods
      ' 1. Площадь шара\n'
      ' 2. Площадь внешней поверхности сферы\n'
      ' 3. Радиус сферы\n'
      ' 4. Координаты центра\n'
      ' 5. Находится ли точка внутри сферы\n'
      ' 6. Задать значение радиуса\n'
      ' 7. Задать координаты центра'
      '\nЕсли желаете выйти нажмите "Enter"')
while True:  # Infinite cycle to select a method or exit the program
    a = input('Сделайте Ваш выбор - ')
    if a == '':
        print('\nДо свидания!')
        break
    if a == '1' or a == '1.' or a == 'Площадь шара' or a == '1. Площадь шара':
        Sphere(int(input('Введите значение радиуса - '))).get_volume()
    elif a == '2' or a == '2.' or a == 'Площадь внешней поверхности сферы' or \
            a == '2. Площадь внешней поверхности сферы':
        Sphere(int(input('Введите значение радиуса - '))).get_square()
    elif a == '3' or a == '3.' or a == 'Радиус сферы' or a == '3. Радиус сферы':
        Sphere().get_radius()
    elif a == '4' or a == '4.' or a == 'Координаты центра' or a == '4. Координаты центра':
        Sphere().get_center()
    elif a == '5' or a == '5.' or a == 'Находится ли точка внутри сферы' or \
            a == '5. Находится ли точка внутри сферы':
        Sphere().is_point_inside()
    elif a == '6' or a == '6.' or a == 'Задать значение радиуса' or \
            a == '6. Задать значение радиуса':
        Sphere().set_radius()
    elif a == '7' or a == '7.' or a == 'Задать координаты центра' or \
            a == '7. Задать координаты центра':
        Sphere().set_center()
    else:
        print('Выберите метод из предложенных')