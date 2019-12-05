# dragonfly

A [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) generator based on [Coheed and Cambria](https://www.coheedandcambria.com) song lyrics, written in Python 3. Also mixes in text from _Coheed and Cambria_'s [Wikipedia page](https://en.wikipedia.org/wiki/Coheed_and_Cambria) in order to give the sentences a better structure.

Feel free to play around with the relative model weights!

## Prerequisites

- Python 3.7+
- Install [pipenv](https://pypi.org/project/pipenv/)
- Get a [Lyrics Genius API Client Access Token](http://genius.com/api-clients)

## Setup

```
export set GENIUS_CLIENT_ACCESS_TOKEN="my_client_access_token_here"

pipenv install
```

Alternatively, set up a `.env` file with the environment variable set. `pipenv` will automaticall load it into the virtual environment for you.

## Running

```
pipenv run python main.py
```

### Example Output

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

