from storage import LocalFileStorage, RemoteFileStorage
from media import AudioFile, PhotoFile

remoteStorage = RemoteFileStorage(url='https://example.com', bucket='my-bucket', auth_token='my-token')
audioFile = AudioFile(remoteStorage, 'my-audio-file.mp3')
audioFile.play()

photo = PhotoFile.create(LocalFileStorage('~/Pictures'), 'my-photo.jpg', data=open('my-photo.jpg', 'rb').read())
photo.view()
