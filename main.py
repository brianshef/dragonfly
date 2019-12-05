#!/bin/python
import argparse
import markovify
import lyricsgenius
import wikipediaapi

import json
import logging
from os import environ

# argparse
_description='''
A Markov Chain generator based on song lyrics.
Also mixes in text from the artist Wikipedia page
in order to give the sentences a better structure.
Adjust the weights using the option to play with the
relative amounts of material used in rendering the final model.
'''
_epilog='''
Best invoked like pipenv run python main.py, OR
pipenv run python main.py --artist "Coheed and Cambria" --wiki "Coheed_and_Cambria" | tee output.txt
'''

# Logging
LOGLEVEL = environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=LOGLEVEL,
    format='[%(asctime)s] [%(levelname)s] | %(message)s'
)
logging.getLogger(name=__name__)

# LyricsGenius API
TOKEN = environ.get('GENIUS_CLIENT_ACCESS_TOKEN')
EXCLUDE = ['(Demo)', '(Live)', 'Remix', '(Mix)', 'Acoustic', 'Radio Edit', '(Edit)', '(Skit)', '(Instrumental)', '(Snippet)', '(Bootleg)']

# Wikipedia API
WIKI_LANG = 'en'
XFORMAT = wikipediaapi.ExtractFormat.WIKI

# Markov Chain
LYRIC_MODEL_NAME = 'lyrics.json'
WIKI_MODEL_NAME = 'wiki.json'
MAX_LENGTH = 210


def get_wiki_page_text(config, lang=WIKI_LANG):
    logging.info('Getting {} wiki data for {}'.format(lang, config.wiki))
    wiki = wikipediaapi.Wikipedia(language=lang, extract_format=XFORMAT)
    page = wiki.page(config.wiki)
    if not page.exists():
        raise Exception('wiki page {} does not exist'.format(page))
    return page.text.upper()


def lg_client():
    genius = lyricsgenius.Genius(TOKEN)
    genius.remove_section_headers = True
    genius.skip_non_songs = True
    genius.excluded_terms = EXCLUDE
    return genius


def get_lyrics(client, config):
    data = []
    logging.info('Getting up to {} songs of lyric info for {}'.format(config.songs, config.artist))
    artist = client.search_artist(config.artist, max_songs=config.songs, sort="title")
    for song in artist.songs:
        try:
            data.append(song.lyrics.upper())
        except Exception as e:
            logging.warn('error getting lyrics from song {}: {}'.format(song, e))
    return data


def generate_lyric_model(config):
    lyrics = get_lyrics(lg_client(), config)
    lyric_model = markovify.Text(''.join(lyrics))
    return lyric_model.to_json()


def generate_wiki_model(config):
    wikitext = get_wiki_page_text(config)
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


def get_model(model_name, config):
    model = load_model(model_name)
    if model is not None:
        return model
    
    model_json = {}
    if model_name == LYRIC_MODEL_NAME:
        model_json = generate_lyric_model(config)
    elif model_name == WIKI_MODEL_NAME:
        model_json = generate_wiki_model(config)

    save_model(model_json, model_name)
    return markovify.Text.from_json(model_json)

    
def main(config):
    logging.info(config)

    lyric_model = get_model(LYRIC_MODEL_NAME, config)
    wiki_model = get_model(WIKI_MODEL_NAME, config)
    
    model = markovify.combine(
        [lyric_model, wiki_model],
        [config.lyric_weight, config.wiki_weight]
    )
    
    for _ in range(config.number):
        print('\n{}'.format(model.make_short_sentence(MAX_LENGTH)))


def configure():
    parser = argparse.ArgumentParser(description=_description, epilog=_epilog)
    parser.add_argument('--artist', '-a', required=True)
    parser.add_argument('--wiki', '-w', required=True)
    parser.add_argument('--songs', '-s', default=20, required=False, type=int)
    parser.add_argument('--number', '-n', default=10, required=False, type=int)
    parser.add_argument('--lyric-weight', '-p', default=1.0, required=False, type=float)
    parser.add_argument('--wiki-weight', '-q', default=0.0, required=False, type=float)
    return parser.parse_args()


if __name__ == "__main__":
    config = configure()
    main(config)
