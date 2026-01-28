from typing import Self
from abc import ABC, abstractmethod

class FileStorage(ABC):
    """
    Абстрактный класс для операций над файлами (интерфейс хранилища)
    """

    @abstractmethod
    def isExists(self: Self, fileName: str) -> bool:
        """Проверяет, существует ли файл"""
        pass

    @abstractmethod
    def info(self: Self, fileName: str) -> dict:
        """Предоставляет информацию о файле (размер, дата создания и т.д.)"""
        pass
    
    @abstractmethod
    def create(self: Self, fileName: str, data: bytes):
        """Создает новый файл"""
        pass

    @abstractmethod
    def read(self: Self, fileName: str) -> bytes:
        """Читает файл"""
        pass

    @abstractmethod
    def update(self: Self, fileName: str, data: bytes):
        """Обновляет файл"""
        pass

    @abstractmethod
    def delete(self: Self, fileName: str):
        """Удаляет файл"""
        pass