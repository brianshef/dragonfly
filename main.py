#!/bin/python
import markovify
import lyricsgenius
from os import environ

TOKEN = environ.get('GENIUS_CLIENT_ACCESS_TOKEN')
ARTIST = 'Coheed and Cambria'
MAX_SONGS = 100
EXCLUDE = ['(Demo)', '(Live)', 'Remix', 'Acoustic']
NUM_SENTENCES = 10

def init_client():
    genius = lyricsgenius.Genius(TOKEN)
    genius.remove_section_headers = True
    genius.skip_non_songs = True
    genius.excluded_terms = EXCLUDE
    return genius


def get_data(client):
    data = []
    artist = client.search_artist(ARTIST, max_songs=MAX_SONGS, sort="title")
    for song in artist.songs:
        data.append(song.lyrics.upper())
    return data


def main():
    genius = init_client()
    data = get_data(genius)
    model = markovify.Text(''.join(data))
    for _ in range(NUM_SENTENCES):
        print(model.make_sentence())


if __name__ == "__main__":
    main()

