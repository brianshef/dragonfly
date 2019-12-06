from .lyrics import handler as lyricshandler
from .wiki import handler as wikihandler
from .models import markov

import logging
from os import environ


# Logging
LOGLEVEL = environ.get('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=LOGLEVEL,
    format='[%(asctime)s] [%(levelname)s] | %(message)s'
)
logging.getLogger(name=__name__)


def main(config, token):
    logging.debug(config)

    lhandler = lyricshandler.Handler(config, token)
    whandler = wikihandler.Handler(config)

    lm_name = '{}-lyrics.json'.format(lhandler.arist_safename())
    wm_name = '{}-wiki.json'.format(lhandler.arist_safename())

    lmodel = markov.load_file(lm_name, lambda e: logging.warn(e))
    if not lmodel:
        lyrics = lhandler.get_lyrics()
        lmodel = markov.from_text(lyrics)
        markov.save_file(lmodel, lm_name)

    model = lmodel
    
    if config.wiki or config.wiki_weight > 0:
        wmodel = markov.load_file(wm_name, lambda e: logging.warn(e))
        if not wmodel:
            wikipage = whandler.get_wiki()
            wmodel = markov.from_text(wikipage)
            markov.save_file(wmodel, wm_name)
        model = markov.combine_models(
            [lmodel, wmodel],
            [config.lyric_weight, config.wiki_weight]
        )
    
    markov.generate_sentences(model=model, num_sentences=config.number)
