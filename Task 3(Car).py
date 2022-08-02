class Car:  # Creating a class
    def __init__(self, engine='off', color='brown', car_body_style='hatchback', year='2011'):  # Creating a constructor
        self.engine = engine
        self.color = color
        self.car_body_style = car_body_style
        self.year = year

    def engine_run(self):  # Creating methods
        if self.engine == 'on':
            print('Автомобиль заведен')

    def engine_shutdown(self):
        if self.engine == 'off':
            print('Автомобиль заглушен')

    def car_year(self):
        print(f'Автомобиль {self.year} года выпуска')

    def car_body_type(self):
        print(f'Автомобиль - {self.car_body_style}')

    def car_color(self):
        print(f'Автомобиль - {self.color} цвета')


Car(input('Состояние двгателя(on/off) - ').lower()).engine_run()  # Data input from the keyboard and result
Car(input('Состояние двгателя(on/off) - ').lower()).engine_shutdown()
Car(input('Год выпуска автомобиля - ')).car_year()
Car(input('Тип кузова автомобиля - ')).car_body_type()
Car(input('Цвет автомобиля - ')).car_color()