import time
import itertools


class TrafficLight:
    __color = [['R', [7, 31]], ['Y', [2, 33]], ['G', [9, 32]], ['Y', [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[1][0])


light = TrafficLight()
light.running()
