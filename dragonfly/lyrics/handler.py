import lyricsgenius

from . import exclude

EXCLUDE = exclude.EXCLUDE

class Handler():
    def __init__(self, config, token):
        _client = lyricsgenius.Genius(token)
        _client.remove_section_headers = True
        _client.skip_non_songs = True
        _client.excluded_terms = EXCLUDE
        self.client = _client
        self.artist = config.artist
        self.songs = config.songs
    
    def get_lyrics(self):
        lyrics = []
        artist = self.client.search_artist(self.artist, max_songs=self.songs, sort="title")
        for song in artist.songs:
            try:
                lyrics.append(song.lyrics.upper())
            except Exception:
                continue # just skip songs missing lyric data
        return lyrics
    
    def arist_safename(self):
        return "".join([c for c in self.artist if c.isalpha() or c.isdigit()]).strip()
