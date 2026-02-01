"""
Создайте класс `Car`, наследник `Vehicle`
"""
from typing import Self
from hw_05.base import Vehicle
from hw_05.engine import Engine

class Car(Vehicle):
    engine: Engine | None = None

    def set_engine(self: Self, engine: Engine):
        self.engine = engine
