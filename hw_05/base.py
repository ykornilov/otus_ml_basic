"""
Доработайте класс `Vehicle`
"""
from abc import ABC
from typing import Self
from hw_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self: Self, weight: float = 800, fuel: float = 0, fuel_consumption: float = 7):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption # l/100km

    def start(self: Self):
        if self.started:
            return
        
        if self.fuel <= 0:
            raise LowFuelError

        self.started = True

    def move(self: Self, distance: float):
        if not self.started:
            print('Двигатель не заведен')
            return

        need_fuel = self.fuel_consumption * distance / 100
        if self.fuel < need_fuel:
            raise NotEnoughFuel(self.fuel, need_fuel)

        self.fuel -= need_fuel
        print(f'Преодолели {distance} км. Осталось топлива: {self.fuel}')
