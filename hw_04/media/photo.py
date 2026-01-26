from typing import Self
from storage import FileStorage
from .media import MediaFile

class PhotoFile(MediaFile):
    def __init__(self: Self, storage: FileStorage, name: str):
        super().__init__(storage, name)

    def __extract_metadata(self: Self) -> dict:
        return {
            'resolution': '1920x1080',
            'camera_make': 'Canon',
            'camera_model': 'EOS 5D',
            'iso': 400,
        }

    @staticmethod
    def create(storage: FileStorage, name: str, data: bytes):
        if not name.endswith(('.jpg', '.jpeg', '.png', '.webp')):
            raise ValueError('Неподдерживаемый формат')
        storage.create(name, data)
        return PhotoFile(storage, name)

    def read(self: Self) -> bytes:
        return self.storage.read(self.name)

    def update(self: Self, data: bytes):
        self.storage.update(self.name, data)
        self.metadata = self.__extract_metadata()

    def view(self: Self):
        """Отображает фото"""
        pass

    def convert_to(self: Self, target_format: str) -> Self:
        output_name = self.name.rsplit('.', 1)[0] + f'.{target_format}'
        converted_data = self.read()  # + конвертация
        return PhotoFile.create(self.storage, output_name, converted_data)

    def delete(self: Self):
        self.storage.delete(self.name)