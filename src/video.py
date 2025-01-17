from src.get_service import *


class Video(Get_Service):

    def __init__(self, video_id: str):
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        try:
            VIDEO_INFO = self.youtube.videos().list(id=video_id, part='snippet,statistics').execute()
            self.title: str = VIDEO_INFO['items'][0]['snippet']['title']
            self.url: str = f'https://www.youtube.com/watch?v={video_id}'
            self.view_count: int = VIDEO_INFO['items'][0]['statistics']['viewCount']
            self.like_count: int = VIDEO_INFO['items'][0]['statistics']['likeCount']
        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id
