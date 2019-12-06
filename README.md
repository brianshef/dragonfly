# dragonfly

A [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) generator based on song lyrics ( originally [Coheed and Cambria](https://www.coheedandcambria.com) ), written in Python 3. Also mixes in text from the artist's wiki page in order to give the sentences a better structure.

## Prerequisites

- Python 3.7+
- Install [pipenv](https://pypi.org/project/pipenv/)
- Get a [Lyrics Genius API Client Access Token](http://genius.com/api-clients)

```
export set GENIUS_CLIENT_ACCESS_TOKEN="my_client_access_token_here"
```

Alternatively, set up a `.env` file with the environment variable set. `pipenv` will automaticall load it into the virtual environment for you.

## Installation

```
pipenv run python setup.py install
```

## Run It

```
pipenv run dragonfly
```


### Usage

```
usage: dragonfly [-h] [--artist ARTIST] [--wiki WIKI] [--songs SONGS]
                 [--number NUMBER] [--lyric-weight LYRIC_WEIGHT]
                 [--wiki-weight WIKI_WEIGHT]

A Markov Chain generator based on song lyrics. Also mixes in text from the
artist Wikipedia page in order to give the sentences a better structure.
Adjust the weights using the option to play with the relative amounts of
material used in rendering the final model.

optional arguments:
  -h, --help            show this help message and exit
  --artist ARTIST, -a ARTIST
  --wiki WIKI, -w WIKI
  --songs SONGS, -s SONGS
  --number NUMBER, -n NUMBER
  --lyric-weight LYRIC_WEIGHT, -p LYRIC_WEIGHT
  --wiki-weight WIKI_WEIGHT, -q WIKI_WEIGHT

Best invoked like pipenv run python main.py, OR pipenv run python main.py
--artist "Coheed and Cambria" --wiki "Coheed_and_Cambria" | tee output.txt
```

Pro tip -- use at least 100 songs ( `--songs 100` ) for best results!


#### Example Output (Coheed and Cambria)

```
SO RUN, LITTLE CHILDREN, PLAY I'LL LEAVE THE LIGHT OH, CAN YOU HEAR ME?

WE'LL LEAVE IT ON THE LOVES YOU LEFT ME?

IT'S SO TYPICAL OF ME I WANNA MAKE, JUST MAKE YOU WERE THE BEAUTY THAT WE LOVE GREAT CLOUDS ROLL OVER THE WORLD JUST FALLS APART AND THERE'S NO LETTING GO THIEVES OF OUR VICES IN YOUR ABSENCE, I WADE THROUGH THE WALLS!

WHAT DID I DO TO TO DESERVE ALL OF YOU NO, I'M CALLING FOR MERCY NOW IT'S TIME, PLEASE PRAY FOR ME...

THEN THE PARTY'S OVER HOLLY WOOD, HOLLY WOOD SHE IS CRACKED GOODS POOR HOLLY WOOD SHE IS CRACKED GOODS POOR HOLLY WOOD OH, WATCH OUT!

OH, I ASK TOO MUCH, PLEASE TURN BACK THE CLOCK READS 21:13 ALL WORK WILL STOP AND THE JURY THAT STANDS THE VERDICT ALIVE, HERE AMONG THE FENCE...

WHAT DID I DO TO ME THE LOVE OF YOUR CHEST REMEMBER WHEN WE WERE YOUNG?

WITH THIS WHAT I CAN SAY BEFORE THE SECOND STAGE TURBINE BLADE AFTER SIGNING WITH EQUAL VISION RECORDS.

IT'S FOUR A.M THE CITY THAT WE HAD TO LEAVE IT ON THE BILLBOARD CHARTS.

FOR IN THE STARS AND YOU’RE MY EVERYTHING FROM HERE TO REACT HEY NOW, WHAT IS IT, BOY?
```

