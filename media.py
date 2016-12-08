class Movie:

    def __init__(self, title, youtube_url, poster_url):
        self.title = title
        self.trailer_youtube_url = youtube_url
        self.poster_image_url = poster_url

        self._set_youtube_id()

    def _set_youtube_id(self):
        self.trailer_youtube_id = self.trailer_youtube_url.split('v=')[1]
