class Vehicle:  #транспорт

    __COLOR_VARIANTS = ['серый', 'синий', 'зелёный', 'белый']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)


    def get_model(self):
        return  f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
       return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        new_color = str(new_color)
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):  #седан
    __PASSENGERS_LIMIT = 5




vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'синий', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('розовый')
vehicle1.set_color('ЗЕЛЁНЫЙ')
vehicle1.owner = 'Vasyok'

# # Проверяем что поменялось
vehicle1.print_info()

