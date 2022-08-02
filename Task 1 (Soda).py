class Soda:  # Creating a class
    def __init__(self, taste: str):  # Creating a constructor
        self.taste = taste

    def choose_a_taste(self):  # Creating method
        if self.taste == '':
            print('Просто газировка')
        else:
            print(f'У вас газировка со вкусом "{self.taste}"')


Soda(input('Выберите вкус газировки - ')).choose_a_taste()  # Entering taste from the keyboard and result