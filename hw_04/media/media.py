from typing import Self
from abc import ABC, abstractmethod
from storage import FileStorage

class MediaFile(ABC):
    """Базовый класс для всех медиа-файлов"""

    def __init__(self: Self, storage: FileStorage, name: str):
        self.storage = storage
        self.name = name

        if not self.storage.isExists(self.name):
            raise FileNotFoundError("File not found")

        fileInfo = self.storage.info(self.name)
        self.size = fileInfo['size']
        self.created_at = fileInfo['created_at']
        self.owner = fileInfo.get('owner', None)

        self.metadata = self.__extract_metadata()

    @abstractmethod
    def __extract_metadata(self: Self) -> dict:
        """Извлекает специфичные метаданные для типа файла"""
        pass