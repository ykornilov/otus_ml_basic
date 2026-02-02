"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from typing import Self
from hw_05.base import Vehicle
from hw_05.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self: Self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo: float = 0

    def load_cargo(self: Self, cargo: float):
        need_cargo = self.cargo + cargo
        if need_cargo > self.max_cargo:
            raise CargoOverload(need_cargo, self.max_cargo)
        
        self.cargo = need_cargo

    def remove_all_cargo(self: Self) -> float:
        cargo = self.cargo
        self.cargo = 0
        return cargo
