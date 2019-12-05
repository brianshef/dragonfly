#!/bin/python
import markovify
import lyricsgenius
import wikipediaapi

import json
import logging
from os import environ

# Logging
LOGLEVEL = environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=LOGLEVEL,
    format='[%(asctime)s] [%(levelname)s] | %(message)s'
)
logging.getLogger(name=__name__)

# LyricsGenius API
TOKEN = environ.get('GENIUS_CLIENT_ACCESS_TOKEN')
ARTIST = 'Coheed and Cambria'
MAX_SONGS = 110
EXCLUDE = ['(Demo)', '(Live)', 'Remix', 'Acoustic', 'Beer Drinkers']

# Wikipedia API
WIKI_PAGE = 'Coheed_and_Cambria'
WIKI_LANG = 'en'
XFORMAT = wikipediaapi.ExtractFormat.WIKI

# Markov Chain
LYRIC_MODEL_NAME = 'lyrics.json'
WIKI_MODEL_NAME = 'wiki.json'
NUM_SENTENCES = 10
MAX_LENGTH = 280


def get_wiki_page_text(page=WIKI_PAGE, lang=WIKI_LANG):
    wiki = wikipediaapi.Wikipedia(language=lang, extract_format=XFORMAT)
    page = wiki.page(page)
    if not page.exists():
        raise Exception('wiki page {} does not exist'.format(page))
    return page.text.upper()


def init_lg_client():
    genius = lyricsgenius.Genius(TOKEN)
    genius.remove_section_headers = True
    genius.skip_non_songs = True
    genius.excluded_terms = EXCLUDE
    return genius


def get_lyrics(client):
    data = []
    artist = client.search_artist(ARTIST, max_songs=MAX_SONGS, sort="title")
    for song in artist.songs:
        data.append(song.lyrics.upper())
    return data


def generate_lyric_model():
    genius = init_lg_client()
    lyrics = get_lyrics(genius)
    lyric_model = markovify.Text(''.join(lyrics))
    return lyric_model.to_json()


def generate_wiki_model():
    wikitext = get_wiki_page_text()
    wiki_model = markovify.Text(wikitext)
    return wiki_model.to_json()


def save_model(model, filename):
    with open(filename, 'w') as outfile:
        json.dump(model, outfile)
    logging.info('saved model to {}'.format(filename))


def load_model(filename):
    model = None
    try:
        with open(filename) as f:
            data = json.load(f)
            model = markovify.Text.from_json(data)
            print('model loaded from {}'.format(filename))
    except Exception:
        logging.info('{} not found'.format(filename))
    return model


def get_model(model_name):
    model = load_model(model_name)
    if model is not None:
        return model
    
    model_json = {}
    if model_name == LYRIC_MODEL_NAME:
        model_json = generate_lyric_model()
    elif model_name == WIKI_MODEL_NAME:
        model_json = generate_wiki_model()

    save_model(model_json, model_name)
    return markovify.Text.from_json(model_json)

    
def main():
    lyric_model = get_model(LYRIC_MODEL_NAME)
    wiki_model = get_model(WIKI_MODEL_NAME)
    logging.debug('{}={}, {}={}'.format(
        'LYRICS model', type(lyric_model),
        'WIKI model', type(wiki_model)
    ))
    
    lyric_model_weight = 1
    wiki_model_weight = 1.4

    model = markovify.combine(
        [lyric_model, wiki_model],
        [lyric_model_weight, wiki_model_weight]
    )
    
    for _ in range(NUM_SENTENCES):
        print('\n{}'.format(model.make_short_sentence(MAX_LENGTH)))


if __name__ == "__main__":
    main()
