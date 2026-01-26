from typing import Self
from .file_storage import FileStorage

class LocalFileStorage(FileStorage):
    def __init__(self: Self, path: str):
        self.path = path

    def isExists(self: Self, fileName: str) -> bool:
        pass

    def info(self: Self, fileName: str) -> dict:
        pass

    def create(self: Self, fileName: str, data: bytes):
        pass

    def read(self: Self, fileName: str) -> bytes:
        pass

    def update(self: Self, fileName: str, data: bytes):
        pass

    def delete(self: Self, fileName: str):
        pass