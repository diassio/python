class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is riding')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn(self, direction):
        print(f'{self.name} is turning {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} - {self.speed}km/h is Over speed!')

        else:
            print(f'{self.name} speed is {self.speed}km/h')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} - {self.speed}km/h is Over speed!')

        else:
            print(f'{self.name} speed is {self.speed}km/h')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police


town = TownCar('KIA Rio', 'white', 70)
town.go()
town.show_speed()

police = PoliceCar('Police', 'black', 180)
police.stop()
police.go()
police.show_speed()

work_car = WorkCar('Kamaz', 'black', 45)
work_car.turn('left')