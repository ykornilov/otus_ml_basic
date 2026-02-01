"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
from typing import Self

class VehicleError(Exception):
    pass

class LowFuelError(VehicleError):
    def __init__(self: Self):
        super().__init__('Отсустствует топливо')

class NotEnoughFuel(VehicleError):
    def __init__(self: Self, current_fuel: float, needed_fuel: float):
        super().__init__(f'Недостаточно топлива. Текущее количество топлива: {current_fuel}, необходимое количество топлива: {needed_fuel}')

class CargoOverload(VehicleError):
    def __init__(self: Self, cargo: float, max_cargo: float):
        super().__init__(f'Перегруз. Вес груза: {cargo}, максимальный вес груза: {max_cargo}')
