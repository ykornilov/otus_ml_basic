# Архитектура классов для работы с медиа-файлами

## Структура

```
storage/                 # Слой хранилищ (где хранятся файлы)
├── FileStorage          # Абстрактный интерфейс
├── LocalFileStorage     # Локальная файловая система
└── RemoteFileStorage    # Удаленное хранилище (S3, Azure, FTP...)

media/                   # Слой медиа-файлов (что хранится)
├── MediaFile            # Базовый класс с общими атрибутами
├── AudioFile            # Аудио: mp3, wav, flac
├── PhotoFile            # Фото: jpg, png, webp
└── VideoFile            # Видео: mp4, avi, mkv
```

## Ключевые особенности архитектуры

### 1. Разделение ответственности
- **Storage** - отвечает за операции с файлами (создание, чтение, обновление, удаление)
- **Media** - отвечает за бизнес-логику работы с медиа (метаданные, конвертация, ML)

### 2. Общие атрибуты (MediaFile)
- `name` - имя файла
- `size` - размер
- `created_at` - дата создания
- `owner` - владелец
- `metadata` - специфичные метаданные для типа

### 3. Специфичные метаданные
- **AudioFile**: битрейт, длительность, артист, альбом
- **PhotoFile**: разрешение, камера, ISO, EXIF
- **VideoFile**: разрешение, FPS, кодек, длительность

### 4. Операции
- `create()` - создание с валидацией формата
- `read()` - чтение содержимого
- `update()` - обновление с пересчетом метаданных
- `convert_to()` - конвертация формата
- `delete()` - удаление

## Примеры использования

```python
# Работа с разными хранилищами
local = LocalFileStorage('~/media')
remote = RemoteFileStorage('https://s3.example.com', 'bucket', 'token')

# Создание и воспроизведение
audio = AudioFile.create(local, 'song.mp3', data)
audio.play()

# Конвертация
audio_wav = audio.convert_to('wav')

# Работа с фото
photo = PhotoFile(remote, 'image.jpg')

# Работа с видео
video = VideoFile(local, 'movie.mp4')
```

## Масштабируемость

### Добавление нового типа медиа (DocumentFile)
```python
class DocumentFile(MediaFile):
    def __extract_metadata(self):
        return {'pages': 10, 'author': 'John'}
    # + специфичные методы
```

### Добавление нового хранилища (S3Storage)
```python
class S3Storage(FileStorage):
    def isExists(self, fileName): ...
    def create(self, fileName, data): ...
    # ... остальные методы интерфейса
```
